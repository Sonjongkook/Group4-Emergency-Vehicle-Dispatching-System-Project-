import sys

class Vertex:
	#initialize member variables of the vertex
	def __init__(self, node):
		self.value = node
		self.neighbor = {}
		self.distance = float('inf')
		self.visited = False

	def add_neighbor(self, adjacent, weight):
		self.neighbor[adjacent] = weight

	def get_value(self):
		return self.value

	def get_weight(self, adjacent):
		return self.neighbor[adjacent]

	def set_distance(self, d):
		self.distance = d

	def get_distance(self):
		return self.distance

	def set_visited(self):
		self.visited = True




