from vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())  # make a class iterabe

    def add_vertax(self, node_value):
        self.num_vertices += 1  # increa number of vertice in graph
        new_vertax = Vertex(node_value)  # make a new Vertax valued with param
        self.vert_dict[node_value] = new_vertax  # add it to vert_dict

        return new_vertax

    def get_vertax(self, target_value):
        if target_value in self.vert_dict:  # searching key  of vert_dict
            return self.vert_dict[target_value]  # if exist return value
        else:
            return None

    def add_edge(self, frm_node, to_node, weight):
        if frm_node not in self.vert_dict:  # if frm_node is not exist in graph add it
            self.add_vertax(frm_node)
        if to_node not in self.vert_dict:  # if to_node is not exist in graph add it
            self.add_vertax(to_node)  # if to_node is not exist in graph add it

        # using Vertax class method to connect two vertax
        self.vert_dict[frm_node].add_neighbor(self.vert_dict[to_node], weight)
        self.vert_dict[to_node].add_neighbor(self.vert_dict[frm_node], weight)  # we suppose indirected Graph

    def reset_verticles(self):
        for id, vertex in self.vert_dict.items():  # initialize
            vertex.distance = float('inf')
            vertex.visited = False
            vertex.previous = None

    def __str__(self):
        return "number of vertice is {}".format(self.num_vertices)
