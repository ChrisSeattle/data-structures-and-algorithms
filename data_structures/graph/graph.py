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


# I'm not sure switching to using dictionaries made this easier for me.
# As dictionaries, there are plenty of ambiguities on what a singluar
# vertice looks like, and in what context we are managing the entire
# vertice (currently dictionary item) object vs. vertice name (or value)
# I will assume all references to 'val', 'v1', or 'v2' are for the keys in
# in the dictionary of self.graph. This means the add_vert method only
# adds the name of the vertice, but cannot handle

class Graph(object):
    """ Allows for connecting multiple Vertice, which may have weights & direction
        For now we use dictionary keys as Vertice names & values as dictionary
        of key: value pair of name: weight of connection to neighboring vertice
    """
    def __init__(self):
        self.graph = {}

    def __str__(self):
        return f'{[*self.graph]}'

    def __repr__(self):
        return f'<Graph | Vertices: {[*self.graph]} | Length: {len(self.graph)}>'

    def __len__(self):
        return len(self.graph)

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
            # check to see if the vert already exists, if so save it to report later
            # import pdb; pdb.set_trace()
            if self.has_vert(val[i]):
                err += f'{val[i]} '
            else:
                self.graph[val[i]] = rel[i]
            # self.graph.update(val)  # put the key:value pair into graph
            # if len(rel) > 0:
            #     self.add_vert(i)
            #     [self.add_edge(i, v2, weight) for (v2, weight) in rel[i].items()]
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
            v1 and v2 must be already existing vertices in the graph
        """
        # it is unclear to me if v1 and v2 are vertice names, or vertice
        # objects (which are dictionaries for now)
        # I'm going with vertice names as that is how I imagine the use
        # case for this, but I could easily see the other way as valid.
        # don't forget to validate
        if v1 not in self.graph.keys():
            raise ValueError('First given Vertice is not present')
        if v2 not in self.graph.keys():
            raise ValueError('Second given Vertice is not present')
        # Overwrite if previously the v1 to v2 connection existed
        # But also, preserve any other connections from v1 to other vertices
        self.graph[v1][v2] = weight
        # add a relationship and weight between two verts

    def get_neighbors(self, val):
        """ Return all verticies that the given val vertice connects out to
        """
        # Given a val (key), return all adjacent verts
        # If we only want the names of the vertice, we would do the following:
        # return self.graph[val].keys()
        # To return the "vertice objects" (currently a dictionary)
        return list(self.graph[val].keys())
