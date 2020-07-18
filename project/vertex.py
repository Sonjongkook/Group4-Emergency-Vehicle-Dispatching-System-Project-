import sys


class Vertex:
    # initialize member variables of the vertex
    def __init__(self, node_value):
        self.id = node_value
        self.neighbor = {}
        self.distance = float('inf')
        self.visited = False

        self.previous = None  # predecessor which is essential for graph

    def add_neighbor(self, adjacent, weight=0):
        self.neighbor[adjacent] = weight

    def get_id(self):
        return self.id

    def get_weight(self, adjacent):
        return self.neighbor[adjacent]

    def set_distance(self, d):
        self.distance = d

    def get_distance(self):
        return self.distance

    def set_visited(self):
        self.visited = True

    def set_previous(self, current):  # predecessor is important to backtrackinng shortest route
        self.previous = current

    def get_previous(self):
        return self.previous

    def __lt__(self, other):
        return self.id < other.id  # to implement heapify
