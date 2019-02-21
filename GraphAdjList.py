# credits: https://www.youtube.com/watch?v=HDUzBEG1GlA
# Undirected Graph

class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = []

    def addNeighbour(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}

    def addVertex(self,vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def addEdge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.addNeighbour(v)
                if key == v:
                    value.addNeighbour(u)
            return True
        else:
            return False

    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
