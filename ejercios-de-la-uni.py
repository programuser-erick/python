#Clase del 17 de agosto

""" 1) Ingresar 2 valores, siendo los mismos la base y la altura de un triangulo
Mostrar la superficie del mismo"""

""" valor1= int(input("Ingrese el primer valor: "))
valor2= int(input("Ingrese el segundo valor: "))

superficie= (valor1*valor2) // 2

print("la superficie de un triangulo es",superficie)
"""

""" 2) Ingresar valores y calcular su promedio
Utilizar una sola variable de ingreso de datos"""

""" #Variables inicializadas en cero
cont,valor=0,0

#Primer valor
valor1= int(input("Ingresar el primer valor: "))
cont= cont + 1
valor= valor + valor1

#Segundo valor
valor2= int(input("Ingresar el segundo valor: "))
cont= cont + 1
valor= valor + valor2

#Tercer valor
valor3= int(input("Ingresar el tercer valor: "))
cont= cont + 1
valor= valor + valor3

#Promedio Total
promedio= valor / cont

print("el promedio total es", promedio)

"""


#Clase del 24 de agosto

""" 1) Ingresar las 2 notas de los parciales
Si el promedio entero es menor a 4, informar recursa
Si el promedio es menor a 7, informar rinde final
Si el promedio es mayor o igual a 7, informar  aprobado"""


""" examen1 = int(input("Ingrese la nota que se saco en el examen: ")) 
examen2 = int(input("Ingrese la nota que se saco en el segundo examen: "))
promedio= (examen1 + examen2) // 2

if promedio <= 3:
    print("El promedio de los dos examenes es",promedio,": Estas desaprobado")
elif promedio <= 6:
    print("El promedio de los dos examenes es",promedio,": Tienes que rendir final")
else:
    print("El promedio de los dos examenes es",promedio,": Estas aprobado")
"""



""" 2) Ingresar un año e informar si es un año bisiesto"""

""" anio= int(input("Ingrese un año deseado: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(anio,"es bisiesto")
else:
    print(anio,"no es bisiesto")

"""

""" 3) Se ingresa por teclado la cantidad, en kilos, de dulce de leche y galletitas y queso crema
Si cada chocotorta insume: 300gr de dulce, 450 gr de galletitas y 150 gr de queso crema, Cuantas chocotortas se pueden hacer con la cantidad ingresada?"""

""" #Pedir al usuario que ingrese los valores
dulce = int(input("Ingrese la cantidad de dulce de leche en kilos: "))
galletitas = int(input("Ingrese la cantidad de galletitas en kilos: "))
queso = int(input("Ingrese la cantidad de queso en kilos: "))

#Convertimos las cantidades a gramos y depues se divide por las cantidades que insume la chocotorta
dulce= dulce*1000 // 300
galletitas=galletitas*1000 // 450
queso=queso*1000 // 150


#Hago las condiciones segun la cantidad mas pequeña para poder hacer las tortas
if dulce < galletitas and dulce < queso:
    print("se puede hacer",dulce,"tortas segun la cantidad de dulce")
elif galletitas < dulce and galletitas < queso:
    print("se puede hacer",galletitas,"tortas segun las galletitas")
else:
    print("se puede hacer",queso,"tortas segun el queso")
"""

""" 4) Se ingresa 3 valores correspondientes a la longitud de los lados de un triangulo 
Se solicita:
a- Verificar que los valores ingresados formen un triangulo
b- Si forman un triangulo, que triangulo es?"""

""" a= int(input("ingrese el primer valor: "))
b= int(input("ingrese el segundo valor: "))
c= int(input("ingrese el tercer valor: "))

#la suma de dos de sus lados siempre tiene que ser mayor al tercero
if a + b > c and a + c > b and c + b > a:
    print("es un triangulo")
    if a == b == c:
        print("es un triangulo equilátero")
    elif a == b or a == c or c == b:
        print("es un triangulo isósceles")
    else:
        print("es un triangulo escaleno")
else:
    print("No es un triangulo")
"""


#Clase del 31 de agosto

""" 1) Mostra los primeros 10 numeros, comenzar desde cero"""

""" numero= 0

while numero <= 10:
    print(numero)
    numero += 1 """


""" 2) Mostra los valores entre 10 y 30 y que sean pares, el contador comienza en cero"""

""" contador = 0

while contador <= 30:
    if contador >= 10:
        if contador % 2 == 0:
            print(contador,end=" ")
    contador += 1
print("fin")

"""
""" contador = 0
numero = 10

while numero <= 30:
    if numero % 2 == 0:
        print(numero)
        contador += 1
    numero += 1 """


""" 3) Arrojar 50 veces un dado, Informar cuantas veces salio el 5"""

#Metodo con el bucle while
""" import random
contador=0
contador_cinco=0

while contador <= 50:
    dado=random.randint(1,6) #simulacion del dado
    if dado == 5:
        contador_cinco +=1
    contador +=1

print("el numero cinco salio",contador_cinco,"veces")
"""
#Metodo con el bucle for
""" import random
contador_cinco = 0 

for _ in range(50):
    dado = random.randint(1,6)
    if dado == 5:
        contador_cinco += 1

print("el numero 5 salio",contador_cinco,"veces")
"""

