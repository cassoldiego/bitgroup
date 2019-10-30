# Multiplicando dois números
# Gerando quadrado com o tamanho do produto
 
a=int(input("Informe o primeiro número: "))
b=int(input("Informe o segundo número: "))
tamanho = a*b
for c in range (0, tamanho):
    for i in range (0, tamanho):
        if (i == (tamanho - 1)):
            print ("*")
        else:
            print("* ", end="")
