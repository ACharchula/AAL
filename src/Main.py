from src.Graph import *
from src.Algorithms import *
from src.ConnectedGraphGenerator import *
import time
import networkx as nx
import matplotlib.pyplot as plt

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
g.addRoad(0,2,1,1)
g.addRoad(2,3,1,1)

graphToDraw.add_edge(0,1)
graphToDraw.add_edge(0,2)
graphToDraw.add_edge(2,3)

g.addNewTownPartnership()
g.addTownToTownPartnership(1,0)
g.addTownToTownPartnership(2,0)

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


# g = GraphOfTowns(1)
#
# g.addTown('a', 1)
# g.addTown('b', 1)
# g.addTown('c', 100)
# g.addTown('d', 1)
# g.addTown('e', 10)
# g.addTown('f', 100)
# g.addTown('g', 1)
#
# g.addRoad('a', 'b', 1, 4)
# g.addRoad('a', 'c', 1, 4)
# g.addRoad('c', 'd', 1, 4)
# g.addRoad('b', 'd', 1, 4)
# g.addRoad('d', 'e', 1, 4)
# g.addRoad('d', 'f', 1, 4)
# g.addRoad('f', 'g', 1, 4)
# g.addRoad('e', 'g', 1, 4)
#
# g.addNewTownPartnership()
# g.addTownToTownPartnership('c', 0)
# g.addTownToTownPartnership('e', 0)

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

