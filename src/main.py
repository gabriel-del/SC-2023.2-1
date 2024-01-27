import sys, os,csv, random
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from data import *
from knn import *


def separate_data(x):
  data = x[1:].copy()
  random.shuffle(data)
  delimiter = int(len(data) * 0.3)
  train = data[delimiter:]
  test = data[:delimiter]

  id_train = [line[0] for line in train]
  id_test = [line[0] for line in test]
  target_train = [line[1] for line in train]
  target_test = [line[1] for line in test]
  data_train = [line[2:] for line in train]
  data_test = [line[2:] for line in test]
  return [target_train, target_test, data_train, data_test, id_train, id_test]


with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:  # lê e fecha arquivo
    f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
    knn = KNNClass(separate_data(f))
    # knn.print()
    print(knn.data_train)
