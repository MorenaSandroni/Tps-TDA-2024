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
maestros, k, n = read_file("prop_24_8.txt")
best_value, best_partition = backtracking(maestros, k)
print_results(file_path ="prop_24_8.txt", n = n, k = k, maestros = maestros,
              best_partition = best_partition, best_value = best_value,
              start_time = 0, end_time = 0, expected_value = 0)