""" 4) Arrojar la bolilla de ruleta 80 veces, informar cuantas veces salio el valor de la segunda docena (13-24)"""


""" import random
segunda_docena=0
for _ in range(80):
    resultado= random.randint(1,36) # simulamos la ruleta
    if 13 <= resultado <=24:
        segunda_docena += 1

print("salio la segunda docena",segunda_docena,"veces")
"""



""" 5) Generar dos numeros aleatorios, el primero entre 1 y 4 : donde 1-oro, 2-basto, 3-espada, 4-copa.
    El segundo es un numero entre 1 y 12: Informar
    a- Cuantas veces salio el 7 de espadas
    b- Cuantas veces salio el AS de basto
    c- Cuantas veces salio un valor impar
    Realizar 80 tiradas """

""" import random
contador=0
contador_7_espadas= 0
contador_as_basto=0
carta_impar = 0
while contador <= 80:
    palo= random.randint(1,4)
    carta=random.randint(1,12)
    if palo==3 and carta==7:
        contador_7_espadas += 1
    elif palo == 3 and carta == 1:
        contador_as_basto +=1
    elif carta % 2 != 0:
        carta_impar += 1
    contador += 1
    
print(f"Cantidad de veces que salió el 7 de espadas: {contador_7_espadas}")
print(f"Cantidad de veces que salió el AS de basto: {contador_as_basto}")
print(f"Cantidad de veces que salió un valor impar: {carta_impar}") """




""" 6) Generar valores entre 100 y 1000, y sumarlos. Finalizar el proceso cuando la suma supere los 10000 """
""" import random
contador= 0
suma=0
while suma < 10000:
    valores= random.randint(100,1000)
    suma=suma+valores
    contador += 1

print("la suma fue:",suma)
print("se realizaron",contador,"vueltas")
"""

#Clase del 7 de septiembre

""" 1) Sucesion de fibonacci, generar 20 valores de la sucesion"""

""" a,b,cont= 1,1,0
print(a,b,end=" ")
while cont < 20:
    c= a+b
    print(c,end=" ")
    a=b
    b=c
    cont += 1
"""

""" 2) Generar 50 valores aleatorios entre 10 y 30
    Realizar la suma de los valores múltiplos de 4
    Mostrar el resultado en el Programa principal
    Determinar si el nro es multiplo de 4 con una funcion"""

""" import random
cont= 0
suma4=0

def mult4(i):
    if i % 4 == 0:
        return True
    else:
        return False

while cont < 50:
    nro= random.randint(10,30)
    if mult4(nro) == True:
        suma4= suma4+nro
    cont += 1

print("La suma de los números múltiplos de 4 es:", suma4)
"""


""" 3) Generar 50 valores aleatorios entre 10 y 30
    Realizar la suma de los valores primos
    Mostrar el resultado en el Programa principal
    Determinar si el nro es primo con una funcion"""

import random

def nro_primo(i):
    if i <= 1:
        return False
    if i == 2:
        return True
    if i % 2 == 0:
        return False
    
    return True

cont= 0
suma_primo= 0

while cont < 50:
    nro= random.randint(10,30)
    if nro_primo(nro) == True:
        suma_primo = suma_primo + nro
    cont +=1
print("la suma de los valores primos es:",suma_primo)


""" 4) Generar 50 valores aleatorios entre 10 y 30
    Realizar la suma de los numeros deficientes
    Mostrar el resultado en el Programa principal
    Determinar si el nro es deficiente con una funcion"""

""" 5) Generar la sucesion de fibonacci hasta la posicion 30. Mostrar solamente aquellos valores que se encuentren en posiciones impares
Se recuerda que la sucesion comienza con los valores 1 y 1"""

""" 6) Generar 100 nros aleatorios entre 1 y 100
Informar cuantos de ellos son nros oblongos"""

#Clase del 14 de septiembre

""" 1) Ingresar un nro u calcular su factorial"""

""" 2) Partiendo de los valores a= 1 y b=1, obtener la sucesion de fibonacci, hasta la posicion 30
Determinar cuantos valores deficientes hay en la sucesion, a partir de la posicion 4"""

""" 3) Juego:
    Arrojar un dado obteniendo un valor entre 1 y 6
    Con un sumador se simulará el avance o el retroceso
    del jugador. El sumador comienza en cero.
    El juego finaliza cuando se llegue a 100, y el avance será de la siguiente manera: si sale un nro primo, el sumador avanza ese numero.
    El 1 y 2, no se considera primo
    Si sale par, se resta ese numero
    Si sale el uno, no avanza
    Por fin de proceso indicar cuantas veces se arrojo el dado"""

""" 4) Realizar 80 vueltas y generar 
animal= 1-Perro, 2-Gato, 3-Conejo
sexo= 1-macho, 2-hembra
Por fin de proceso, informar
1-Cuantos perros machos fueron atendidos
2-Cuantos conejos fueron atendidos
3-Porcentajes de gatos hembras atendidos
"""

""" 5) Generar 100 valores aleatorios comprendidos entre 20 y 400. De los nros oblongos que surjan, informar cual fue el mayor y el menor valor del lote"""

""" 6) Ingrese una nota válida, entre 1 y 10"""