# Antoni Charchuła AAL-2-LS podróż

import sys
from src.ConnectedGraphGenerator import *
from src.Algorithms import dijkstra, getShortestPath
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

    dijkstraComplexity = amountOfRoads*math.log10(amountOfTowns)

    complexity = deepCopyComplexity * numberOfDeepCopy + dijkstraComplexity * numberOfDeepCopy + dijkstraComplexity

    return complexity


def compareResultsAndTheory(data, amountOfPartnerships, maxAmountOfTownsInPartnership):
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
    print('=============================')
    print('Amount of Partnerships:', amountOfPartnerships)

    if amountOfPartnerships != 0:
        print('Max amount of towns in partnership :', maxAmountOfTownsInPartnership)

    print('=============================')
    print('  Towns    t(n)    q(n)')
    for row in result:
        print('%5d %10.2f %6.2f' % (row[0], row[1], row[1]/(c*row[2])))



def mode1(inputTxt, outputTxt):
    inputData = inputTxt.read()
    listOfData = [int(s) for s in inputData.split() if s.isdigit()]

    startingTown = listOfData[0]
    endingTown = listOfData[1]
    graph = generateGraphFromTxt(listOfData)
    dijkstra(graph, startingTown, endingTown)
    results = getShortestPath(graph, startingTown)

    for result in results:
        outputTxt.write(result + '\n')
        print(result)

    plt.show()


def mode2(amountOfTowns, graphDensity, amountOfPartnerships, maxAmountOfTownsInPartnership, startTown, endTown):
    if amountOfPartnerships == 0:
        minTownsInPartnership = 0
    else:
        minTownsInPartnership = 1

    if amountOfTowns < 100:
        graph = generateConnectedGraph(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
                                   minRoadFee, maxRoadLength, minRoadLength, maxAmountOfTownsInPartnership,
                                   minTownsInPartnership, graphDensity)
    else:
        graph = generateConnectedGraphWithoutDrawing(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee, maxRoadFee,
                                   minRoadFee, maxRoadLength, minRoadLength, maxAmountOfTownsInPartnership,
                                   minTownsInPartnership, graphDensity)
    if graph is None:
        return

    dijkstra(graph, startTown, endTown)
    results = getShortestPath(graph, startTown)

    for result in results:
        print(result)

    if amountOfTowns < 100:
        plt.show()


def mode3(startingAmountOfTowns, startingAmountOfPartnerships, startingAmountOfTownsInPartnerships,
          amountOfSteps, sizeOfStep, repetitions, maxAmountOfPartnerships, maxAmountOfTownsInPartnership):

    if amountOfSteps % 2 == 0:
        print('Please give an odd number as amount of steps')
        return

    graphDensity = 1

    for amountOfPartnerships in range(startingAmountOfPartnerships, maxAmountOfPartnerships + 1):
        for amountOfTownsInPartnership in range(startingAmountOfTownsInPartnerships, maxAmountOfTownsInPartnership + 1):

            if amountOfPartnerships != 0 and amountOfTownsInPartnership == 0:
                continue

            amountOfTowns = startingAmountOfTowns
            result = []

            for i in range(0, amountOfSteps):
                for j in range(0, repetitions):

                    graph = generateConnectedGraphWithoutDrawing(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee,
                                           maxRoadFee, minRoadFee, maxRoadLength, minRoadLength,
                                           amountOfTownsInPartnership, amountOfTownsInPartnership, graphDensity)

                    for townId in range(0, amountOfTowns):
                        if graph.getTown(townId).partnershipNumber is None:
                            startTown = townId
                            break

                    start = time.time()
                    dijkstra(graph, startTown, amountOfTowns - 1)
                    end = time.time()

                    print('Amount of towns: ', amountOfTowns, 'Loop: ', j, 'Result: ', (end - start) * 1000)

                    result.append((amountOfTowns, (end-start)*1000, theoreticalComplexity(
                        amountOfTowns, graph.amountOfRoads, graph.listOfTownPartnerships)))

                amountOfTowns += sizeOfStep

            compareResultsAndTheory(result, amountOfPartnerships, amountOfTownsInPartnership)

            if amountOfPartnerships == 0:
                break

def warmUp():
    graphDensity = 1

    print('===Machine warm up started===')

    for amountOfPartnerships in range(1,3):
        for amountOfTownsInPartnership in range(1, 3):

            amountOfTowns = 50

            for i in range(0, 10):
                for j in range(0, 10):

                    graph = generateConnectedGraphWithoutDrawing(amountOfTowns, amountOfPartnerships, oneHourCost, maxTownFee, minTownFee,
                                           maxRoadFee, minRoadFee, maxRoadLength, minRoadLength,
                                           amountOfTownsInPartnership, amountOfTownsInPartnership, graphDensity)

                    for townId in range(0, amountOfTowns):
                        if graph.getTown(townId).partnershipNumber is None:
                            startTown = townId
                            break

                    dijkstra(graph, startTown, amountOfTowns - 1)

    print('===Machine warm up ended===')

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

    if graphDensity < 2/amountOfTowns:
        print("Error - please insert graph denisty bigger or equal than 2/amountOfTowns!")
    else:
        mode2(amountOfTowns, graphDensity, amountOfPartnerships, maxAmountOfTownsInPartnership, startTown, endTown)
elif sys.argv[1] == '-m3':
    startingAmountOfTowns = int(sys.argv[2])
    startingAmountOfPartnerships = int(sys.argv[3])
    startingAmountOfTownsInPartnerships = int(sys.argv[4])
    amountOfSteps = int(sys.argv[5])
    sizeOfStep = int(sys.argv[6])
    repetitions = int(sys.argv[7])
    maxAmountOfPartnerships = int(sys.argv[8])
    maxAmountOfTownsInPartnership = int(sys.argv[9])

    warmUp()
    mode3(startingAmountOfTowns, startingAmountOfPartnerships, startingAmountOfTownsInPartnerships,
          amountOfSteps, sizeOfStep, repetitions, maxAmountOfPartnerships, maxAmountOfTownsInPartnership)

else:
    print('Please use available modes: -m1, -m2 or -m3. Read Readme if you need more help')