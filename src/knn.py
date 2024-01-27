import random

class KNNClass():
  def __init__(self, f, k=5):
    data = f[1:].copy()
    random.shuffle(data)
    delimiter = int(len(data) * 0.3)
    test = data[:delimiter]
    train = data[delimiter:]
    self.target_train = [line[1] for line in train]
    self.target_test = [line[1] for line in test]
    self.data_train = [line[2:] for line in train]
    self.data_test = [line[2:] for line in test]
    self.id_train = [line[0] for line in train]
    self.id_test = [line[0] for line in test]
    self.target_test_guessed = []
    self.k = k

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
    return right_guess.count(True)/len(right_guess)
