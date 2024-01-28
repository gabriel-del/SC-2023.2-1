import sys, os, csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from knn import *

accuracies = []
with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:
    f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
    for _ in range(100):
        knn = KNNClass(f)
        # print(list(knn.calculate_distances(['0', '0', '0.325', '0.0', '0.0', '0.030022053231939166', '1']))[:10])
        knn.predict()
        accuracy = knn.accuracy()
        # print(accuracy)
        accuracies.append(accuracy)

print('\nAcurácias: ')
print(f'Média: {sum(accuracies) / len(accuracies)}, máxima: {max(accuracies)}, mínima: {min(accuracies)}')
