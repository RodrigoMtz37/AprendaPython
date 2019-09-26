#MARTINEZ AGUILAR EDGAR RODRIGO
#Fecha de creacion: 25\09\2019

valor1=input("Valor 1:")
valor2=input("Valor 2:")
salida="Valores proporcionados: {} y {}. {}."

if (valor1==valor2):
    print(salida.format(valor1,valor2,"Los valores son iguales"))
else:
    if valor1>valor2:
        print(salida.format(valor1,valor2,"El valor mayor es el primero"))
    else:
        print(salida.format(valor1,valor2,"El valor mayor es el segundo"))