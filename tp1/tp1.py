
def calcular_tiempo_total(batallas):
    batallas = ordenar_por_proporcion(batallas)
    coef_de_impacto = 0 # Suma acumulada de los tiempos de finalizacion
    t_total = 0 # Tiempo total
    for t_act, b_act in batallas:
        coef_de_impacto += (t_total + t_act) * b_act
        t_total += t_act
    return coef_de_impacto

def ordenar_por_proporcion(batallas):
    batallas.sort(key = lambda x: x[1]/x[0], reverse=True)
    return batallas

def leer_archivo(ruta):
    lista = [] 
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            if linea == 'T_i,B_i\n': continue
            t, b = linea.split(',')
            lista.append((int(t), int(b)))
    return lista


if __name__ == '__main__':
    test_1 = leer_archivo('10.txt')
    assert calcular_tiempo_total(test_1) == 309600
    print("OK TEST 1")
    test_2 = leer_archivo('50.txt')
    assert calcular_tiempo_total(test_2) == 5218700
    print("OK TEST 2") 
    test_3 = leer_archivo('100.txt')
    assert calcular_tiempo_total(test_3) == 780025365
    print("OK TEST 3")
    test_4 = leer_archivo('1000.txt')
    assert calcular_tiempo_total(test_4) == 74329021942
    print("OK TEST 4")
    test_5 = leer_archivo('5000.txt')
    assert calcular_tiempo_total(test_5) == 1830026958236
    print("OK TEST 5")
    test_6 = leer_archivo('10000.txt')
    assert calcular_tiempo_total(test_6) == 7245315862869
    print("OK TEST 6")
    test_7 = leer_archivo('100000.txt')
    assert calcular_tiempo_total(test_7) == 728684685661017
    print("OK TEST 7")
   
    
