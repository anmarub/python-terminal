import os

# Crear matriz de 4 X 4, y llenarlas por teclado con números enteros.

matriz = []
f1 = []
f2 = []
f3 = []
f4 = []

x = 0
y = 0
z = 0
w = 0

def inicio():
    print('~' * 25, ' Ejercicios con Matrices ', '~' * 25)

def clear():
    os.system('clear')

def continuar_opcion():
    print('=' * 60)
    print('')
    input('Presion ◄◄ Enter ╝ ►► para continuar')

while x < 4:
    try:
        inicio()
        dato = int(input('Digite los numeros de la matriz 1: '), )
        x += 1
        f1.append(dato)
        clear()
    except:
        print('El Caracter ingresado no es un numero entero')
while y < 4:
    try:
        inicio()
        dato = int(input('Digite los numeros de la matriz 2: '), )
        y += 1
        f2.append(dato)
        clear()
    except:
        print('El Caracter ingresado no es un numero entero')
while z < 4:
    try:
        inicio()
        dato = int(input('Digite los numeros de la matriz 3: '), )
        z += 1
        f3.append(dato)
        clear()
    except:
        print('El Caracter ingresado no es un numero entero')
while w < 4:
    try:
        inicio()
        dato = int(input('Digite los numeros de la matriz 4: '), )
        w += 1
        f4.append(dato)
        clear()
    except:
        print('El Caracter ingresado no es un numero entero')

matriz.append(f1)
matriz.append(f2)
matriz.append(f3)
matriz.append(f4)

# 1. Imprimir en forma de matriz
inicio()
print('=' * 25, 'Punto #1', '=' * 25)
for r in range(len(matriz)):
    for c in range(len(matriz)):
        print(matriz[r][c], end='\t')
    print() # Salto de linea en la terminal

continuar_opcion()
clear()
# 2. sumar diagonal derecha
inicio()
sumaDer = 0
c = 3 # declaramos constante para hallar la columna

print('=' * 25, 'Punto #2', '=' * 25)
for r in range(len(matriz)):
    matriz[r][c-r]
    sumaDer = sumaDer + matriz[r][c-r]
print('La suma de la Diagonal Derecha es ►►► ',sumaDer)

continuar_opcion()
clear()
# 3. sumar diagonal izquierda
inicio()
sumaIzq = 0

print('=' * 25, 'Punto #3', '=' * 25)
for r in range(len(matriz)):
    x = matriz[r][r]
    sumaIzq = sumaIzq + x
print('La suma de la Diagonal Izquierda es ►►► ',sumaIzq)

continuar_opcion()
clear()
# 4. sumar bordes
inicio()
sumaBordes = 0

print('=' * 25, 'Punto #4', '=' * 25)
for a in range(len(matriz)):
    x = matriz[0*a][a]
    sumaBordes = sumaBordes + x

for b in range(len(matriz)):
    x = matriz[b][0*b]
    sumaBordes = sumaBordes + x

for c in range(len(matriz)):
    x = matriz[c][(3+c)-c]
    sumaBordes = sumaBordes + x

for d in range(len(matriz)):
    x = matriz[(3+d)-d][d]
    sumaBordes = sumaBordes + x

print('La suma de los 4 border es ►►► ',sumaBordes)
continuar_opcion()
clear()
# 5. decir cuantos números son pares
print('=' * 25, 'Punto #5', '=' * 25)
pares = []

for x in range(len(matriz)):
    for y in range(len(matriz)):
        z = matriz[x][y]
        if (z % 2) == 0:
            pares.append(z)
print('La cantidad de numeros Impares en la matriz son ►►► ',len(pares))
continuar_opcion()
clear()
# 6. decir cuantos números son impares
print('=' * 25, 'Punto #6', '=' * 25)
Impares = []

for x in range(len(matriz)):
    for y in range(len(matriz)):
        z = matriz[x][y]
        if (z % 3) == 0:
            Impares.append(z)
print('La cantidad de numeros Impares en la matriz son ►►► ',len(Impares))
continuar_opcion()
clear()
# 7. crear una segunda matriz, y llenar sus elementos con la multiplicación de cada elemento,
# por el numero pedido por teclado

#Ciclo para ejecutar la multiplicacion de cada elemento de la matriz (Listas de listas)
inicio()
print('=' * 25, 'Punto #7', '=' * 25)
while True:
    try:
        numero = int(input('Ingrese el Numero a Multiplicar la Matriz >>> '),)
        for r in range(len(matriz)):
            for c in range(len(matriz)):
                matriz[r][c] = matriz[r][c] * numero
        break
    except:
        print('Digite un numero entero!!')

continuar_opcion()
clear()
# 8. mostrar la segunda matriz
# Loop para ejecutar la impresion de la nueva matriz en el formato
inicio()
print('=' * 25, 'Punto #8', '=' * 25)
for r in range(len(matriz)):
    for c in range(len(matriz)):
        print(matriz[r][c], end='\t')
    print()

continuar_opcion()
clear()