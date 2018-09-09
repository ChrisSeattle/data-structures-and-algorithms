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
# As dictionaries, there are plenty of ambiguities on what a singluar
# vertice looks like, and in what context we are managing the entire
# vertice (currently dictionary item) object vs. vertice name (or value)

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
