import sys, os,csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')

def average(category):
  return sum([float(line[f[0].index(category)]) for line in Survived_1]) / len(Survived_1)

with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:
  f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
  Survived_1 = list(filter(lambda x: x[1] == '1', f))

  print(f"Pclass: {average('Pclass')}")
  print(f"Sex: {average('Sex')}")
  print(f"Age: {average('Age')}")
  print(f"SibSp: {average('SibSp')}")
  print(f"Parch: {average('Parch')}")
  print(f"Fare: {average('Fare')}")
  # print(f"Embarked: {average('Embarked')}")
