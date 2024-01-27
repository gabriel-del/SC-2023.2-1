class KNNClass():
  def __init__(self, data, k=3):
    self.k = k
    self.target_train = data[0]
    self.target_test = data[1]
    self.data_train = data[2]
    self.data_test = data[3]
    self.id_train = data[4]
    self.id_test = data[5]
    self.target_test_guessed = []

  def predict(self):
    for p in self.data_train:
      vizinhos = []
      distancias = self.calculate_distances(p)
      target_list = [target for _, target in sorted(zip(distancias, self.target_train))]
      vizinhos.append(target_list[:self.k])
    self.target_test_guessed.append(max(vizinhos, key=vizinhos.count))

  def calculate_distances(self, x):
    distances = []
    for y in self.data_train:
      d = [abs(x_n - y_n)**2 for x_n, y_n in zip(float(x),float(y))]
      distances.append(sum(d) ** 0.5)
    return distances

  def accuracy(self, y_test):
    count = 0
    for i in range(0, len(y_test)):
      if self.y_pred[i] == y_test[i]:
        count+=1
    accuracy = count / len(y_test)
    return accuracy

