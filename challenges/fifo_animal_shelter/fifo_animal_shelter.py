from ... data_structures.queue.queue import Node, Queue

class Animal_Shelter(object):
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
        self._length = 0
        self.dogs = Queue()
        self.cats = Queue()

        # if data is not None:
        #     try:
        #         vals = iter(data)
        #     except TypeError:
        #         vals = [data]
        #     for i in vals:
        #         newNode = Node(i)
        #         if self.front is None:  # this is the first node in queue
        #             self.front = newNode
        #         elif self.back is None:  # this is the second node in queue
        #             self.front._next, self.back = newNode, newNode
        #         else:
        #             self.back._next, self.back = newNode, newNode
        #         self._length += 1

    def __len__(self):
        return self._length

    def __str__(self):
        return f'Front: {self.front} | Back: {self.back} | Length: {self._length}'

    def __repr__(self):
        return f'<Front: {self.front} | Back: {self.back} | Length: {self._length}>'

    def enqueue(self, animal):
        """ Adds animal to the shelter. animal can be either a dog or a cat object.
            On adding animal, increments _length. First in, First out.
        """
        animal.type
        newNode = Node(animal)
        if self.front is None:  # this is the first node in queue
            self.front = newNode
        elif self.back is None:  # this is the second node in queue
            self.front._next, self.back = newNode, newNode
        else:
            self.back._next, self.back = newNode, newNode
        self._length += 1

    def dequeue(self):
        """ Returns the node that is in the front of the queue.
            Removes it from the queue and deincrements the _length
        """
        temp = self.front
        self.front = self.front._next
        temp._next = None
        self._length -= 1
        return temp

    def peek(self):
        return self.front



