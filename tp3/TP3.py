import itertools
import time

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

def run_tests(test_files, expected_values, func):
    if func == 'B':
        func = backtracking
    elif func == 'A':
        func = distribuir_maestros
    for i in range(len(test_files)):
        file_path = test_files[i]
        expected_value = expected_values[i]
        maestros, k, n = read_file(file_path)
        print(f"File = {file_path}")
        print(f"n = {n}, k = {k}")
        print(f"Maestros: {maestros}")
        start_time = time.time()
        best_value, best_partition = func(maestros, k)
        end_time = time.time()
        print(f"Mejor partición: {best_partition}")
        print(f"Valor óptimo: {best_value}")
        try:
            assert best_value == expected_value
            print(f"OK")
        except AssertionError:
            print(f"ERROR: Valor óptimo para {file_path} es {best_value}, pero se esperaba {expected_value}")

        print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
        print()

def run_tests_only_assert(test_files, expected_values):
    for i in range(len(test_files)):
        file_path = test_files[i]
        expected_value = expected_values[i]
        maestros, k, n = read_file(file_path)
        print(f"File = {file_path}")
        best_value, best_partition = backtracking(maestros, k)
        try:
            assert best_value == expected_value
            print(f"OK")
        except AssertionError:
            print(f"ERROR: Valor óptimo para {file_path} es {best_value}, pero se esperaba {expected_value}")
        print()

if __name__ == '__main__':
    test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
                  '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt', '15_4.txt',
                  '15_6.txt', '17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt', '18_8.txt', '20_4.txt',
                  '20_5.txt', '20_8.txt']

    expected_values = [1894340, 1640690, 807418, 4298131, 385249, 355882, 2906564,
                       15659106, 15292055, 10694510, 4311889, 6377225, 15974095, 11513230,
                       5427764, 10322822, 11971097, 21081875, 16828799, 11417428]
    select_algorithm = input("Para correr el algoritmo de backtracking ingrese B, para correr el algoritmo de aproximacion ingrese A ").upper()
    if select_algorithm == 'B':
        run_only_assert = input(
            "Para correr unicamente los asserts ingrese T, para correr los asserts con mas informacion ingrese F ").upper() == 'T'
        if run_only_assert:
            run_tests_only_assert(test_files, expected_values)
        else:
            run_tests(test_files, expected_values, select_algorithm)
    elif select_algorithm == 'A':
        run_tests(test_files, expected_values, select_algorithm)
