with open('Titanic-Dataset.csv', 'r') as f:  # garante que o arquivo será fechado corretamente quando finalizado
    lines = f.readlines()  # lê todas as linhas do aquivo e armazena na lista 'lines'
    nomes = [linha.split('"') for linha in lines]
    dados = [(nomes[c][0].split(','), [nomes[c][1]], nomes[c][2].split(',')) for c in range(1,len(nomes))]
    final = [c[0] + c[1] +c[2] for c in dados]

for line in final:
  print(line)
