import sys, os, csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from knn import *


with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:
    f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
    knn = KNNClass(f)
    # print(list(knn.calculate_distances(['0', '0', '0.325', '0.0', '0.0', '0.030022053231939166', '1']))[:10])
    knn.predict()
    knn.accuracy()
