import sys, os,csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from data import *
from knn import *

def PclassF(x):
  if x == '3': return '0'
  if x == '2': return '0.5'
  if x == '1': return '1'
def SexF(x):
  if x == 'male': return '0'
  if x == 'female': return '1'
def AgeF(x, m):
  return str(float(x) / m)
def SibSpF(x, m):
  return str(float(x) / m)
def ParchF(x, m):
  return str(float(x) / m)
def FareF(x, m):
  return str(float(x) / m)
def EmbarkedF(x):
  if x == 'C': return '0'
  if x == 'S': return '1'
  if x == 'Q': return complex(0.5,3**(1/2)/2)
  # if x == 'Q': return '2'
def toInt(x):
  try: return int(x)
  except: return 0

newFile = []
with open(f'{os.path.dirname(__file__)}/../data/Titanic-Dataset.csv', 'r') as f:
  f = list(csv.reader(f, delimiter=',', lineterminator='\n'))
  maxAge = max([toInt(line[f[0].index('Age')]) for line in f[1:]])
  maxSibSp = max([toInt(line[f[0].index('SibSp')]) for line in f[1:]])
  maxParch = max([toInt(line[f[0].index('Parch')]) for line in f[1:]])
  maxFare = max([toInt(line[f[0].index('Fare')]) for line in f[1:]])
  for line in f[1:]:
    if len(line) != len(f[0]):
      raise Exception('Linha com colunas faltando')
    PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked = line
    if Age == '' or Embarked == '': continue
    newLine = [PassengerId, Survived, PclassF(Pclass), SexF(Sex), AgeF(Age, maxAge),
    SibSpF(SibSp, maxSibSp), ParchF(Parch, maxParch), FareF(Fare, maxFare), EmbarkedF(Embarked)]
    newFile.append(newLine)

with open(f'{os.path.dirname(__file__)}/../data/Titanic-Processed.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['PassengerId','Survived','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked'])
  for line in newFile:
    writer.writerow(line)
