def max_soldados_elim(x, f):
    n = len(x)
    G = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
          if j == i:
            G[i][j] = min(x[i - 1], f[i - 1])
          else:
            G[i][j] = max(G[i - j]) + min(x[i - 1], f[j - 1])

    return max(G[n])

def matriz_soldados_elim(x, f):
    n = len(x)
    DP = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(0, i + 1):
          if j == 0:
            DP[i][j] = max(DP[i - 1])
          elif j == i:
            DP[i][j] = min(x[i - 1], f[i - 1])
          else:
            DP[i][j] = DP[i - j + 1][0] + min(x[i - 1], f[j - 1])
    return DP

def reconstruir_camino(x,f):
  G = matriz_soldados_elim(x, f)
  n = len(x)

  #Armo la lista llena de "Cargar" y pongo "Atacar" al final porque siempre se ataca al final
  estrategia = ["Cargar" for _ in range(n - 1)]
  estrategia.append("Atacar")
  i = n

  while( i > 0 ):
    j = G[i].index(max(G[i]))
    i = i - j
    estrategia[i - 1] = "Atacar"

  return estrategia

def leer_archivo(nombre_archivo):
    lista_x = []
    lista_f = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            n = int(lineas[1])
            for i in range(2, 2 * n + 2):
                valor = int(lineas[i])
                if i <= n+1:
                    lista_x.append(valor)
                else:
                    lista_f.append(valor)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    
    return lista_x, lista_f


if __name__ == '__main__':
    mostrar_caminos = input("¿Desea ver los caminos reconstruidos? (s/n): ").lower() == 's'

    x, f = leer_archivo('5.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 1413
    print("OK TEST 1")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)
    
    x, f = leer_archivo('10_bis.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 1237
    print("OK TEST 2") 
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)

    x, f = leer_archivo('10.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 2118
    print("OK TEST 3")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)

    x, f = leer_archivo('20.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 11603
    print("OK TEST 4")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)

    x, f = leer_archivo('50.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 3994
    print("OK TEST 5")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)

    x, f = leer_archivo('100.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 7492
    print("OK TEST 6")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)
    x, f = leer_archivo('200.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 4230
    print("OK TEST 7")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)

    x, f = leer_archivo('500.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 15842
    print("OK TEST 8")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)

    x, f = leer_archivo('1000.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 4508
    print("OK TEST 9")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)

    x, f = leer_archivo('5000.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 504220
    print("OK TEST 10")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f)
        print(caminos)