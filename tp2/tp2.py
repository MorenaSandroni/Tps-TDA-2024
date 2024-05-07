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
    x, f = leer_archivo('5.txt')
    assert max_soldados_elim(x,f) == 1413
    print("OK TEST 1")
    x, f = leer_archivo('10_bis.txt')
    assert max_soldados_elim(x, f) == 1237
    print("OK TEST 2") 
    x, f = leer_archivo('10.txt')
    assert max_soldados_elim(x, f) == 2118
    print("OK TEST 3")
    x, f = leer_archivo('20.txt')
    assert max_soldados_elim(x, f) == 11603
    print("OK TEST 4")
    x, f = leer_archivo('50.txt')
    assert max_soldados_elim(x, f) == 3994
    print("OK TEST 5")
    x, f = leer_archivo('100.txt')
    assert max_soldados_elim(x, f) == 7492
    print("OK TEST 6")
    x, f = leer_archivo('200.txt')
    assert max_soldados_elim(x, f) == 4230
    print("OK TEST 7")
    x, f = leer_archivo('500.txt')
    assert max_soldados_elim(x, f) == 15842
    print("OK TEST 8")
    x, f = leer_archivo('1000.txt')
    assert max_soldados_elim(x, f) == 4508
    print("OK TEST 9")
    x, f = leer_archivo('5000.txt')
    assert max_soldados_elim(x, f) == 504220
    print("OK TEST 10")