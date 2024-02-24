import random
lim=eval(input('limite superior:'))
x= random.randrange(0,lim)
n=eval(input('Digite um número:'))
while (n!=x):
    if (n>x):
        print('muito alto')
    while (n==x):
        print('acertou')
    else:
        print('muito baixo')
