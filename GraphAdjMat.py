# credits: https://www.youtube.com/watch?v=HDUzBEG1GlA# credits: https://www.youtube.com/watch?v=HDUzBEG1GlA
# Undirected Graph

class Vertex:
    def __init__(self,n):
        self.name = n

class Graph:
    vertices = {}
    edges = []
    edgeIndices = {}

    def addVertex(self,vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.edgeIndices[vertex.name] = len(self.edgeIndices)
            return True
        else:
            return False

    def addEdge(self,u,v,weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edgeIndices[u]][self.edgeIndices[v]] = weight
            self.edges[self.edgeIndices[v]][self.edgeIndices[u]] = weight
            return True
        else:
            return False

    def printGraph(self):
        for v, i in sorted(self.edgeIndices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j],end='')
            print('')

# Undirected Graph
