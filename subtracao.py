a = int (input("Digite o valor de ‘A’: "))
b = int (input("Digite o valor de ‘B’: "))
primos = a - b
encontrados=0
testando=2
while encontrados < primos:
    testador=1
    conta_div=0
    while testando >= testador:
        if testando%testador == 0:
            conta_div+=1
        testador+=1
    if conta_div == 2:
        print (testando,"",end="")
        encontrados+=1
    testando+=1
print("")
