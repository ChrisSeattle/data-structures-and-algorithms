# this will probably be used later. For now we are using dictionaries.
# class Vertice:
#     """ These will be used as Node like objects in our Graph data structure.
#         Each vertice is away of all the vertices it connects out to.
#     """
#     def __init__(self, val):
#         self.val = val
#         self.vertices = []

#     def __repr__(self):
#         return f'{self.val}'

#     def __str__(self):
#         return f'<Vertice | Val: {self.val} | Connects: {self.vertices} | Connections: {len(self.vertices)}>'

class Node(object):
    """ Node used in Binary tree. Is aware of a left and a right
        for following Nodes, holds a value and data.
    """
    def __init__(self, val, data=None, left=None, right=None):
        self.val = val
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | Val: {self.val} | Data: {self.data} | Left: {self.left} | Right: {self.right}>'


class Queue(object):
    """ This Queue works with Nodes as both inputs and outputs.
    """
    def __init__(self):
        """ Initialize Queue with front & back set to None and _length of 0.
            This version of Queue will not take in any initital values or Nodes.
        """
        self.front = None
        self.back = None
        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):
        return f'Front: {self.front} | Back: {self.back} | Length: {self._length}'

    def __repr__(self):
        return f'<Front: {self.front} | Back: {self.back} | Length: {self._length}>'

    def enqueue(self, newNode):
        """ Adds a node for the passed val and increments _length.
            First in, First out.
        """
        if self.front is None:  # this is the first node in queue
            self.front, self.back = newNode, newNode
        elif self.back is self.front:  # this is the second node
            self.front._next, self.back = newNode, newNode
        else:
            self.back._next, self.back = newNode, newNode
            newNode._next = None
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


class Graph(object):
    """ Allows for connecting multiple Vertice, which may have weights & direction
        For now we use dictionary keys as Vertice names w/ values as dictionary
        of key:value pair of name:weight of connection to neighboring vertice
    """
    def __init__(self):
        self.graph = {}

    def __str__(self):
        return f'{[*self.graph]}'

    def __repr__(self):
        return f'<Graph | Vertices: {[*self.graph]} | Length: {len(self.graph)}>'

    def __len__(self):
        return len(self.graph)

    def breadth_first(self, val):
        """ Accepts a starting node as input, then traverses all nodes/vertices
            of the graph in a breadth first approach. Prints these out in order
            they were visited
        """
        if not self.has_vert(val):
            raise ValueError('Starting vertice is not in the Graph')

        visited = dict()
        q = Queue()
        q.enqueue(val)
        visited[val] = True
        result = []
        while q:
            for n in self.graph[q.front].keys():
                if n not in visited:
                    visited[n] = True
                    q.enqueue(n)
            result.append(q.dequeue)
        return result

    def add_vert(self, val):
        """ Adding Vertice to graph if it does not already exist
            For now we use dictionary key as vertice name with values holding
            dictionary of connected vertice name : connection weight
        """
        rel = []
        err = ''
        if isinstance(val, dict):
            val, rel = list(val.keys()), list(val.values())
        else:
            if not isinstance(val, list):
                val = list(val)
            for ea in val:
                rel.append({})
        for i in range(len(val)):
            # check to see if the vert already exists, if so save for later report
            if self.has_vert(val[i]):
                err += f'{val[i]} '
            else:
                self.graph[val[i]] = rel[i]
            # self.graph.update(val)  # put the key:value pair into graph
        # if any passed vertices already existed, send ValueError
        if len(err) > 0:
            raise ValueError(f'Vertice(s) {err} already present')
        return True

    def has_vert(self, val):
        """ Check to see if this vertice is already in the graph.
            For now, check if the name is a key in self.graph
        """
        return val in self.graph.keys()  # Bool return

    def add_edge(self, v1, v2, weight):
        """ This is adding a directional weighted connection from v1 to v2
            v1 and v2 must be already existing vertice names in the graph
        """
        if not self.has_vert(v1):
            raise ValueError('First given Vertice is not present')
        if not self.has_vert(v2):
            raise ValueError('Second given Vertice is not present')
        # Overwrite if previously the v1 to v2 connection existed
        # But also, preserve any other connections from v1 to other vertices
        self.graph[v1][v2] = weight

    def get_neighbors(self, val):
        """ Return all verticies that the given val vertice connects out to
        """
        # Given a val (key), return all adjacent verts
        # test this vertice exists in graph
        if val not in self.graph.keys():
            raise ValueError('That vertice is not present')
        return list(self.graph[val].keys())
