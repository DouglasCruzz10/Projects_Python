# multiplica todos os elementos de uma lista e retorna o resultado

def mult_list(lista):
    result = 1
    for i in lista:
        result *= i
    return result