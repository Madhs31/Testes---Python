lst=[] #abre uma lista vazia
for i in range(5): #para i repetir 5 vezes (basicamente)
    lst.append([]) #e já manda adicionar as vezes na lista vazia
    for j in range(5): #agr chegou a vez do j
        if (i==j): #se i for igual a j faça
            lst[i].append(0)  #na linha adicione 0 na lista
        else: #se não
            lst[i].append(1) #adicione 1

for line in lst: #para linha em lista
    print(line) #mostre