"""Mayor o menor: Escribe un programa que solicite al usuario dos números y luego determine cuál de los dos números es mayor."""

#solicitar valores al usuario
valor1= int(input("porfavor ingrese el primer valor: "))
valor2= int(input("porfavor ingrese el segundo valor: "))

#verificar si los valores son negativos
if valor1<0 or valor2<0:
    print("no se puede ingresar valores negativos")
else:
    #comparacion de valores
    if valor1 > valor2:
        print(f"{valor1} es mayor que {valor2}")
    elif valor1 == valor2:
        print(f"{valor1} es igual a {valor2}")
    else:
        print(f"{valor1} es menor a {valor2}")
