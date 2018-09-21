from .breadth_first import Node, Queue


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

    def get_edges(self, arr):
        """ Input is an array of intended connections. Going in order, if any
            of the connections do not exist, return False. If they all exist,
            return the sum total of all the connections.
        """
        total = 0
        curr = arr[0]
        if not self.has_vert(curr):
            return (False, 0)
        for city in arr:
            if city == curr:
                continue
            if city not in self.graph[curr].keys():
                return (False, 0)
            total += self.graph[curr][city]
            curr = city
        return (True, total)

    def depth_first(self):
        """ depth first traversal. This starts with first key in self.graph
        """
        if len(self.graph) == 0:
            return None
        temp = []
        hold = []
        results = dict()
        curr = list(self.graph.keys())[0]
        hold.append(curr)

        while len(hold) > 0:
            curr = hold.pop()  # Technically repeated values won't change order
            results[curr] = True  # Tracking both visited and traversal order
            temp = list(self.graph[curr].keys())
            while len(temp) > 0:
                val = temp.pop()
                if val not in results:
                    hold.append(val)  # skipping val if it is already reported
        print(list(results.keys()))
        return list(results.keys())

    def breadth_first(self, val):
        """ Accepts a starting node as input, then traverses all nodes/vertices
            of the graph in a breadth first approach. Prints these out in order
            they were visited.
            This could be simplified (and not use  Queue) if we always work
            with the key-value pairs of node name to dictionary of connections.
        """
        if not self.has_vert(val):
            raise ValueError('Starting vertice is not in the Graph')

        visited = dict()
        q = Queue()
        startNode = Node(val)
        q.enqueue(startNode)
        visited[val] = True
        result = []
        while q:
            for n in self.graph[q.front.val].keys():
                if n not in visited:
                    visited[n] = True
                    newNode = Node(n)
                    q.enqueue(newNode)
            result.append(q.dequeue().val)
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

