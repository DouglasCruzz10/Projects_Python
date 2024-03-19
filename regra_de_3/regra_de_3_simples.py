from modules.input_letters import input_letras
from modules.get_input import valida_numero
import os
def regra_simples():
    greatness = []
    values_initial = []
    values_final = []

    great_one = input_letras('Digite a primeira grandeza: ')
    great_two = input_letras('Digite a segunda grandeza: ')

    pop_up = ['S', 'N']
    confirm = input_letras(f'{great_one}, {great_two}: Deseja confirmar: [S/N]> ').upper()
    
    while True:
        if confirm not in pop_up:
            confirm = input_letras(f'{great_one}, {great_two}: Deseja confirmar: [S/N]> ').upper()
        else:
            break
    
    
    while True:
        if confirm == 'S':
            greatss =  [great_one, great_two]
            greatness.append(greatss)
            break
        else:
            great_one = input_letras('Digite a primeira grandeza: ')
            great_two = input_letras('Digite a segunda grandeza: ')
            confirm = input_letras(f'{great_one}, {great_two}: Deseja confirmar: [S/N]> ').upper()
    print(f'Grandeza1: {great_one} \n Grandeza2: {great_two}')
    msg = '''

    [1]Valor inicial da primeira grandeza = X
    [2]Valor inicial da segunda grandeza = X
    [3]Valor final da primeira grandeza = X
    [4]Valor final da segunda grandeza = X
    '''
    print(msg)
    
    try:
        user = int(input('Digite a opção que deseja: '))
    except ValueError:
        user = int(input('erro!! Digite a opção que deseja: '))

    match user:
        case 1:
            V1G1 = 'X'
            V1G2 = int(input('Digite o valor inicial da segunda grandeza: '))
            V2G1 = int(input('Digite o valor final da primeira grandeza: '))
            V2G2 = int(input('Digite o valor final da segunda grandeza: '))
            Value_one = V1G1,V1G2
            Value_two = V2G1,V2G2
            values_initial.append(Value_one)
            values_final.append(Value_two)
    
        case 2:
            V1G1 = int(input('Digite o valor inicial da primeira grandeza: '))
            V1G2 = 'X'
            V2G1 = int(input('Digite o valor final da primeira grandeza: '))
            V2G2 = int(input('Digite o valor final da segunda grandeza: '))
            Value_one = V1G1,V1G2
            Value_two = V2G1,V2G2
            values_initial.append(Value_one)
            values_final.append(Value_two)
        
        case 3:
            V1G1 = int(input('Digite o valor inicial da primeira grandeza: '))
            V1G2 = int(input('Digite o valor inicial da segunda grandeza: '))
            V2G1 = 'X'
            V2G2 = int(input('Digite o valor final da segunda grandeza: '))
            Value_one = V1G1,V1G2
            Value_two = V2G1,V2G2
            values_initial.append(Value_one)
            values_final.append(Value_two)
    
        case 4:
            V1G1 = int(input('Digite o valor inicial da primeira grandeza: '))
            V1G2 = int(input('Digite o valor inicial da segunda grandeza: '))
            V2G1 = int(input('Digite o valor final da primeira grandeza: '))
            V2G2 = 'X'
            Value_one = V1G1,V1G2
            Value_two = V2G1,V2G2
            values_initial.append(Value_one)
            values_final.append(Value_two)
    print(values_initial, values_final)
    
    # Pedir pro usuário informar se é a regra é diretamente ou inversamente proporcional.
    try:
        user = input('Digite se as grandezas são diretamente [D] ou inversamente [I] proporcionais: ').upper()
    except ValueError:
        user = input('Error!! Digite se as grandezas são diretamente [D] ou inversamente [I] proporcionais: ').upper()
    match user:
        case 'D':
            if (V1G1 == 'X'):
                result = (V1G2 * V2G1)/V2G2
                print(f'X = {result:.2f} {great_one}')
            elif (V2G1 == 'X'):
                result = (V1G1 * V2G2)/V1G2
                print(f'X = {result:.2f} {great_one}')
            elif (V1G2 == 'X'):
                result = (V1G1 * V2G2)/V2G1
                print(f'X = {result:.2f} {great_two}')
            elif (V2G2 == 'X') :
                result = (V1G2 * V2G1)/V1G1
                print(f'X = {result:.2f} {great_two}')
    
        case'I':
            if (V1G1 == 'X'):
                result = (V2G1 * V2G2)/V1G2
                print(f'X = {result:.2f} {great_one}')
            elif (V2G1 == 'X'):
                result = (V1G1 * V1G2)/V2G2
                print(f'X = {result:.2f}v{great_one}')
            elif (V1G2 == 'X'):
                result = (V2G1 * V2G2)/V1G1
                print(f'X = {result:.2f} {great_two}')
            elif (V2G2 == 'X') :
                result = (V1G1 * V1G2)/V2G1
                print(f'X = {result:.2f} {great_two}')    
        