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

#     g.graph = {
#         'A': {'B': 10, 'C': 15},
#         'B': {'D': 15, 'E': 5, 'C': 2},
#         'C': {'F': 50, 'G': 25},
#         'D': {},
#         'E': {'C': 5},
#         'F': {'E': 10},
#         'G': {'F': 20}
#     }

# I'm not sure switching to using dictionaries made this easier for me.
# Based on the after class notes, I can see that the Graph should be a
# dictionary with what seems to be a vertice name as a key, and the value
# being a nested dictionary whose key - value pairs are the connected vertice
# name - weight of connection (which I assume is directional). I am also
# assuming that individual key, value pair that represents each vertice
# will also be a dictionary of exactly one item (technically it could be
# another data type like a Node with a value & data, or other options).
# When added to the graph it should not be simply inserted as a nested
# dictionary (which would result in 3 levels of nested dictionaries).
# Instead this 'vertice' shall have it's key, value pair added to the
# dictionary of the graph property.


class Graph(object):
    """ Allows for connecting multiple Vertice, which may have weights & direction
        For now we use dictionary keys as Vertice names & values as dictionary
        of key: value pair of name: weight of connection to neighboring vertice
    """
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def add_vert(self, val):
        """ Adding Vertice to graph if it does not already exist
            For now we use dictionary key as vertice name with values holding
            dictionary of connected vertice name : connection weight
        """
        # check to see if the vert already exists: if so raise exception
        if self.has_vert(val):
            raise ValueError('That vertice is already present')
        self.graph.update(val)  # put the key:value pair into graph

    def has_vert(self, val):
        """ Check to see if this vertice is already in the graph.
            For now, check if the name is a key in self.graph
        """
        # checks for a key in the graph
        return val in self.graph.keys()  # Bool return

    def add_edge(self, v1, v2, weight):
        """ This is adding a directional weighted connection from v1 to v2
            v1 and v2 must be already existing vertices in the graph
        """
        # it is unclear to me if v1 and v2 are vertice names, or vertice
        # objects (which are dictionaries for now)
        # I'm going with vertice names as that is how I imagine the use
        # case for this, but I could easily see the other way as valid.
        # don't forget to validate
        if not self.has_vert(v1):
            raise ValueError('First given Vertice is not present')
        if not self.has_vert(v2):
            raise ValueError('Second given Vertice is not present')
        old = self.graph[val]
        # add a relationship and weight between two verts


    def get_neighbors(self, val):
        """ Return all verticies that the given val vertice connects out to
        """
        # Given a val (key), return all adjacent verts
        # If we only want the names of the vertice, we would do the following:
        # return self.graph[val].keys()
        # To return the "vertice objects" (currently a dictionary)
        return {name: self.graph[name] for name in self.graph[val].keys()}
