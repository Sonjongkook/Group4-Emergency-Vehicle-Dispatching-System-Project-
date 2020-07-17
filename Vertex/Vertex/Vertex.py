import sys

class Vertex:
	#initialize member variables of the vertex
	def __init__(v, node):
		v.value = node
		v.neighbor = {}
		v.distance = float('inf')
		v.visited = False

	def add_neighbor(v, adjacent, weight):
		self.neighbor[adjacent] = weight

	def get_value(v):
		return v.value

	def get_weight(v, adjacent):
		return v.neighbor[adjacent]

	def set_distance(v, d):
		v.distance = d

	def get_distance(v):
		return v.distance

	def set_visited(v):
		v.visited = True




