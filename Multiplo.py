#MARTINEZ AGUILAR EDGAR RODRIGO
#Fecha de creacion: 25\09\2019

numero=int(input("Dame un numero entero: "))

esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)

if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")