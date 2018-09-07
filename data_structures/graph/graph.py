class Vertice:
    """
    """
    def __init__(self, value):
        self.value = value
        self.vertices = []

    def __repr__(self):
        pass

    def __str__(self):
        pass


class Graph(object):
    """ Docstring
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
        """
        """
        # use val to crete a new Vertice
        # and ertice to sel.graph
        # check to see ifthe vert already existss: is so raise exception
            # create a helper method for this

        # Updated Notes:
        # add vertice to self.graph
        # check to see if the vert already exists: if so raise exception
            # create a helper method
        pass

    def has_vert(self, val):
        """
        """
        # checks for a key in the graph
        pass

    def add_edge(self, v1, v2, weight):
        """
        """
        # add a relationship and weight between two verts
        # don't forget to validate
        pass

    def get_neighbors(self, val):
        """
        """
        # Given a val (key), return all adjacent verts
        pass
