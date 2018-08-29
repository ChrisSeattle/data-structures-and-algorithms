from .queue.queue import Node, Queue

class Animal(object):
    """ This will be an animal object to be used by Animal_Shelter
    """
    def __init__(self, pet_name, pet_type):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.tag = 0


class AnimalShelter(object):
    """ AnimalShelter which holds only dogs and cats.
        Users can select to adopt a dog, a cat, or no preference.
        The shelter operates using a first-in, first-out approach.
    """
    def __init__(self, data=None):
        """ Initialize Queue with front & back set to None and _length of 0, if no data passed
            If initialized with data, creating add a Node in the Queue for each value in the iterable.
        """
        self.front = None
        self.back = None
        self.dogs = Queue()
        self.cats = Queue()
        self._length = 0
        self.tag = 0
        # next animal will get this tag added to their object,
        # essentially an incrementing count of incoming pets
        # this also works as a total number of cats & dogs the
        # shelter has had, but not for current total.

    def __len__(self):
        return self._length

    def __str__(self):
        return f'Total Tagged Animals: {self.tag} | Sheltered Animals: {self._length}'

    def __repr__(self):
        return f'<Total Intake: {self.tag} | Length: {self._length}>'

    def enqueue(self, animal):
        """ Adds animal to the shelter. animal can be either a dog or a cat object.
            On adding animal, increments _length. First in, First out.
        """
        if animal.pet_type == 'dog':
            self.tag += 1
            animal.tag = self.tag
            self.dogs.enqueue(animal)
            self._length += 1
        elif animal.pet_type == 'cat':
            self.tag += 1
            animal.tag = self.tag
            self.cats.enqueue(animal)
            self._length += 1
        else:
            return f'Sorry, we only take dogs and cats here!'

    def dequeue(self, pref):
        """ The user may have a preference equal to 'dog' or 'cat', or 'any'.
            if the user gave 'any' for preference, they will get whichever
            animal the shelter has had the longest. Likewise, if they give
            the other options for preference, they will get whichever of that
            type of animal the shelter has had the longest.
        """
        if pref == 'any':
            if self.dogs.front.val.tag < self.cats.front.val.tag:
                pref = 'dog'
            elif self.cats.front.val.tag < self.dogs.front.val.tag:
                pref = 'cat'
        if pref == 'dog':
            self._length -= 1
            return self.dogs.dequeue()
        elif pref == 'cat':
            self._length -= 1
            return self.cats.dequeue()
        else:
            return f'Sorry, we only give out dogs and cats here!'


