def operaciones(k):
    memoria = []
    if k == 0:
        return []
    a = 0
    while a < k:
        if a % 2 == 0:
            a = a * 2
            memoria.append("por2")
        else:
            a = a + 1
            memoria.append("mas1")

    print(memoria[::-1])
    return memoria[::-1]

operaciones