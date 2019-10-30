a = int (input("Digite o valor de ‘A’: "))
b = int (input("Digite o valor de ‘B’: "))
resultado = a//b
cont1 = cont2 = 1
for i in range (0, resultado):
      print ("O curso é ", end = "")
      while (cont2 >= 1):
         print ("muito ", end = "")
         cont2 = cont2 - 1
      print ("bom!")
      cont1 +=1
      cont2 = cont1
