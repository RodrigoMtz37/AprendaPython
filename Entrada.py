#MARTINEZ AGUILAR EDGAR RODRIGO
#Fecha de creacion: 25\09\2019

entrada=input()
print(type(entrada))

esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):

    print("Dato entero, ¡Muy bien!")
else:
    print("No es entero. Intenta de nuevo.")