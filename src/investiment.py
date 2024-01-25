def list_train_test(data):
  import random
  data_test = data.copy()
  random.shuffle(data_test)

  test_size = int(len(data_test) * 0.3)

  test_total = data_test[(len(data_test) - test_size):]
  test_total.sort(key=lambda x:x[0])
  X_test = [cart[1] for cart in test_total]
  y_test = [cart[0] for cart in test_total]

  train_total = data_test[:(len(data_test) - test_size)]
  train_total.sort(key=lambda x:x[0])
  X_train = [cart[1] for cart in train_total]
  y_train = [cart[0] for cart in train_total]

  return X_train, X_test, y_train, y_test

print(1)
import sys
sys.path.append('../data')
from data import *
# fib(8)
print(data)


# no_class_features = [cart[2] for cart in no_class]
# data_correct = [(cart[1], cart[2]) for cart in data]

# X_train, X_test, y_train, y_test = list_train_test(data_correct)

# knn = KNNClass()
# knn.fit(X_train, y_train)

# knn.predict(X_test) # check output

# knn.accuracy(y_test)

# definindo_noClass = knn.predict(no_class_features)

# data_previsto = no_class.copy()

# for i in range(len(definindo_noClass)):
#     data_previsto[i][1] = definindo_noClass[i]
#     print(data_previsto[i])
