from src.Graph import *
import random
import networkx as nx
import matplotlib.pyplot as plt


def generateNumberOfEdges(amountOfVertices):
    maxAmount = amountOfVertices * (amountOfVertices - 1) / 2  # complete graph
    minAmount = amountOfVertices - 1

    return random.randint(minAmount, maxAmount)


def generateConnectedGraph(amountOfVertices, amountOfPartnerships):
    drawing = nx.Graph()
    graph = GraphOfTowns(random.randint(1, 4))  # !!! rethink costs

    amountOfEdges = generateNumberOfEdges(amountOfVertices)

    graph.addTown(0, random.randint(1, 30))
    drawing.add_node(0, x=0)

    for x in range(1, amountOfVertices):
        graph.addTown(x, random.randint(1, 30))  # return?
        secondNode = random.randint(0, x - 1)
        graph.addRoad(x, secondNode, random.randint(1, 10), random.randint(1, 4))
        amountOfEdges -= 1

        drawing.add_node(x, x=x)
        drawing.add_edge(x, secondNode)

    if amountOfEdges != 0:
        for x in range(0, amountOfEdges):

            while 1:
                frm = random.randint(0, amountOfVertices - 1)
                to = random.randint(0, amountOfVertices - 1)

                if graph.checkIfRoadExists(frm, to):
                    continue
                else:
                    graph.addRoad(frm, to, random.randint(1, 10), random.randint(1, 4))
                    drawing.add_edge(frm,to)
                    break

    for x in range(0, amountOfPartnerships):
        graph.addNewTownPartnership()

    for x in graph.getPartnerships():
        loops = random.randint(2, 4)
        for y in range(0, loops):
            while 1:
                town = random.randint(0, amountOfVertices - 1)

                if town in x:
                    continue
                else:
                    x.append(town)
                    break

    nx.draw(drawing, with_labels=True)
    plt.show()

    return graph
