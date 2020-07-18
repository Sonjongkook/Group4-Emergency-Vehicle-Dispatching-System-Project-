import heapq
import math


def dijkstra(graph, start):  # parameters are node
    # initialize distances for all of the nodes in the graph
    # starting node should be 0, all other nodes start at infinity

    target_zipcode = None
    shortest_distance = None
    start.set_distance(0)  # change default value infinite to 0
    # create a list that consists of pairs for all of the nodes and their distances
    # graph class is iteralble thanks to __iter__
    unvisited_nodes = [(node.get_distance(), node) for node in graph]
    # use a priority queue to sort the available_nodes by their distance
    heapq.heapify(unvisited_nodes)
    while unvisited_nodes:
        # set the node with the least distance to current and mark it as visited
        current = heapq.heappop(unvisited_nodes)[1]
        current.set_visited()
        # check all of the current node's neighbors and update their distances
        for next in current.neighbor:
            if next.visited:
                continue  # go from where iterate begin
            temp_distance = current.get_distance() + current.get_weight(next)

            if temp_distance < next.get_distance():
                next.set_distance(temp_distance)
                next.set_previous(current)
                target_zipcode = next.get_id()

        # rebuild priority queue with new distances assigned to unvisited nodes
        while unvisited_nodes:
            heapq.heappop(unvisited_nodes)
        unvisited_nodes = [(node.get_distance(), node)
                           for node in graph if not node.visited]
        heapq.heapify(unvisited_nodes)

    # Once all of the nodes have been visited and their shortest distances calculated,
        # return the value of the shortest distance from the start node to the goal node
