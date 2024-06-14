import itertools
import time
import random
import numpy as np
from scipy.optimize import linprog
import heapq

# Certificador Eficiente NP
def certificador_eficiente(subgrupos, B):
    suma_cuadrados = 0

    # Para cada subgrupo S_j, calcular la suma de las habilidades y elevarla al cuadrado
    for subgrupo in subgrupos:
        suma_subgrupo = sum(subgrupo)
        suma_cuadrados += suma_subgrupo ** 2

    # Comparar la suma total de los cuadrados con B
    return suma_cuadrados <= B

# Backtracking
def calcular_objetivo(grupos):
    return sum(sum(num for _, num in grupo) ** 2 for grupo in grupos)

def backtracking(x, k, grupos_actuales=None, indice_actual=0, mejor_valor=float('inf'), mejor_grupo=None):
    if grupos_actuales is None:
        grupos_actuales = [[] for _ in range(k)]

    # Si hemos asignado todos los elementos, evaluamos esta partición
    if indice_actual == len(x):
        valor = calcular_objetivo(grupos_actuales)
        if valor < mejor_valor:
            mejor_grupo = [[nombre for nombre, _ in grupo] for grupo in grupos_actuales]
            return valor, mejor_grupo
        else:
            return mejor_valor, mejor_grupo

    valor_actual = calcular_objetivo(grupos_actuales)  # Calcular el valor objetivo actual
    for i in range(k):
        grupos_actuales[i].append(x[indice_actual])

        # Evitar agregar si la suma actual ya supera el mejor valor conocido
        if valor_actual < mejor_valor:
            valor, grupo = backtracking(
                x, k, grupos_actuales, indice_actual + 1, mejor_valor,mejor_grupo)

            if valor < mejor_valor:
                mejor_valor, mejor_grupo = valor, grupo

        grupos_actuales[i].pop()

        # Si se añade a un grupo vacío, no tiene sentido intentar con otros grupos vacíos
        if not grupos_actuales[i]:
            break

    return mejor_valor, mejor_grupo

# Aproximacion (Punto 5)
def suma_cuadrados(sumas_grupos):
    return sum(suma ** 2 for suma in sumas_grupos)

def distribuir_maestros(maestros, k):
    maestros_ordenados = sorted(maestros, key=lambda x: x[1], reverse=True)
    grupos = [[] for _ in range(k)]
    sumas_grupos = [0] * k

    for nombre, habilidad in maestros_ordenados:
        indice_grupo = sumas_grupos.index(min(sumas_grupos))
        grupos[indice_grupo].append(nombre)
        sumas_grupos[indice_grupo] += habilidad

    return suma_cuadrados(sumas_grupos), grupos

# Aproximacion Lineal
def aproximacionLineal(maestros, k):
    # Setup data
    habilidades = [habilidad for nombre, habilidad in maestros]
    n = len(habilidades)
    habilidades = np.array(habilidades)
    # Crear variables de decisión
    num_vars = n * k
    bounds = [(0, 1)] * num_vars + [(None, None), (None, None)]  # Agregar M y m

    # Restricción: cada maestro debe estar en un solo subgrupo
    A_eq = np.zeros((n, num_vars + 2))
    for i in range(n):
        for j in range(k):
            A_eq[i, i * k + j] = 1
        b_eq = np.ones(n)

    # Restricciones para M y m
    A_ub = np.zeros((2 * k, num_vars + 2))
    b_ub = np.zeros(2 * k)

    for j in range(k):
        for i in range(n):
            A_ub[j, i * k + j] = habilidades[i]
            A_ub[k + j, i * k + j] = -habilidades[i]
        A_ub[j, -2] = -1  # M constraint
        A_ub[k + j, -1] = 1  # m constraint

    # Definir la función objetivo para minimizar M - m
    c = np.zeros(num_vars + 2)
    c[-2] = 1  # Max variable
    c[-1] = -1  # Min variable

    # Medir tiempo de ejecución del modelo de programación lineal con HiGHS
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    # Resultado
    if res.success:
        solution = res.x[:-2].reshape(n, k)
        # Asegurarse de que cada maestro está asignado a un grupo
        assigned = np.sum(solution, axis=1)
        if np.allclose(assigned, 1):
            subgrupos = [np.where(solution[:, j] >= 0.5)[0] for j in range(k)]
            sum_squares = sum(np.sum(habilidades[subgrupo]) ** 2 for subgrupo in subgrupos)
            return sum_squares, subgrupos
        else:
            print("Error: No todos los maestros están asignados a un grupo.")
    else:
        print("No se encontró una solución óptima.")

