name_list =[]
n = 0
q = eval(input('Quantos nomes deseja inserir:'))
while n < q:
    name = input('Digite um nome:')
    name_list.append(name)
    n += 1
print(name_list)
sumvog = 0
sumcons = 0
for name in name_list:
    qvogal = 0
    qcons = 0
    for c in name:
       if c in 'AEIOUaeiouãâôêáé':
            qvogal += 1
       elif c in'':
            qvogal += 0 
            qcons += 0 
    else:
            qcons +=1
    sumvog += qvogal
    sumcons += qcons
print('Quantidade de vogais:',sumvog,'Quantidade de consoantes:',sumcons,'Total de letras:',sumvog+sumcons)