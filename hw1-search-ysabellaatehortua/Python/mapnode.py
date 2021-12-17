"""
The MapNode class represents a single node in a Map.

Adam Eck
10/18/2021
"""

class MapNode():
    """
    Creates a new MapNode

    lat: the latitude coordinate of the MapNode
    long: the longitude coordinate of the MapNode
    """
    def __init__(self, lat, long):
        # save the params
        self.lat = lat
        self.long = long

        # create the collections
        self.neighbors = []
        self.costs = {}

    """
    Adds a MapNode as a neighbor

    node: the MapNode to add as a neighbor
    """
    def addNeighbor(self, node, cost):
        if node not in self.neighbors:
            self.neighbors.append(node)
            self.costs[node] = cost