# Nueva Aproximacion (Punto 6)
def distribuir_maestros_equilibrio(maestros, k):
    maestros_ordenados = sorted(maestros, key=lambda x: x[1], reverse=True)
    grupos = [[] for _ in range(k)]
    sumas_grupos = [0] * k
    heap = [(0, i) for i in range(k)]  # (suma, índice del grupo)
    heapq.heapify(heap)

    # Asigna de manera alternada para equilibrar la carga
    for nombre, habilidad in maestros_ordenados:
        suma_actual, indice_grupo = heapq.heappop(heap)
        grupos[indice_grupo].append(nombre)
        suma_actual += habilidad
        sumas_grupos[indice_grupo] = suma_actual
        heapq.heappush(heap, (suma_actual, indice_grupo))

    return suma_cuadrados(sumas_grupos), grupos

# Run Usage
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Saltar líneas de comentarios y vacías
    lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]

    k = int(lines[0].strip())  # La primera línea no comentada es la cantidad de grupos
    masters = []
    for line in lines[1:]:
        parts = line.strip().split(', ')
        if len(parts) == 2:
            masters.append((parts[0], int(parts[1])))
        else:
            print(f"Línea ignorada por formato incorrecto: {line.strip()}")

    n = len(masters)  # Número total de maestros

    return masters, k, n

def generar_datos_prueba(num_maestros, max_habilidad):
    maestros = [(f"Maestro_{i}", random.randint(1, max_habilidad)) for i in range(num_maestros)]
    return maestros
def print_results(file_path=None, aleatory=None, n=0, k=0, maestros=[()], best_partition=0,
                  best_value=0, start_time=0, end_time=0, expected_value=None):
    if file_path:
        print(f"File = {file_path}")
    if aleatory:
        print(f"Set aleatorio {aleatory}")
    print(f"n = {n}")
    print(f"k = {k}")
    print(f"Maestros: {maestros}")
    print(f"Mejor partición: {best_partition}")
    print(f"Valor obtenido: {best_value}")
    if expected_value is not None:
        print(f"Valor esperado: {expected_value}")
    print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
    print()
def relation_results(file_path=None, aleatory=None, n=0, k=0, maestros=[(str, int)], expected_value=None, funcs=[]):
    if file_path:
        print(f"File = {file_path}")
    if aleatory:
        print(f"Set aleatorio {aleatory}")
    print(f"n = {n}")
    print(f"k = {k}")
    print(f"Maestros: {maestros}")
    print(f"Valor esperado: {expected_value}")
    values = []
    # Corregir esto
    for func in funcs:
        print(f"{func}")
        start_time = time.time()
        best_value, best_partition = func(maestros, k)
        end_time = time.time()
        print(f"Mejor partición: {best_partition}")
        print(f"Valor obtenido: {best_value}")
        print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
        print()
        values.append(best_value)
    if len(values) == 2:
        relation = values[1] / values[0]
    else:
        relation = values[0] / expected_value

    if relation > max:
        max = relation
    print(f" MAX INTER: {max}")
    print(f"Relacion: {relation}")
    print()
def run_test_files(test_files, expected_values, func):
    if func == '1':
        func = backtracking
    elif func == '2':
        func = distribuir_maestros
    elif func == '3':
        func = aproximacionLineal
    elif func == '4':
        func = distribuir_maestros_equilibrio
    for i in range(len(test_files)):
        file_path = test_files[i]
        expected_value = expected_values[i]
        maestros, k, n = read_file(file_path)
        start_time = time.time()
        best_value, best_partition = func(maestros, k)
        end_time = time.time()
        print_results(file_path = file_path, n = n, k = k, maestros = maestros,
                      best_partition = best_partition, best_value = best_value,
                      start_time = start_time, end_time = end_time, expected_value = expected_value)
def run_aleatory_tests(qty_sets, func):
    if func == '1':
        func = backtracking
    elif func == '2':
        func = distribuir_maestros
    elif func == '3':
        func = aproximacionLineal
    elif func == '4':
        func = distribuir_maestros_equilibrio

    for i in range(qty_sets):
        max_habilidad = random.randint(1, 100)
        n = random.randint(5, 20)
        maestros = generar_datos_prueba(n, max_habilidad)
        k = random.randint(2, 5)
        start_time = time.time()
        best_value, best_partition = func(maestros, k)
        end_time = time.time()
        print_results(aleatory = i+1, n = n, k = k, maestros = maestros,
                      best_partition = best_partition, best_value = best_value,
                      start_time = start_time, end_time = end_time)
