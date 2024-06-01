def array_soldados_elim(x, f):
    n = len(x)
    DP = [0] * (n + 1)
    for i in range(1, n + 1):
        DP[i] = max(DP[j] + min(x[i - 1], f[i - j - 1]) for j in range(i))

    return DP

def max_soldados_elim(x, f):
    return array_soldados_elim(x,f)[-1]


def reconstruir_camino(x, f, DP):
    n = len(x)
    camino = []
    i = n  # Empezamos desde el final

    while i > 0:
        for j in range(i):
            if DP[i] == DP[j] + min(x[i - 1], f[i - j - 1]):
                camino.append(i - 1) 
                i = j
                break

    camino.reverse()  # Porque construimos el camino desde el final

    # Ahora asociamos los indices conseguidos a las acciones correspondientes

    estrategia = ["Cargar"] * n

    for i in camino:
        estrategia[i] = "Atacar" # Si el indice está en el camino, significa que en ese minuto se atacó

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
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)
    
    x, f = leer_archivo('10_bis.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 1237
    print("OK TEST 2") 
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)

    x, f = leer_archivo('10.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 2118
    print("OK TEST 3")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)

    x, f = leer_archivo('20.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 11603
    print("OK TEST 4")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)

    x, f = leer_archivo('50.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 3994
    print("OK TEST 5")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)

    x, f = leer_archivo('100.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 7492
    print("OK TEST 6")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)
    x, f = leer_archivo('200.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 4230
    print("OK TEST 7")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)

    x, f = leer_archivo('500.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 15842
    print("OK TEST 8")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)

    x, f = leer_archivo('1000.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 4508
    print("OK TEST 9")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)

    x, f = leer_archivo('5000.txt')
    resultado = max_soldados_elim(x, f)
    assert resultado == 504220
    print("OK TEST 10")
    if mostrar_caminos:
        print("Caminos reconstruidos:")
        caminos = reconstruir_camino(x, f, array_soldados_elim(x, f))
        print(caminos)