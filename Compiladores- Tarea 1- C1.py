def minimizar_dfa(n, alfabeto, estadosF, transiciones):

    tabla = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if (i in estadosF) != (j in estadosF):
                tabla[i][j] = True

    cambiado = True
    while cambiado:
        cambiado = False
        for i in range(n):
            for j in range(i + 1, n):
                if not tabla[i][j]:  
                    for simbolo in alfabeto:
                        p = transiciones[i][alfabeto.index(simbolo)]
                        q = transiciones[j][alfabeto.index(simbolo)]
                        if p != q and tabla[min(p, q)][max(p, q)]:
                            tabla[i][j] = True
                            cambiado = True
                            break

    paresIgual = [(i, j) for i in range(n) for j in range(i + 1, n) if not tabla[i][j]]

    return paresIgual

c = int(input("Ingrese el número de casos: "))

casos = []

for _ in range(c):
    n = int(input("Ingrese el número de estados del DFA: "))
    alfabeto = input("Ingrese el alfabeto del DFA (separado por espacios): ").split()
    estadosF = list(map(int, input("Ingrese los estados finales (separados por espacios): ").split()))

    transiciones = []
    print("Ingrese la tabla de transiciones, una fila por estado:")
    for _ in range(n):
        transiciones.append(list(map(int, input().split())))

    casos.append((n, alfabeto, estadosF, transiciones))

ResultadosCompletos = []
for n, alfabeto, estadosF, transiciones in casos:
    paresIgual = minimizar_dfa(n, alfabeto, estadosF, transiciones)

    if paresIgual:
        pares_formateados = " ".join(f"({pair[0]}, {pair[1]})" for pair in paresIgual)
        ResultadosCompletos.append(pares_formateados)
    else:
        ResultadosCompletos.append("")

for result in ResultadosCompletos:
    print(result)
