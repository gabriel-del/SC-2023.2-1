import sys, os,csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from data import *
from knn import *


with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:  # lê e fecha arquivo
