import itertools
import time
import random


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

# Aproximacion punto 5
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

# Run usage

#
# def run_tests_only_assert(test_files, expected_values):
#     for i in range(len(test_files)):
#         file_path = test_files[i]
#         expected_value = expected_values[i]
#         maestros, k, n = read_file(file_path)
#         print(f"File = {file_path}")
#         best_value, best_partition = backtracking(maestros, k)
#         try:
#             assert best_value == expected_value
#             print(f"OK")
#         except AssertionError:
#             print(f"ERROR: Valor óptimo para {file_path} es {best_value}, pero se esperaba {expected_value}")
#         print()
#
# if __name__ == '__main__':
#     set_simple_rel = input("Para correr tests simples ingrese S, para correr tests para relaciones ingrese R").upper()
#     if set_simple_rel == 'S':
#         set_data = input("Para correr los tests con los archivos de prueba ingrese T, para correr los tests con datos generados aleatoriamente ingrese A").upper()
#         if set_data == 'T':
#             test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
#                           '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt',
#                           '15_6.txt', '17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
#                           '20_5.txt', '20_8.txt']
#
#             expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
#                                15659106, 15292055, 10694510, 4311889, 6377225, 15974095, 11513230,
#                                5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
#
#             select_algorithm = input("Para correr el algoritmo de backtracking ingrese B, para correr el algoritmo de aproximacion ingrese A ").upper()
#             if select_algorithm == 'B':
#                 run_only_assert = input(
#                     "Para correr unicamente los asserts ingrese T, para correr los asserts con mas informacion ingrese F ").upper() == 'T'
#                 if run_only_assert:
#                     run_tests_only_assert(test_files, expected_values)
#                 else:
#                     run_tests(test_files, expected_values, select_algorithm)
#
#             elif select_algorithm == 'A':
#                 run_tests(test_files, expected_values, select_algorithm)
#
#         elif set_data == 'A':
#             cant_sets_aleatorios = int(input("Ingrese la cantidad de sets aleatorios a generar: "))
#             select_algorithm = input("Para correr el algoritmo de backtracking ingrese B, para correr el algoritmo de aproximacion ingrese A, \n"
#                                      "si desea correr ambos ingrese BA").upper()
#             if select_algorithm == 'B':
#                 print("Backtracking")
#                 for i in range(cant_sets_aleatorios):
#                     num_maestros = random.randint(5, 20)
#                     max_habilidad = random.randint(1, 100)
#                     maestros = generar_datos_prueba(num_maestros, max_habilidad)
#                     num_grupos = random.randint(2, 5)
#                     print(f"Set aleatorio {i + 1}")
#                     print(f"Maestros: {maestros}")
#                     print(f"n = {num_maestros}")
#                     print(f"k = {num_grupos}")
#                     start_time = time.time()
#                     best_value, best_partition = backtracking(maestros, num_grupos)
#                     end_time = time.time()
#                     print(f"Mejor partición: {best_partition}")
#                     print(f"Valor óptimo: {best_value}")
#                     print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
#                     print()
#             elif select_algorithm == 'A':
#                 print("Aproximacion")
#                 for i in range(cant_sets_aleatorios):
#                     num_maestros = random.randint(5, 20)
#                     max_habilidad = random.randint(1, 100)
#                     maestros = generar_datos_prueba(num_maestros, max_habilidad)
#                     num_grupos = random.randint(2, 5)
#                     print(f"Set aleatorio {i + 1}")
#                     print(f"Maestros: {maestros}")
#                     print(f"n = {num_maestros}")
#                     print(f"k = {num_grupos}")
#                     start_time = time.time()
#                     best_value, best_partition = distribuir_maestros(maestros, num_grupos)
#                     end_time = time.time()
#                     print(f"Mejor partición: {best_partition}")
#                     print(f"Valor óptimo: {best_value}")
#                     print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
#                     print()
#             elif select_algorithm == 'BA':
#                 for i in range(cant_sets_aleatorios):
#                     num_maestros = random.randint(5, 20)
#                     max_habilidad = random.randint(1, 100)
#                     maestros = generar_datos_prueba(num_maestros, max_habilidad)
#                     num_grupos = random.randint(2, 4)
#                     print(f"Set aleatorio {i + 1}")
#                     print(f"Maestros: {maestros}")
#                     print(f"n = {num_maestros}")
#                     print(f"k = {num_grupos}")
#                     print()
#                     print("Backtracking")
#                     start_time_bt = time.time()
#                     best_value_bt, best_partition_bt = backtracking(maestros, num_grupos)
#                     end_time_bt = time.time()
#                     print(f"Mejor partición: {best_partition_bt}")
#                     print(f"Valor óptimo: {best_value_bt}")
#                     print(f"Tiempo de ejecución: {end_time_bt - start_time_bt:.4f} segundos")
#                     print()
#                     print("Aproximacion")
#                     start_time_a = time.time()
#                     best_value_a, best_partition_a = distribuir_maestros(maestros, num_grupos)
#                     end_time_a = time.time()
#                     print(f"Mejor partición: {best_partition_a}")
#                     print(f"Valor óptimo: {best_value_a}")
#                     print(f"Tiempo de ejecución: {end_time_a - start_time_a:.4f} segundos")
#                     print()
#     elif set_simple_rel == 'R':
#         set_algorithm = input("Para correr el algoritmo de backtracking con el de aproximacion ingrese BA, para correr el algoritmo de \n"
#                               "bactracking con el de aproximacion lineal ingrese BL").upper()
#         if set_algorithm == 'BA':
#             set_data = input(
#                 "Para correr las relacion con archivos de prueba ingrese T, para las relaciones con datos generados aleatoriamente ingrese A, \n"
#                 "para correr las relaciones con volumenes inmanejables ingrese I ").upper()
#             if set_data == 'T':
#                 test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
#                               '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt',
#                               '15_6.txt', '17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
#                               '20_5.txt', '20_8.txt']
#
#                 expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
#                                    15659106, 15292055, 10694510, 4311889, 6377225, 15974095, 11513230,
#                                    5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
#                 for i in range(len(test_files)):
#                     file_path = test_files[i]
#                     expected_value = expected_values[i]
#                     maestros, k, n = read_file(file_path)
#                     print(f"File = {file_path}")
#                     print(f"n = {n}")
#                     print(f"k = {k}")
#                     print(f"Maestros: {maestros}")
#                     print(f"Valor esperado: {expected_value}")
#                     print("Backtracking")
#                     start_time_bt = time.time()
#                     best_value_bt, best_partition_bt = backtracking(maestros, k)
#                     end_time_bt = time.time()
#                     print(f"Mejor partición: {best_partition_bt}")
#                     print(f"Valor óptimo: {best_value_bt}")
#                     print(f"Tiempo de ejecución: {end_time_bt - start_time_bt:.4f} segundos")
#                     print()
#                     print("Aproximacion")
#                     start_time_a = time.time()
#                     best_value_a, best_partition_a = distribuir_maestros(maestros, k)
#                     end_time_a = time.time()
#                     print(f"Mejor partición: {best_partition_a}")
#                     print(f"Valor óptimo: {best_value_a}")
#                     print(f"Tiempo de ejecución: {end_time_a - start_time_a:.4f} segundos")
#                     print()
#                     relation = best_value_a / best_value_bt
#                     print(f"Relacion: {relation}")
#                     print()
#             elif set_data == 'A':
#                 cant_sets_aleatorios = int(input("Ingrese la cantidad de sets aleatorios a generar: "))
#                 for i in range(cant_sets_aleatorios):
#                     num_maestros = random.randint(5, 20)
#                     max_habilidad = random.randint(1, 100)
#                     maestros = generar_datos_prueba(num_maestros, max_habilidad)
#                     num_grupos = random.randint(2, 4)
#                     print(f"Set aleatorio {i + 1}")
#                     print(f"Maestros: {maestros}")
#                     print(f"n = {num_maestros}")
#                     print(f"k = {num_grupos}")
#                     print()
#                     print("Backtracking")
#                     start_time_bt = time.time()
#                     best_value_bt, best_partition_bt = backtracking(maestros, num_grupos)
#                     end_time_bt = time.time()
#                     print(f"Mejor partición: {best_partition_bt}")
#                     print(f"Valor óptimo: {best_value_bt}")
#                     print(f"Tiempo de ejecución: {end_time_bt - start_time_bt:.4f} segundos")
#                     print()
#                     print("Aproximacion")
#                     start_time_a = time.time()
#                     best_value_a, best_partition_a = distribuir_maestros(maestros, num_grupos)
#                     end_time_a = time.time()
#                     print(f"Mejor partición: {best_partition_a}")
#                     print(f"Valor óptimo: {best_value_a}")
#                     print(f"Tiempo de ejecución: {end_time_a - start_time_a:.4f} segundos")
#                     print()
#                     relation = best_value_a / best_value_bt
#                     print(f"Relacion: {relation}")
#                     print()
#             elif set_data == 'I':
#                 print("Por ser volumenes inmanejables no corremos Backtracking, pero contamos con los valores optimos")
#                 test_files = ['17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
#                               '20_5.txt', '20_8.txt']
#
#                 expected_values = [15974095, 11513230,5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
#                 for i in range(len(test_files)):
#                     file_path = test_files[i]
#                     expected_value = expected_values[i]
#                     maestros, k, n = read_file(file_path)
#                     print(f"File = {file_path}")
#                     print(f"n = {n}")
#                     print(f"k = {k}")
#                     print(f"Maestros: {maestros}")
#                     print(f"Valor esperado: {expected_value}")
#                     print()
#                     print("Aproximacion")
#                     start_time_a = time.time()
#                     best_value_a, best_partition_a = distribuir_maestros(maestros, k)
#                     end_time_a = time.time()
#                     print(f"Mejor partición: {best_partition_a}")
#                     print(f"Valor óptimo: {best_value_a}")
#                     print(f"Tiempo de ejecución: {end_time_a - start_time_a:.4f} segundos")
#                     print()
#                     relation = best_value_a / expected_value
#                     print(f"Relacion: {relation}")
#                     print()


