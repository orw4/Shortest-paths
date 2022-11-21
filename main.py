# Gets a graph representing a map and finds the shortest paths from a given point to all the points
# 21/11/2022

class Map:
    def __init__(self,vertices,edges,start):
        self.vertices = vertices
        self.edges = edges
        self.start = start

    # the vertices are a list of vertices (represented by letters)
    # the edges are a list of lists, each list has 2 vertices and a weight (a number representing the distance)
    # the start and end are the beginning point and the destination of the path

    # finds the index of a given vertex
    def findVertex(self,vertex):
        for v in range(len(self.vertices)):
            if self.vertices[v] == vertex:
                return v
        return -1

    # returns a list of neighbors of a given vertex with the weight of the common edge
    def findNeighbors(self,vertex):
        neighbors = []
        for e in self.edges:
            if vertex in e:
                if e[0] == vertex:
                    neighbors.append([e[1],e[2]])
                else:
                    neighbors.append([e[0],e[2]])
        return neighbors

    # sets the distance of each vertex from the beginning to the maximum
    def setDistance(self):
        maximal = 0
        for e in self.edges:
            maximal = max(maximal,e[2])
        distances = [maximal * len(self.vertices)] * len(self.vertices)
        distances[self.findVertex(self.start)] = 0
        return distances

    def shortestPath(self):
        distances = self.setDistance()
        searched = [self.start]
        toSearch = [self.start]
        while toSearch != []:
            for v1 in toSearch:
                for v2 in self.findNeighbors(v1):
                    if distances[self.findVertex(v2[0])] >= distances[self.findVertex(v1)] + v2[1]:
                        distances[self.findVertex(v2[0])] = distances[self.findVertex(v1)] + v2[1]
                        toSearch.append(v2[0])
                toSearch.remove(v1[0])
                searched.append(v1[0])
        return distances


v = ['u','a','b','c','d','e']
e = [['u','a',1],['u','b',3],['a','d',5],['a','c',4],['b','c',5],['b','d',4],['c','e',6],['d','e',2]]
s = 'u'
m = Map(v,e,s)
print(m.shortestPath())