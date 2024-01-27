import sys, os,csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from data import *
from knn import *


with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:  # lê e fecha arquivo
    f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
    # knn = KNNClass(f)
    id = [line[0] for line in f[1:]]
    target = [line[1] for line in f[1:]]
    data = [line[2:] for line in f[1:]]
    print(data)
