class KNNClass():
  def __init__(self, k=3):
    self.k = k

  def fit(self, x, y):
    self.X_train = x
    self.y_train = y


  def _euclides(self, p, Q):
    distances = []
    for q in Q:
      d = [(x_p - x_q)**2 for x_p, x_q in zip(p,q)]
      d_sum = sum(d)
      d_final = d_sum**0.5
      distances.append(d_final)

    return distances

  def _most_common(self, lst):
    return max(set(lst), key=lst.count)

  def predict(self, X_test):
    vizinhos = []
    for p in X_test:
      distancias = self._euclides(p, self.X_train)
      y_sorted = [y for _, y in sorted(zip(distancias, self.y_train))]
      vizinhos.append(y_sorted[:self.k])

    knn_viz = list(map(self._most_common, vizinhos))
    self.y_pred = knn_viz
    return knn_viz

  def accuracy(self, y_test):
    count = 0
    for i in range(0, len(y_test)):
      if self.y_pred[i] == y_test[i]:
        count+=1

    accuracy = count / len(y_test)
    return accuracy
