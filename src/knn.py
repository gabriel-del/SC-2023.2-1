

class KNNClass():
  def __init__(self, data, k=5):
    self.k = k
    self.target_train = data[0]
    self.target_test = data[1]
    self.data_train = data[2]
    self.data_test = data[3]
    self.id_train = data[4]
    self.id_test = data[5]
    self.target_test_guessed = []

  def calculate_distances(self, x):
    distances = []
    for y in self.data_train:
      d = [(abs(complex(x_n) - complex(y_n)))**2 for x_n, y_n in zip(x,y)]
      distances.append(sum(d) ** 0.5)
    return sorted(zip(distances, self.id_train, self.target_train))

  def predict(self):
    for p in self.data_test:
      target_list = [target for _, _,target in self.calculate_distances(p)]
      vizinhos = target_list[:self.k]
      self.target_test_guessed.append(max(set(vizinhos), key = vizinhos.count))
    return self.target_test_guessed

  def accuracy(self):
    right_guess = [ x == y for x, y in zip(self.target_test_guessed, self.target_test)]
    result = right_guess.count(True)/len(right_guess)
    print(result)
    return result
