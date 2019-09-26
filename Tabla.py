#MARTINEZ AGUILAR EDGAR RODRIGO
#Fecha de creacion: 25\09\2019

valor=input("Dame un valor entre el 1 y el 9: ")
valor=int(valor)

for i in range(1,11):
    salida="{} x {} = {}"
    print(salida.format(valor,i,i*valor))