file1=input('Nome do primeiro arquivo')
file2=input('Nome do segundo arquivo')

arq1=open(file1,'r')
arq2=open(file2,'r')
arq3=open('file3.txt','w+')

arq3.write(arq1.read())
arq3.write(arq2.read())

print(arq3.read())

arq1.close()
arq2.close()
arq3.close()
