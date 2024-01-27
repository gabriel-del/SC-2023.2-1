import sys, os,csv, random
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from knn import *

def separate_data(x):
  data = x[1:].copy()
  random.shuffle(data)
  delimiter = int(len(data) * 0.3)
  test = data[delimiter:]
  train = data[:delimiter]

  id_train = [line[0] for line in train]
  id_test = [line[0] for line in test]
  target_train = [line[1] for line in train]
  target_test = [line[1] for line in test]
  data_train = [line[2:] for line in train]
  data_test = [line[2:] for line in test]
  return [target_train, target_test, data_train, data_test, id_train, id_test]

with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:
    f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
    knn = KNNClass(separate_data(f))
    # print(list(knn.calculate_distances(['0', '0', '0.325', '0.0', '0.0', '0.030022053231939166', '1']))[:10])
    knn.predict()
    knn.accuracy()
