import sys
from src.Mode1 import *

if sys.argv[1] == '-m1':
    inputFile = open(sys.argv[2], 'r')
    outputFile = open(sys.argv[3], 'a')
    mode1(inputFile, outputFile)
elif sys.argv[1] == '-m2':
    print('hehe')
elif sys.argv[1] == '-m3':
    print('eheheh')
else:
    print('Please use available modes: -m1, -m2 or -m3.')