def run_tests():
    print("1. Datos de catedra")
    print("2. Datos aleatorios")
    option = input("Ingrese el número de la opción que desea: ")
    print("1. Algoritmo Backtraking")
    print("2. Algoritmo Aproximación")
    print("3. Algoritmo Programacion Lineal")
    print("4. Algoritmo de Aproximacion por Equilibrio de Carga (Punto 6)")
    option_alg = input("Ingrese el número de la opción que desea: ")
    if option == '1':
        test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
                      '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt',
                      '15_6.txt', '17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
                      '20_5.txt', '20_8.txt']

        expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
                           15659106, 15292055, 10694510, 4311889, 6377225, 15974095, 11513230,
                           5427764, 10322822, 11971097, 21081875, 16828799, 11417428]

        run_test_files(test_files, expected_values, option_alg)

    elif option == '2':
        qty_sets = int(input("Ingrese la cantidad de sets aleatorios a generar: "))
        run_aleatory_tests(qty_sets, option_alg)
def run_file_relation(test_files, expected_values,funcs):
    max = -1
    for i in range(len(test_files)):
        file_path = test_files[i]
        expected_value = expected_values[i]
        maestros, k, n = read_file(file_path)
        relation_results(file_path=file_path, n=n, k=k, maestros=maestros, expected_value= expected_value, funcs=funcs)
def run_aleatory_relation(qty_sets, funcs):
    max = -1
    for i in range(qty_sets):
        max_habilidad = random.randint(1, 100)
        n = random.randint(5, 20)
        maestros = generar_datos_prueba(n, max_habilidad)
        k = random.randint(2, 5)
        relation_results(aleatory = i+1, n=n, k=k, maestros=maestros, funcs=funcs)
def run_relations():
    print("1. Backtracking VS Aproximación")
    print("2. Backtracking VS Programación Lineal")
    print("3. Backtracking VS Aproximación por Equilibrio de Carga (Punto 6)")
    option = input("Ingrese el número de la opción que desea: ")
    print("1. Datos de catedra")
    print("2. Datos aleatorios")
    print("3. Datos inmanejables")
    option_data= input("Ingrese el número de la opción que desea: ")
    if option == '1':
        if option_data == '1':
            test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
                          '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt', '15_6.txt']
            expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
                               15659106, 15292055, 10694510, 4311889, 6377225]
            run_file_relation(test_files, expected_values, [backtracking, distribuir_maestros])
        elif option_data == '2':
            qty_sets = int(input("Ingrese la cantidad de sets aleatorios a generar: "))
            run_aleatory_relation(qty_sets, [backtracking, distribuir_maestros])

        elif option_data == '3':
            print("Por ser volumenes inmanejables no corremos Backtracking, pero contamos con los valores optimos")
            test_files = ['17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
                          '20_5.txt', '20_8.txt']

            expected_values = [15974095, 11513230, 5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
            run_file_relation(test_files, expected_values, [distribuir_maestros])
    elif option == '2':
        if option_data == '1':
            test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
                          '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt', '15_6.txt']
            expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
                               15659106, 15292055, 10694510, 4311889, 6377225]
            run_file_relation(test_files, expected_values, [backtracking, aproximacionLineal])
        elif option_data == '2':
            qty_sets = int(input("Ingrese la cantidad de sets aleatorios a generar: "))
            run_aleatory_relation(qty_sets, [backtracking, aproximacionLineal])

        elif option_data == '3':
            print("Por ser volumenes inmanejables no corremos Backtracking, pero contamos con los valores optimos")
            test_files = ['17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
                          '20_5.txt', '20_8.txt']

            expected_values = [15974095, 11513230, 5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
            run_file_relation(test_files, expected_values, [aproximacionLineal])
    elif option == '3':
        if option_data == '1':
            test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
                          '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt', '15_6.txt']
            expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
                               15659106, 15292055, 10694510, 4311889, 6377225]
            run_file_relation(test_files, expected_values, [backtracking, distribuir_maestros_equilibrio])
        elif option_data == '2':
            qty_sets = int(input("Ingrese la cantidad de sets aleatorios a generar: "))
            run_aleatory_relation(qty_sets, [backtracking, distribuir_maestros_equilibrio])

        elif option_data == '3':
            print("Por ser volumenes inmanejables no corremos Backtracking, pero contamos con los valores optimos")
            test_files = ['17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
                          '20_5.txt', '20_8.txt']

            expected_values = [15974095, 11513230, 5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
            run_file_relation(test_files, expected_values, [distribuir_maestros_equilibrio])


def main():
    while True:
        print("1. Correr Tests")
        print("2. Correr Relaciones")
        print("3. Salir")
        option = input("Ingrese el número de la opción que desea: ")

        if option == '1':
            run_tests()
        elif option == '2':
            run_relations()
        elif option == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == '__main__':
    main()




