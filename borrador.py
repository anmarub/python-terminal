matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
while True:
    try:
        numero = int(input('Ingrese el Numero a Multiplicar la Matriz >>> '),)
        for r in range(len(matriz)):
            for c in range(len(matriz)):
                matriz[r][c] = matriz[r][c] * numero
        break
    except:
        print('Digite un numero entero!!')

