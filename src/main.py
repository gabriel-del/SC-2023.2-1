import sys, os,csv
sys.path.append(f'{os.path.dirname(__file__)}/../data')
from data import *
from knn import *

final2 = []
with open(f'{os.path.dirname(__file__)}/../data/Titanic-Dataset.csv', 'r') as f:  # lê e fecha arquivo
    lines = f.readlines()  # lê todas as linhas do arquivo e armazena na lista 'lines'
    nomes = [linha.split('"') for linha in lines] # usa aspas como argumento para separar o nome
    dados = [(nomes[c][0].split(','), [nomes[c][1]], nomes[c][2].split(',')) for c in range(1,len(nomes))] # usa virgula como argumento para separar o restante dos dados
    final = [c[0] + c[1] +c[2] for c in dados] # remove as sublistas
for n in final:
    if len(n) == 14 and n[7]!= '': #descarta as listas incompletas e com dados nulos
        lista = [int(n[1]), [int(n[2]), n[6], float(n[7]), int(n[8]), int(n[9]), float(n[11])]] # monta uma nova lista com os dados essenciais
        if lista[1][1] == 'male':
            lista[1][1] = 0 # 0 para masculino
        if lista[1][1] == 'female':
            lista[1][1] = 1 #1 para feminino
        final2.append(lista) # lista final

print('Survived,Pclass,Sex,Age,SibSp,Parch,Fare')
for n in final2:
    print(n)


# Survived,Pclass,Sex,Age,SibSp,Parch,Fare,Embarked
# final[n][1] + final[n][2] + final[n][6] + final[n][7] + final[n][8] + final[n][9] + final[n][11]
