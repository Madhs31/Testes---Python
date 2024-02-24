medias=[]
qtd_alunos=4
b1=eval(input('Digite a primeira nota:'))
b2=eval(input('Digite a segunda nota:'))
for i in range (0, qtd_alunos):
    soma=0
    medias.append((b1+b2/2))
    soma+=(b1+b2)/2

media=soma/qtd_alunos
maior=0
for i in range(0,qtd_alunos):
    if(medias[i]>media):
        maior+=1
print('{} alunos ficaram com média maior que a média da sala'.format(maior))


