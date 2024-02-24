idade=eval(input('idades(digite uma idade negativa para sair):'))
total=0
while idade>0:
    if total==0:
        maior,menor=idade,idade
    else:
        if(idade>maior):
            maior=idade
        if(idade<menor):
            menor=idade
    total+=1

media=(maior+menor)/2
print('A média é: {}'.format(media))
