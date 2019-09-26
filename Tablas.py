#MARTINEZ AGUILAR EDGAR RODRIGO
#Fecha de creacion: 25\09\2019

for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    print()
    for j in range(1,11):
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else: 
        print()