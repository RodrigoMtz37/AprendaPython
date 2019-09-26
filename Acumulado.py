#MARTINEZ AGUILAR EDGAR RODRIGO
#Fecha de creacion: 25\09\2019

acum=int(0)
valor=str("")

while True:
    numero=input("Dame un valor entero: ")
    if valor=="":
        print("Vacio. Salida del programa.")
        break
    else:
        acum+=int(valor)
        salida="Monto acumulado: {}"
        print(salida.format(acum))