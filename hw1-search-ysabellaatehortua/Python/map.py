"""
Map class defines a graph representation for the city map.

Adam Eck
10/18/2021
"""

import mapnode


class Map():
    """
    Creates a new Map
    """
    def __init__(self):
        # create the fields
        self.startNode = None

        # create the collections
        self.nodes = []
        self.nodeMap = {}
        self.goalNodes = []


    """
    Adds a new MapNode to the Map

    node: the MapNode to add
    """
    def addMapNode(self, node):
        # add the state to the Map
        self.nodes.append(node)
        self.nodeMap[(node.lat, node.long)] = node


    """
    Writes the Map to a file

    filename: the name of the file in which to write the Map
    """
    def writeToFile(self, filename):
        file = open(filename, "w")

        # write the nodes to file
        file.write("Nodes:\n")
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            line = "{}: {}\n".format(i, (node.lat, node.long))
            file.write(line)

        # write the edges to file
        file.write("\nEdges:\n")
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            line = "{}: ".format(i)
            for j in range(len(node.neighbors)):
                neighbor = node.neighbors[j]
                if j > 0:
                    line += ", "
                line += "({}; {})".format(self.nodes.index(neighbor), round(node.costs[neighbor], 4))
            file.write("{}\n".format(line))

        # write the start node to file
        file.write("\nStart Node:\n")
        file.write("{}\n".format(self.nodes.index(self.startNode)))

        # finally, write the goal nodes to file
        file.write("\nGoal Nodes:\n")
        line = ""
        for i in range(len(self.goalNodes)):
            node = self.goalNodes[i]
            if (i > 0):
                line += ", "
            line += str(self.nodes.index(node))
        file.write("{}\n".format(line))

        # close the file
        file.close()

"""
Reads a Map from file

filename: the name of the file containing the Map
"""
def readFromFile(filename):
    # create the map to return
    map = Map()

    # read from the file
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # process the lines
    inNodes = False
    inEdges = False
    inStart = False
    inGoals = False
    for line in lines:
        # does this line need processing?
        if (line == "\n"):
            continue
        elif (line.startswith("Nodes")):
            inNodes = True
            continue
        elif (line.startswith("Edges")):
            inNodes = False
            inEdges = True
            continue
        elif (line.startswith("Start")):
            inEdges = False
            inStart = True
            continue
        elif (line.startswith("Goal")):
            inStart = False
            inGoals = True
            continue

        # drop the newline
        line = line.replace("\n", "")

        # process the info on the line
        if (inNodes):
            split = line.split(":")
            loc = split[1]
            splitLoc = loc.replace("(", "").replace(")", "").replace(" ", "").split(",")

            nodeNum = int(split[0])
            lat = float(splitLoc[0])
            long = float(splitLoc[1])

            node = mapnode.MapNode(lat, long)
            map.addMapNode(node)
        elif (inEdges):
            split = line.split(":")
            neighbors = split[1]
            neighborsSplit = neighbors.replace(" ", "").split(",")

            nodeNum = int(split[0])
            node = map.nodes[nodeNum]
            for str in neighborsSplit:
                tupleSplit = str.replace("(", "").replace(")", "").replace(" ", "").split(";")

                neighborNum = int(tupleSplit[0])
                cost = float(tupleSplit[1])
                node.addNeighbor(map.nodes[neighborNum], cost)
        elif (inStart):
            startNum = int(line)
            map.startNode = map.nodes[startNum]
        elif (inGoals):
            line = line.replace(" ", "")
            split = line.split(",")
            for str in split:
                nodeNum = int(str)
                map.goalNodes.append(map.nodes[nodeNum])

    # return the read in map
    return map
