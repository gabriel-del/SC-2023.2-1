import sys, os,csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from data import *
from knn import *
# Survived,Pclass,Sex,Age,SibSp,Parch,Fare,Embarked

def PclassF(x):
  if x == '3': return 0
  if x == '2': return 0.5
  if x == '1': return 1
def SexF(x):
  if x == 'male': return 0
  if x == 'female': return 1
def AgeF(x, m):
  return float(x) / m
def SibSpF(x, m):
  return float(x) / m
def ParchF(x, m):
  return float(x) / m
def FareF(x, m):
  return float(x) / m
def EmbarkedF(x):
  if x == 'C': return 0
  if x == 'S': return 1
  if x == 'Q': return 2
  # if x == 'Q': return 0.5+(3**(1/2))j



with open(f'{os.path.dirname(__file__)}/../data/Titanic-Dataset.csv', 'r') as f:
  f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
  maxAge, maxSibSp, maxParch, maxFare = 80, 8, 8, 70
  for line in f[1:]:
    if len(line) != len(f[0]):
      raise Exception('Linha com colunas faltando')
    PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked = line
    if Age == '': continue
    newLine = [PassengerId, Survived, PclassF(Pclass), SexF(Sex), AgeF(Age, maxAge), SibSpF(SibSp, maxSibSp), ParchF(Parch, maxParch), FareF(Fare, maxFare), EmbarkedF(Embarked)]
    print(newLine)
