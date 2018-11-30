from src.ConnectedGraphGenerator import generateGraphFromTxt
from src.Algorithms import dijkstrav2, getShortestPath


def mode1(inputTxt, outputTxt):
    inputData = inputTxt.read()
    listOfData = [int(s) for s in inputData.split() if s.isdigit()]

    startingNode = listOfData[0]
    endingNode = listOfData[1]
    graph = generateGraphFromTxt(listOfData)
    dijkstrav2(graph, startingNode, endingNode)
    result = getShortestPath(graph, startingNode)
    outputTxt.write(result)
    print(result)
