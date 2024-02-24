def soma(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if (y==0):
        print('O divisor não pode ser zero:')
        return 0
    else:
        return x/y
    
n1=eval(input('Digite um número:'))
n2=eval(input('Digite um número:'))
op=input('Entre com uma operação ('+','-','*','/') ou "S" para sair:')
while (op!='S'): 
    if (op=='+'):
        result=soma(n1,n2)
    elif (op=='-'):
        result=sub(n1,n2)
    elif (op=='*'):
        result=mult(n1,n2)
    elif (op=='/'):
        result=div(n1,n2)
print('O resultado é:', result)