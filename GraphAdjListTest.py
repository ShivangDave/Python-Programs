from GraphAdjList import Graph
from GraphAdjList import Vertex

g = Graph()
a = Vertex('A')
g.addVertex(a)
g.addVertex(Vertex('B'))

for i in range(ord('A'),ord('K')):
    g.addVertex(Vertex(chr(i)))

edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FJ','GJ']
for edge in edges:
    g.addEdge(edge[:1],edge[1:])

g.printGraph()
