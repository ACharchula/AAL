# Projekt z przedmiotu AAL (Analiza Algorytmów)

### Author

Antoni Charchuła (283713) 

### Problem 

AAL-2-LS podróż
Dane są miasta połączone siecią dróg. Dla każdej drogi znany jest czas przejazdu w godzinach. Wjazd do każdego miasta oraz na kazdą drogę jest płatny (koszt ustalony oddzielnie dla każdego miasta i drogi). Miasta mogą należeć do grup partnerskich (maksymalnie do jednego partnerstwa) - wjazd do takiego miasta zwalnia z opłat za wjazd do pozostałych miast partnerskich. Każda godzina podróży ma ustalony koszt (niezależny od drogi). Należy znaleźć najtańszą opcję podróży pomiędzy dwoma wyróżnionymi miastami.

Aplication running modes
---
### Mode 1
```
python3 PathFinder.py -m1 (input).txt (output).txt
```
In input.txt put your graph in given pattern:
>**in the first line:** (start node) (end node) (amount of towns) (amount of roads) (cost of one hour trip) (amount of partnerships) (amount of towns in partnerships)

>**next (amount of towns) lines:** (town id) (town fee)

>**next (amount of roads) lines:** (town id) (next town id) (road enter fee) (hours of driving)

>**next (amount of towns in partnerships) lines:** (town id) (partnership number)

Example:
```
0 1 4 4 1 1 2
0 10
1 6
2 10
3 1000
0 1 100 3
0 2 10 1
2 3 10 1
3 1 70 1
2 0 
3 0
```
This mode will find shortest path in given graph of towns, display result in console and save it to output.txt Additionally it will display the graph.
### Mode 2
```
python3 PathFinder.py -m2 (amount of Towns) (graph density) (amount of partnerships) (max amount of towns in partnerships) (start town) (end town)
```
This mode will generate random graph with given parameters. If amount of towns is less than 100, program will display the graph.

### Mode 3
```
python3 PathFinder.py -m3 (starting amount of towns) (starting amount of partnerships) (starting amount of towns in partnerships) (amount of steps) (size of step) (repetitions) (max amount of partnerships) (max amount of towns in partnership)
```
This mode will perform tests of theoretical complexity. It generates results in console. 

Data structure , algorithms and files
---
### Data structure - Graph.py
graph - class **GraphOfTowns**
vertex - class **Town**
edges - class **Road**

Towns are stored in dictionary in GraphOfTowns. Every town contains list of roads. And every road contains two ids of towns, which it connect. 

### Algorithms
**Graph generation** - class ConnectedGraphGenerator. Iteration in range(0, amountOfTowns) and adds town to random town in graph. If there will be roads to add, it searches two random towns which are not connected and adds a road.

**Shortest path finding** - class Algorithms. Algorithm based on dijkstra algorithm with heap (in projected heapq was used). One big modifiation is changing the graph when town which belongs to partnership is reached. In this situation, algorithm creates copy of original graph using deepCopy (the biggest impact on complexity of the algorithm), replaces the the town with the reached one. Adds additional roads to reached town from the copied town. And changes fees of specific towns in partnerships in copied graph. Also it saves in towns data which partnerships has been already connected.

This modification let us find shortest path in dynamic changing graph. Also it lets coming back to previously visited towns, which is sometimes needed. 

### Files

**PathFinder** - "main" of the program, it contains modes and functions which calculate theoretical complexity

**Graph** - contains data structure

**ConnectedGraphGenerator** - contains functions which generates graph. There is function with drawing generation and without it, because drawing generations slows the program.

**Algorithms** - contains algorithms connected with shortest path finding and displaying the result.

Additional information
---
> - In order to display graphs you need to have numpy installed.
> - In mode 3 it is not recommended to run test for bigger amount of towns than 150 - tests are really slow beacuse of graphDensity = 1.
