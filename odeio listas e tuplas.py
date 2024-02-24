lst=[]
st1=('O Poderoso Chefão','1972','Francis','US$6 milhões')
lst.append(st1)
resp=''
while (resp!='N'):
    title=input('Entre com o título do filme:')
    ano=eval(input('Entre com o ano de lançamento:'))
    diretor=input('Entre com o diretor do filme:')
    orcamento=input('Entre com o orçamento do fime:')
    tup=(title,ano,diretor,orcamento)
    lst.append(tup)
    print=(str(tup[0]))+'-'+str(ano)+'adicionado;'
    rep=input('Deseja adicionar outro filme(S/N)?')
print=('Lista completa:',lst)
lst.pop(0)
print('Nova lista',lst)



