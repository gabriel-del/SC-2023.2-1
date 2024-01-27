import sys, os,csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')

def average(category, table):
  return sum([float(line[f[0].index(category)]) for line in table]) / len(table)

with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'r') as f:
  f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
  Survived_1 = list(filter(lambda x: x[1] == '1', f))

  print(f"Pclass: {average('Pclass', Survived_1)}")
  print(f"Sex: {average('Sex', Survived_1)}")
  print(f"Age: {average('Age', Survived_1)}")
  print(f"SibSp: {average('SibSp', Survived_1)}")
  print(f"Parch: {average('Parch', Survived_1)}")
  print(f"Fare: {average('Fare', Survived_1)}")
  # print(f"Embarked: {average('Embarked', Survived_1)}")
