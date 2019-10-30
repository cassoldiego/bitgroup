a=int(input("Informe o primeiro número: "))
b=int(input("Informe o segundo número: "))
numero = a+b
if numero > 1:
    for i in range (2, numero):
        if (numero % i) == 0:
            print ("O número",numero,"não é primo.")
            break
    if (i == (numero - 1)):
        print ("O número",numero,"é primo.")
else:
    print ("O número",numero,"não é primo.")
