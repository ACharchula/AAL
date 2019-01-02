import sys
from src.ConnectedGraphGenerator import *
from src.Algorithms import dijkstrav2, getShortestPath
import matplotlib.pyplot as plt
import time

oneHourCost = random.randint(1, 2)
maxTownFee = 50
minTownFee = 5
maxRoadFee = 10
minRoadFee = 2
maxRoadLength = 10
minRoadLength = 1


def theoreticalComplexity(amountOfTowns, amountOfRoads, listOfPartnerships):
    deepCopyComplexity = (1 + amountOfTowns + amountOfRoads)
    numberOfDeepCopy = 0
    partnershipIndex = 1
    for partnership in listOfPartnerships:
        if partnershipIndex == 1:
            numberOfDeepCopy = len(partnership) * partnershipIndex
        else:
            numberOfDeepCopy = (1 + numberOfDeepCopy) * len(partnership) * partnershipIndex

        partnershipIndex += 1

    # print('counted number of deepcopy', numberOfDeepCopy)

    complexity = deepCopyComplexity * numberOfDeepCopy

    return complexity


def compareResultsAndTheory(data):
    result = []
    prev = -1
    amount = 0
    sum = 0
    theoretical = 0

    for record in data:
        if prev == record[0]:
            sum += record[1]
            amount += 1
        else:
            if sum != 0:
                avg = sum/amount
                result.append((prev, avg, theoretical))

            prev = record[0]
            theoretical = record[2]
            sum = record[1]
            amount = 1

    avg = sum / amount
    result.append((prev, avg, theoretical))



    mindex = int(len(result)/2 + 0.5) - 1
    c = result[mindex][1]/result[mindex][2]
    print('  n      t(n)    q(n)')
    for row in result:
        print('%5d %10.2f %4.2f' % (row[0], row[1], row[1]/(c*row[2])))



def mode1(inputTxt, outputTxt):
    inputData = inputTxt.read()
    listOfData = [int(s) for s in inputData.split() if s.isdigit()]

    startingTown = listOfData[0]
    endingTown = listOfData[1]
    graph = generateGraphFromTxt(listOfData)
    dijkstrav2(graph, startingTown, endingTown)
    result = getShortestPath(graph, startingTown)
    outputTxt.write(result + '\n')
    print(result)
    plt.show()


def mode2(amountOfTowns, graphDensity, amountOfPartnerships, maxAmountOfTownsInPartnership, startTown, endTown):
    if amountOfPartnerships == 0:
        minTownsInPartnership = 0
    else:
        minTownsInPartnership = 2

    graph = generateConnectedGraph(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
                                   minRoadFee, maxRoadLength, minRoadLength, maxAmountOfTownsInPartnership,
                                   minTownsInPartnership, graphDensity)
    if graph is None:
        return

    dijkstrav2(graph, startTown, endTown)
    result = getShortestPath(graph, startTown)
    print(result)

    if amountOfTowns < 100:
        plt.show()


def mode3(startingAmountOfTowns, amountOfSteps, sizeOfStep, repetitions):
    amountOfTowns = startingAmountOfTowns
    minimalGraphDensity = 2 / startingAmountOfTowns
    result = []

    if amountOfSteps % 2 == 0:
        print('Please give odd number as amount of steps')
        return

    for i in range(0, amountOfSteps):
        for j in range(0, repetitions):
            graphDensity = 1
            amountOfPartnerships = 2
            maxAmountOfTownsInPartnership = 2
            graph = generateConnectedGraph(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee,
                                           maxRoadFee, minRoadFee, maxRoadLength, minRoadLength,
                                           maxAmountOfTownsInPartnership, 2, graphDensity)

            for townId in range(0, amountOfTowns):
                if graph.getTown(townId).partnershipNumber is None:
                    startTown = townId
                    break

            start = time.time()
            dijkstrav2(graph, startTown, amountOfTowns - 1)
            end = time.time()

            print('Amount of towns: ', amountOfTowns, 'Amount of roads:', graph.amountOfRoads, 'Loop: ', j, 'Result: ',
                  (end - start) * 1000)
            # print(graph.listOfTownPartnerships)
            print(theoreticalComplexity(amountOfTowns, graph.amountOfRoads, graph.listOfTownPartnerships))

            result.append((amountOfTowns, (end-start)*1000, theoreticalComplexity(amountOfTowns, graph.amountOfRoads,
                                                                                  graph.listOfTownPartnerships)))

        amountOfTowns += sizeOfStep

    compareResultsAndTheory(result)


sys.setrecursionlimit(1000000)

if sys.argv[1] == '-m1':
    inputFile = open(sys.argv[2], 'r')
    outputFile = open(sys.argv[3], 'a')
    mode1(inputFile, outputFile)
elif sys.argv[1] == '-m2':
    amountOfTowns = int(sys.argv[2])
    graphDensity = float(sys.argv[3])
    amountOfPartnerships = int(sys.argv[4])
    maxAmountOfTownsInPartnership = int(sys.argv[5])
    startTown = int(sys.argv[6])
    endTown = int(sys.argv[7])
    mode2(amountOfTowns, graphDensity, amountOfPartnerships, maxAmountOfTownsInPartnership, startTown, endTown)
elif sys.argv[1] == '-m3':
    startingAmountOfTowns = int(sys.argv[2])
    amountOfSteps = int(sys.argv[3])
    sizeOfStep = int(sys.argv[4])
    repetitions = int(sys.argv[5])
    mode3(startingAmountOfTowns, amountOfSteps, sizeOfStep, repetitions)
    mode3(startingAmountOfTowns, amountOfSteps, sizeOfStep, repetitions)

else:
    print('Please use available modes: -m1, -m2 or -m3.')
