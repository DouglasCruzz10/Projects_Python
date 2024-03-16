from modules.get_input import valida_numero

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

    for i in range(0, greatness_qtd_int):
        print(f'Digite o nome da {i+1}º grandeza:', end=' ')
        names_greatness_list.append(input())
    print(names_greatness_list)
regra_de_3_composta()