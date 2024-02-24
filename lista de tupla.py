n=eval(input('Entre com um número(-1 para sair):'))
lst=[]
while (n!=-1):
    lst.append(n)
    n=eval(input('ENtre com um número:'))
print('Sua lista é:',lst)
lst_resp=[]
for i in range (len(lst)):
    t1=(lst[i].pow(lst[1], 3))
    lst_resp.append(t1)
print(t1)

