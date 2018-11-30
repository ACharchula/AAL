from src.Graph import *
from src.Algorithms import *
from src.ConnectedGraphGenerator import *
import time
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(10000)

graphToDraw = nx.Graph()
g = GraphOfTowns(1)

g.addTown(0, 1)
g.addTown(1, 1)
g.addTown(2, 100)
g.addTown(3, 1)

graphToDraw.add_node(0, x=0)
graphToDraw.add_node(1, x=1)
graphToDraw.add_node(2, x=2)
graphToDraw.add_node(3, x=3)

g.addRoad(0, 1, 1, 1)
g.addRoad(0, 2, 1, 1)
g.addRoad(2, 3, 1, 1)

graphToDraw.add_edge(0, 1)
graphToDraw.add_edge(0, 2)
graphToDraw.add_edge(2, 3)

g.addNewTownPartnership()
g.addTownToTownPartnership(1, 0)
g.addTownToTownPartnership(2, 0)

nx.draw(graphToDraw, with_labels=True)
plt.show()

dijkstrav2(g, 0, 3)
getShortestPath(g, 0)

# dijkstra(g, 0)
#
# to = g.getTown(1)
# path = [to.getId()]
# shortest(to, path)
# print(path[::-1], to.getDistance())


g = GraphOfTowns(1)
drawing = nx.Graph()

g.addTown('a', 1)
g.addTown('b', 1)
g.addTown('c', 10)  # 100
g.addTown('d', 1)
g.addTown('e', 1000)  # 10
g.addTown('f', 1000)  # 100
g.addTown('g', 1)

drawing.add_node('a', x='a')
drawing.add_node('b', x='b')
drawing.add_node('c', x='c')
drawing.add_node('d', x='d')
drawing.add_node('e', x='e')
drawing.add_node('f', x='f')
drawing.add_node('g', x='g')

g.addRoad('a', 'b', 1, 4)
g.addRoad('a', 'c', 1, 1000)  # 4
g.addRoad('c', 'd', 1, 4)
g.addRoad('b', 'd', 1, 4)
g.addRoad('d', 'e', 1, 4)
g.addRoad('d', 'f', 1, 4)
g.addRoad('f', 'g', 1, 4)
g.addRoad('e', 'g', 1, 4)

drawing.add_edge('a', 'b')
drawing.add_edge('a', 'c')
drawing.add_edge('c', 'd')
drawing.add_edge('b', 'd')
drawing.add_edge('d', 'e')
drawing.add_edge('d', 'f')
drawing.add_edge('f', 'g')
drawing.add_edge('e', 'g')

g.addNewTownPartnership()
g.addTownToTownPartnership('c', 0)
g.addTownToTownPartnership('e', 0)

nx.draw(drawing, with_labels=True)
plt.show()

start = time.time()
dijkstrav2(g, 'a', 'g')
end = time.time()

print(end - start)

getShortestPath(g, 'a')

drawing2 = nx.Graph()
g2 = GraphOfTowns(1)

g2.addTown(0, 1)
g2.addTown(1, 15)
g2.addTown(2, 10)
g2.addTown(3, 1)
g2.addTown(4, 5)
g2.addTown(5, 2000)
g2.addTown(6, 2000)
g2.addTown(7, 5)
g2.addTown(8, 1)
g2.addTown(9, 1000)
g2.addTown(10, 5)
g2.addTown(11, 1000)

drawing2.add_node(0, x=0)
drawing2.add_node(1, x=1)
drawing2.add_node(2, x=2)
drawing2.add_node(3, x=3)
drawing2.add_node(4, x=4)
drawing2.add_node(5, x=5)
drawing2.add_node(6, x=6)
drawing2.add_node(7, x=7)
drawing2.add_node(8, x=8)
drawing2.add_node(9, x=9)
drawing2.add_node(10, x=10)
drawing2.add_node(11, x=11)

g2.addRoad(0, 1, 1, 1)
g2.addRoad(0, 8, 1, 1)
g2.addRoad(0, 9, 1, 1)
g2.addRoad(1, 2, 1, 1)
g2.addRoad(9, 4, 1, 1)
g2.addRoad(2, 10, 1, 1)
g2.addRoad(2, 3, 1, 1)
g2.addRoad(4, 10, 1, 1)
g2.addRoad(3, 4, 1, 1)
g2.addRoad(4, 6, 1, 1)
g2.addRoad(4, 5, 1, 1)
g2.addRoad(6, 7, 1, 1)
g2.addRoad(5, 7, 1, 1)
g2.addRoad(3, 11, 1, 1)
g2.addRoad(11, 7, 1, 1)
g2.addRoad(2, 4, 1, 1)

drawing2.add_edge(0, 1)
drawing2.add_edge(0, 8)
drawing2.add_edge(0, 9)
drawing2.add_edge(1, 2)
drawing2.add_edge(9, 4)
drawing2.add_edge(2, 10)
drawing2.add_edge(2, 3)
drawing2.add_edge(4, 10)
drawing2.add_edge(3, 4)
drawing2.add_edge(4, 6)
drawing2.add_edge(4, 5)
drawing2.add_edge(6, 7)
drawing2.add_edge(5, 7)
drawing2.add_edge(3, 11)
drawing2.add_edge(11, 7)
drawing2.add_edge(2, 4)

g2.addNewTownPartnership()
g2.addNewTownPartnership()
g2.addTownToTownPartnership(8, 0)
g2.addTownToTownPartnership(9, 0)
g2.addTownToTownPartnership(10, 1)
g2.addTownToTownPartnership(11, 1)

nx.draw(drawing2, with_labels=True)
plt.show()

start = time.time()
dijkstrav2(g2, 0, 7)
end = time.time()

print(end - start)
print(getShortestPath(g2, 0))

g3 = GraphOfTowns(1)

g3.addTown(1,1)
g3.addTown(2,1)
g3.addTown(3,1)

g3.addRoad(1,2,1,1)
g3.addRoad(2,3,1,1)

g3.addNewTownPartnership()
g3.addNewTownPartnership()
g3.addNewTownPartnership()
g3.addTownToTownPartnership(1,0)
g3.addTownToTownPartnership(2,1)
g3.addTownToTownPartnership(3,2)

start = time.time()
dijkstrav2(g3, 1, 3)
end = time.time()

print(end - start)
print(getShortestPath(g3, 1))

print(np.random.normal(5,2,2))

gg = generateConnectedGraph(12, 3, 2, 50, 5, 10, 2, 8, 1, 4, 2)

start = time.time()
dijkstrav2(gg, 0, 11)
end = time.time()

print(end - start)
getShortestPath(gg, 0)

# g = generateConnectedGraph(13, 3)
# # start = time.time()
# # findShortestPathUsingBruteForce(g, 4, 9)
# # end = time.time()
# #
# # print(end - start)
# #
# start = time.time()
# dijkstra(g, 4)
# end = time.time()
# #
# print(end - start)
# #
# to = g.getTown(9)
# path = [to.getId()]
# shortest(to, path)
# print(path[::-1], to.getDistance())
