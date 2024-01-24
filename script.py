final2 = []
with open('Titanic-Dataset.csv', 'r') as f:  # garante que o arquivo será fechado corretamente quando finalizado
    lines = f.readlines()  # lê todas as linhas do aquivo e armazena na lista 'lines'
    nomes = [linha.split('"') for linha in lines]
    dados = [(nomes[c][0].split(','), [nomes[c][1]], nomes[c][2].split(',')) for c in range(1,len(nomes))]
    final = [c[0] + c[1] +c[2] for c in dados]
for n in final:
    if len(n) == 14 and n[7]!= '':
        lista = [int(n[1]), [int(n[2]), n[6], float(n[7]), int(n[8]), int(n[9]), float(n[11])]]
        if lista[1][1] == 'male': 
            lista[1][1] = 0 # 0 para masculino
        if lista[1][1] == 'female':
            lista[1][1] = 1 #1 para feminino
        final2.append(lista)

print('Survived,Pclass,Sex,Age,SibSp,Parch,Fare')   
for n in final2:
    print(n)


# Survived,Pclass,Sex,Age,SibSp,Parch,Fare,Embarked
# final[n][1] + final[n][2] + final[n][6] + final[n][7] + final[n][8] + final[n][9] + final[n][11]

# [ ("PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked")
# (1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S)
# (2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C)
# (3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S) ]


