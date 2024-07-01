import random

# Lista de nombres de maestros y habilidades
nombres_base = [
    "Ming-Hua", "Yakone", "Tho", "Rafa", "Unalaq", "Wei", "Katara",
    "Hama", "Sura", "Pakku", "La", "Amon", "Ming-Hua I", "Amon I",
    "Tonraq", "Sangok", "Kuruk", "Hama I", "Sura I", "Misu", "Kuruk I",
    "Hama II", "Sura II", "Misu I", "Amon I", "Ming-Hua A", "Yakone E",
    "ThoER", "Rafar", "Unalaqq I"
]

def generar_habilidades_base(n):
    return [int(random.randint(20, 120)) for _ in range(n)]


# Función para generar los archivos de texto con los datos solicitados
def generar_datos(n_archivo, total_elementos, n_grupos):
    archivo_nombre = f"propio_{total_elementos}_{n_grupos}.txt"

    with open(f"./{archivo_nombre}", "w") as f:
        f.write(f"# La primera linea indica la cantidad de grupos a formar, las siguientes son de la forma 'nombre maestro, habilidad'\n")
        f.write(f"{n_grupos}\n")
        cant_elem_subgrupos = total_elementos//n_grupos
        habilidades_base = generar_habilidades_base(cant_elem_subgrupos)
        sum_habilidades = sum(habilidades_base)
        valor_obtenido = (sum_habilidades ** 2) * n_grupos
        for i in range(n_grupos):
            for j in range(cant_elem_subgrupos):
                nombre = nombres_base[i % len(nombres_base)] + f"_{i//len(nombres_base)}_{j}"
                habilidad = habilidades_base[j]
                f.write(f"{nombre}, {habilidad}\n")
    return archivo_nombre, valor_obtenido

# Generar los archivos con diferentes configuraciones
try:
    with open("./propio_resultados_esperados.txt", "w") as f:
        archivo_nombre, valor_obtenido = generar_datos(1, 32, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(2, 36, 4)
        f.write(f"{archivo_nombre,valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(3, 40, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(4, 44, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(5, 48, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(6, 52, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(7, 56, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(8, 60, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(9, 64, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(10, 68, 4)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(1, 30, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(2, 36, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(3, 42, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(4, 48, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(5, 54, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(6, 60, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(7, 66, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(8, 72, 6)
        f.write(f"{archivo_nombre,  valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(9, 78, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(10, 84, 6)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(1, 24, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(2, 32, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(3, 40, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(4, 48, 8)
        f.write(f"{archivo_nombre,  valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(5, 56, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(6, 64, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(7, 72, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(8, 80, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(9, 88, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")
        archivo_nombre, valor_obtenido = generar_datos(10, 96, 8)
        f.write(f"{archivo_nombre, valor_obtenido}\n")

except Exception as e:
    print(f"Error: {e}")