import random
import time

# Define tus funciones aquí

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
    print(f"Valor óptimo: {best_value}")
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
        print(f"Valor óptimo: {best_value}")
        print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
        print()
        values.append(best_value)
    if len(values) == 2:
        relation = values[1] / values[0]
    else:
        relation = values[0] / expected_value

    print(f"Relacion: {relation}")
    print()

def run_test_files(test_files, expected_values, func):
    if func == '1':
        func = backtracking
    elif func == '2':
        func = distribuir_maestros
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
    for i in range(len(test_files)):
        file_path = test_files[i]
        expected_value = expected_values[i]
        maestros, k, n = read_file(file_path)
        relation_results(file_path=file_path, n=n, k=k, maestros=maestros, expected_value= expected_value, funcs=funcs)

def run_aleatory_relation(qty_sets, funcs):
    for i in range(qty_sets):
        max_habilidad = random.randint(1, 100)
        n = random.randint(5, 20)
        maestros = generar_datos_prueba(n, max_habilidad)
        k = random.randint(2, 5)
        relation_results(aleatory = i+1, n=n, k=k, maestros=maestros, funcs=funcs)

def run_relations():
    print("1. Backtracking VS Aproximación")
    print("2. Backtracking VS Programación Lineal")
    option = input("Ingrese el número de la opción que desea: ")
    print("1. Datos de catedra")
    print("2. Datos aleatorios")
    print("3. Datos inmanejables")
    option_data= input("Ingrese el número de la opción que desea: ")
    if option == '1':
        if option_data == '1':
            test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
                          '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt',
                          '15_6.txt', '17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
                          '20_5.txt', '20_8.txt']
            expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
                               15659106, 15292055, 10694510, 4311889, 6377225, 15974095, 11513230,
                               5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
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




