n1=eval(input('Digite o primeiro valor:'))
n2=eval(input('Digite o segundo valor:'))
op=input('Digite a operação(+,-,*,/):')
if (op=='+'):
    res=n1+n2
elif (op=="-"):
    res=n1-n2
elif (op=="*"):
    res=n1*n2
else:
    if (op=="/"):
        if (n2==0):
            n2=eval(input("Digite um número diferente de 0:"))
            res=n1/n2
print("o resultado é:", res)
            