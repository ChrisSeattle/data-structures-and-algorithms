from .fifo_animal_shelter import Queue, Node, Animal, AnimalShelter
import pytest


def test_alive():
    """ Does the testing file run
    """
    pass


def test_animal_exists():
    """ Do we see Animal
    """
    assert Animal


def test_animal_shelter():
    """ Do we see AnimalShelter
    """
    assert AnimalShelter


def test_queue_exists():
    """ Do we see Queue
    """
    assert Queue


@pytest.fixture
def empty_q():
    return AnimalShelter()

@pytest.fixture
def short_set():
    first = Animal('first_pet', 'dog')
    second = Animal('dog_also_second', 'dog')
    third = Animal('cat_come_in_third', 'cat')
    fourth = Animal('dog_is_fourth', 'dog')
    fifth = Animal('cat_for_fifth', 'cat')
    a = AnimalShelter()
    a.enqueue(first)
    a.enqueue(second)
    a.enqueue(third)
    a.enqueue(fourth)
    a.enqueue(fifth)
    return a


def test_create_instance_of_animal_shelter(empty_q):
    """ can we create a Queue instance with no input values
    """
    assert isinstance(empty_q, AnimalShelter)


def test_animal_shelter_default_property(empty_q):
    """ Do the default settings work as expected
    """
    assert empty_q.front is None
    assert empty_q.back is None
    assert isinstance(empty_q.dogs, Queue)
    assert isinstance(empty_q.cats, Queue)
    assert empty_q._length == 0
    assert empty_q.tag == 0


def test_shelter_str_format_on_empty(empty_q):
    """ Do we get the expected str return on empty shelter
    """
    expected = 'Total Tagged Animals: 0 | Sheltered Animals: 0'
    actual = str(empty_q)
    assert expected == actual


def test_animal_shelter_enqueue_exists():
    """ Is the enqueue method present in the AnimalShelter constructor
    """
    assert AnimalShelter.enqueue


def test_add_dog_successful(empty_q):
    """ Can we insert a single Animal object with pet_type of 'dog'
        and see the value in the front position
    """
    fluffy = Animal('Fluffy', 'dog')
    empty_q.enqueue(fluffy)
    assert empty_q.dogs.front.val.pet_name == 'Fluffy'
    assert empty_q.dogs.front.val.tag == 1
    assert len(empty_q) == 1
    assert len(empty_q.dogs) == 1


def test_add_cat_successful(empty_q):
    """ Can we insert a single Animal object with pet_type of 'cat'
        and see the value in the front position
    """
    scratchy = Animal('Scratchy', 'cat')
    empty_q.enqueue(scratchy)
    assert empty_q.cats.front.val.pet_name == 'Scratchy'
    assert empty_q.cats.front.val.tag == 1
    assert len(empty_q) == 1
    assert len(empty_q.cats) == 1


def test_add_cat__and_dog_successful(empty_q):
    """ Can we insert two Animal objects with each pet_type
        and see the correct value in the front position
    """
    scratchy = Animal('Scratchy', 'cat')
    fluffy = Animal('Fluffy', 'dog')
    empty_q.enqueue(scratchy)
    empty_q.enqueue(fluffy)
    assert empty_q.cats.front.val.pet_name == 'Scratchy'
    assert empty_q.dogs.front.val.pet_name == 'Fluffy'
    assert empty_q.cats.front.val.tag == 1
    assert empty_q.dogs.front.val.tag == 2
    assert len(empty_q) == 2


def test_dequeue_exists():
    """ can se see dequeue for AnimalShelter
    """
    assert AnimalShelter.dequeue


def test_dequeue_cat(short_set):
    """ if user wants a cat, does the shelter give a cat
    """
    adopt = short_set.dequeue('cat').val
    assert adopt.pet_type == 'cat'


def test_dequeue_dog(short_set):
    """ if the user wants a dog, does the shelter give a dog
    """
    adopt = short_set.dequeue('dog').val
    assert adopt.pet_type == 'dog'

def test_dequeue_any(short_set):
    """ if the user requests any, does the shelter give the first in
    """
    dog_tag = short_set.dogs.front.val.tag
    cat_tag = short_set.cats.front.val.tag
    tag = min(dog_tag, cat_tag)
    adopt = short_set.dequeue('any').val
    assert adopt.tag == tag


