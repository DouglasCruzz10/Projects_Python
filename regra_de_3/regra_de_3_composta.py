from modules.get_input import valida_numero
from modules.has_x import has_x
from modules.multiplication import mult_list

def regra_de_3_composta():
    names_greatness_list = []
    startvalue_greatness_list = []
    finalvalue_greatness_list = []
    
    greatness_qtd_str = input('Digite a quantidade de grandezas que sua regra de 3 possui [>3]: ')
    # valida se o que o usuário escreveu foi um número, caso contrário o bota em um loop até que a entrada seja apenas númerica
    while True:
        if not greatness_qtd_str.isdigit():
            greatness_qtd_str = input('ERRO! Digite apenas números: ')
        else:
            greatness_qtd_int = int(greatness_qtd_str)
            break
    # valida se o número de grandezas que o usuário escolheu é maior ou igual a 3,
    # caso contrário o coloca em um loop até que a entrada seja maior ou igual a 3
    while True:
        if greatness_qtd_int < 3:
            greatness_qtd_str = input('ERRO! Regras de 3 composta possuem mais de 3 grandezas! Digite novamente: ')
            # valida se o que o usuário escreveu foi um número, caso contrário,
            # o bota em um loop até que a entrada seja apenas númerica
            while True:
                if not greatness_qtd_str.isdigit():
                    greatness_qtd_str = input('ERRO! Digite apenas números: ')
                else:
                    greatness_qtd_int = int(greatness_qtd_str)
                    break

        else:
            greatness_qtd_int = int(greatness_qtd_str)
            break
    
    print('Quando for determinar a incognita use "X" !')

    # um loop for que se repetirá de acordo com a quantidade de grandezas escolhidas
    for i in range(0, greatness_qtd_int):
        # faz o usuário digitar o nome das grandezas de acordo com o número de grandezas que ele escolheu
        print(f'Digite o nome da {i+1}º grandeza:', end=' ')
        names_greatness_list.append(input())

        # insere o valor inicial da grandeza numa variável
        startvalue_greatness = input(f'Digite o valor inicial da grandeza {names_greatness_list[i]}: ')
        
        # se o valor digitado for x minusculo transforma-o em maiuscúlo
        if startvalue_greatness == 'x':
            startvalue_greatness = startvalue_greatness.upper()

        # irá verificar se já existe X dentro das listas de valor, se sim o bota num loop que só quebra quando ele digita um
        # valor númerico.
        while True:
            if (has_x(startvalue_greatness_list) or has_x(finalvalue_greatness_list)) and startvalue_greatness == 'X':
                startvalue_greatness = input('ERRO! incógnita "X" já foi definida, Digite novamente: ')
                if startvalue_greatness == 'x':
                    startvalue_greatness = startvalue_greatness.upper()
            else:
                break

        # irá verificar se o valor da variável é x, se minúsculo converte pra maiúscula, depois adiciona na lista.
        if startvalue_greatness == 'x':
            startvalue_greatness = startvalue_greatness.upper()
        if startvalue_greatness == 'X':
            startvalue_greatness_list.append(startvalue_greatness)
        # se o valor conter qualquer letra que não seja o "X" faz com que o usuário caia num loop até que digite corretamente
        # um valor numerico.
        elif not valida_numero(startvalue_greatness):
            while True:
                startvalue_greatness = input('ERRO! Digite apenas números ou "X"!: ')
                if startvalue_greatness == 'x':
                    startvalue_greatness = startvalue_greatness.upper()

                    # irá verificar se já existe X dentro das listas de valor, se sim o bota num loop que só quebra quando ele digita um
                    # valor númerico.
                    while True:
                        if (has_x(startvalue_greatness_list) or has_x(finalvalue_greatness_list)) and startvalue_greatness == 'X':
                            startvalue_greatness = input('ERRO! incógnita "X" já foi definida, Digite novamente: ')
                            if startvalue_greatness == 'x':
                                startvalue_greatness = startvalue_greatness.upper()
                        else:
                            break
                    break
                if valida_numero(startvalue_greatness) and startvalue_greatness != 'X':
                    break
            startvalue_greatness_list.append(startvalue_greatness)
        else:
            startvalue_greatness_list.append(startvalue_greatness)
        
        # insere o valor final da grandeza numa variável
        finalvalue_greatness = input(f'Digite o valor final da grandeza {names_greatness_list[i]}: ')

        if finalvalue_greatness == 'x':
            finalvalue_greatness = finalvalue_greatness.upper()

        # irá verificar se já existe X dentro das listas de valor, se sim o bota num loop que só quebra quando ele digita um
        # valor númerico.
        while True:
            if (has_x(startvalue_greatness_list) or has_x(finalvalue_greatness_list)) and finalvalue_greatness == 'X':
                finalvalue_greatness = input('ERRO! incógnita "X" já foi definida, Digite novamente: ')
                if finalvalue_greatness == 'x':
                    finalvalue_greatness = finalvalue_greatness.upper()
            else:
                break

        # irá verificar se o valor da variável é x, se minúsculo converte pra maiúscula, depois adiciona na lista.
        if finalvalue_greatness == 'x':
            finalvalue_greatness = finalvalue_greatness.upper()
        if finalvalue_greatness == 'X':
            finalvalue_greatness_list.append(finalvalue_greatness)
        # se o valor conter qualquer letra que não seja o "X" faz com que o usuário caia num loop até que digite corretamente
        # um valor numerico.    
        elif not valida_numero(finalvalue_greatness):
            while True:
                finalvalue_greatness = input('ERRO! Digite apenas números ou "X"!: ')
                if finalvalue_greatness == 'x':
                    finalvalue_greatness = finalvalue_greatness.upper()

                    # irá verificar se já existe X dentro das listas de valor, se sim o bota num loop que só quebra quando ele digita um
                    # valor númerico.
                    while True:
                        if (has_x(startvalue_greatness_list) or has_x(finalvalue_greatness_list)) and finalvalue_greatness == 'X':
                            finalvalue_greatness = input('ERRO! incógnita "X" já foi definida, Digite novamente: ')
                            if finalvalue_greatness == 'x':
                                finalvalue_greatness = finalvalue_greatness.upper()
                        else:
                            break
                    break
                if valida_numero(finalvalue_greatness) and finalvalue_greatness != 'X':
                    break
            finalvalue_greatness_list.append(finalvalue_greatness)
        else:
            finalvalue_greatness_list.append(finalvalue_greatness)
        
    # vai pedir do usuário para identificar qual grandeza é o produto, e vai retornar o indice de onde 
    # está o produto na lista de grandezas
    print('Produto é a grandeza na qual as outras grandezas operam em prol. ')
    product = input(f'Quais dessas grandezas {names_greatness_list} é o produto? [DIGITE DA MESMA FORMA] :')

    # retorna -1 para a variavel indice do produto caso o valor de produto não esteja na lista de grandezas
    # CORRIGIR ESTA LINHA, POIS ESTÁ CAUSANDO ERRO.
    try:
        index_of_product = names_greatness_list.index(product)
    except ValueError:
            index_of_product = -1
        
    # se o indice do produto for -1 bota o usuário num loop até que ele digite corretamente o produto
    if index_of_product == -1:
        while True:
            product = input('DIGITE A GRANDEZA CORRETAMENTE: ')
            index_of_product = names_greatness_list.index(product)
            if not index_of_product == -1:
                break

    # vai inverter o valor inicial e final dentro da lsta da grandeza que for o produto
    store_of_startvalue = startvalue_greatness_list[index_of_product]
    startvalue_greatness_list[index_of_product] = finalvalue_greatness_list[index_of_product]
    finalvalue_greatness_list[index_of_product] = store_of_startvalue

    # irá armazenar em qual lista (de iniciais e finais) que está o 'X'
    line_of_x = 'start list' if has_x(startvalue_greatness_list) else 'final list'

    # irá armazenar o indice de X
    index_of_x = startvalue_greatness_list.index('X') if has_x(startvalue_greatness_list) else finalvalue_greatness_list.index('X')

    # lógica do cálculo:
    # se o x estiver na lista de valores iniciais, vai remover o elemento 'X', multiplicar toda a lista inicial e final
    # e por fim vai dividir final por inicial
    if line_of_x == 'start list':
        startvalue_greatness_list.remove('X')

        # coverte as listas para float
        startvalue_greatness_list = [float(value.replace(',', '.')) for value in startvalue_greatness_list]
        finalvalue_greatness_list = [float(value.replace(',', '.')) for value in finalvalue_greatness_list]

        multiplication_startvalues = mult_list(startvalue_greatness_list)
        multiplication_finalvalues = mult_list(finalvalue_greatness_list)
        result = multiplication_finalvalues / multiplication_startvalues
    # se o x estiver na lista de valores finais, vai remover o elemento 'X', multiplicar toda lista final e inicial
    # e por fim vai dividir inicial por final  
    else:
        finalvalue_greatness_list.remove('X')

        # converte as listas para float
        startvalue_greatness_list = [float(value.replace(',', '.')) for value in startvalue_greatness_list]
        finalvalue_greatness_list = [float(value.replace(',', '.')) for value in finalvalue_greatness_list]

        multiplication_finalvalues = mult_list(finalvalue_greatness_list)
        multiplication_startvalues = mult_list(startvalue_greatness_list)
        result = multiplication_startvalues / multiplication_finalvalues

    print(f'O valor de "X" é: {result:.2f} {names_greatness_list[index_of_x]}')
