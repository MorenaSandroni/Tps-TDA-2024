import itertools
import time


def calculate_objective(groups):
    """Calculate the objective function value for the given groups."""
    return sum(sum(group) ** 2 for group in groups)


def backtracking_with_pruning(x, k, current_groups=None, current_index=0, best_value=float('inf'), best_partition=None):
    """Backtracking algorithm with pruning to find the optimal partition of x into k groups."""
    if current_groups is None:
        current_groups = [[] for _ in range(k)]

    # If we've assigned all elements, evaluate this partition
    if current_index == len(x):
        value = calculate_objective(current_groups)
        if value < best_value:
            return value, [list(group) for group in current_groups]  # Create a deep copy of the groups
        else:
            return best_value, best_partition

    # Try adding the current element to each group and recurse
    for i in range(k):
        current_groups[i].append(x[current_index])
        value, partition = backtracking_with_pruning(
            x, k, current_groups, current_index + 1, best_value, best_partition)

        # Prune if the current value exceeds the best found so far
        if value < best_value:
            best_value, best_partition = value, partition

        # Backtrack: remove the element and try the next group
        current_groups[i].pop()

    return best_value, best_partition


# Función para generar datos de prueba
def generate_test_data(n, max_value=100):
    """Generate test data with n elements."""
    import random
    return [random.randint(1, max_value) for _ in range(n)]


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
            masters.append(parts)
        else:
            print(f"Línea ignorada por formato incorrecto: {line.strip()}")

    x = [int(master[1]) for master in masters]  # Extraer las habilidades
    n = len(x)  # Número total de maestros

    return x, k, n


test_files = ['5_2.txt', '6_3.txt', '6_4.txt', '8_3.txt', '10_3.txt', '10_5.txt',
              '10_10.txt', '11_5.txt', '14_3.txt', '14_4.txt', '14_6.txt','15_4.txt',
              '15_6.txt', '17_5.txt', '17_7.txt', '17_10.txt', '18_6.txt','18_8.txt','20_4.txt',
              '20_5.txt', '20_8.txt']
for file_path in test_files:
    x, k, n = read_file(file_path)
    print(f"File = {file_path}")
    print(f"n = {n}, k = {k}")
    print(f"Habilidades: {x}")
    start_time = time.time()
    best_value, best_partition = backtracking_with_pruning(x, k)
    end_time = time.time()
    print(f"Mejor partición: {best_partition}")
    print(f"Valor óptimo: {best_value}")
    print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
    print()