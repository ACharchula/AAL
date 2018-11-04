from src.Graph import *
from src.Algorithms import *
from src.ConnectedGraphGenerator import *
import time

g = GraphOfTowns(1)

g.addTown('a', 1)
g.addTown('b', 1)
g.addTown('c', 100)
g.addTown('d', 1)
g.addTown('e', 10)
g.addTown('f', 100)
g.addTown('g', 1)

g.addRoad('a', 'b', 1, 4)
g.addRoad('a', 'c', 1, 4)
g.addRoad('c', 'd', 1, 4)
g.addRoad('b', 'd', 1, 4)
g.addRoad('d', 'e', 1, 4)
g.addRoad('d', 'f', 1, 4)
g.addRoad('f', 'g', 1, 4)
g.addRoad('e', 'g', 1, 4)

g.addNewTownPartnership()
g.addTownToTownPartnership('c', 0)
g.addTownToTownPartnership('e', 0)

#start = time.time()
#findShortestPathUsingBruteForce(g, 'a', 'g')
#end = time.time()

#print(end - start)

#start = time.time()
#dijkstra(g, 'a', 'g')
#end = time.time()

#print(end - start)

#to = g.getTown('g')
#path = [to.getId()]
#shortest(to, path)
#print(path[::-1])

g = generateConnectedGraph(13, 3)
start = time.time()
findShortestPathUsingBruteForce(g, 4, 9)
end = time.time()

print(end - start)

start = time.time()
dijkstra(g, 4, 9)
end = time.time()

print(end - start)

to = g.getTown(9)
path = [to.getId()]
shortest(to, path)
print(path[::-1], to.getDistance())

