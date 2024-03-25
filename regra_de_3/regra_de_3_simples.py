from modules.input_letters import input_letras
import os
def regra_simples():
    
    greatness = []
    great_one = input_letras('Digite a primeira grandeza: ')
    great_two = input_letras('Digite a segunda grandeza: ')

    # Aqui é um pop-up para o usuário confirmar se as grandezas foram inseridas corretamente
    
    pop_up = ['S', 'N']
    confirm = input_letras(f'{great_one}, {great_two}: Deseja confirmar: [S/N]> ').upper()
    while True:
        if confirm not in pop_up:
            confirm = input_letras(f'{great_one}, {great_two}: Deseja confirmar: [S/N]> ').upper()
        else:
            break
    
    # Aqui iremos verificar a confirmação do usuário para dar prosseguimento ao progrma
    while True:
        if confirm == 'S':
            greatss =  [great_one, great_two]
            greatness.append(greatss)
            break
        elif confirm == 'N':
            os.system("cls")
            great_one = input_letras('Digite a primeira grandeza: ')
            great_two = input_letras('Digite a segunda grandeza: ')
            confirm = input_letras(f'{great_one}, {great_two}: Deseja confirmar: [S/N]> ').upper()

    os.system('cls')
    print(f' Grandeza 1: {great_one} \n Grandeza 2: {great_two}')
   
   # Aqui iremos perguntar ao usuário onde o X da regra se localiza 
   # dependendo da resposta do usuário o programa irá solicitar que ele insira os outros valores respectivamente
    msg = '''

    [1]Valor inicial da primeira grandeza = X
    [2]Valor inicial da segunda grandeza = X
    [3]Valor final da primeira grandeza = X
    [4]Valor final da segunda grandeza = X
    '''
    
    print(msg)
    # Aqui é onde pedimos ao usuário para apontar a localização do X
    while True:
        try:
            user = int(input('Digite a opção que deseja: '))
            break
        except ValueError:
            print('Escolha corretamente!! [1:2:3:4]')
    
    # LEGENDA DAS VARIÁVEIS
    '''
    V1G1 = PRIMEIRO VALOR DA PRIMEIRA GRANDEZA
    V1G2 = PRIMEIRO VALOR DA SEGUNDA GRANDEZA
    V2G1 = SEGUNDO VALOR DA PRIMEIRA GRANDEZA
    V2G2 = SEGUNDO VALOR DA SEGUNDA GRANDEZA
    '''
    match user:
        case 1:
            V1G1 = 'X'
            while True:   
                try:
                    V1G2 = int(input('Digite o valor inicial da segunda grandeza: '))
                    V2G1 = int(input('Digite o valor final da primeira grandeza: '))
                    V2G2 = int(input('Digite o valor final da segunda grandeza: '))
                except ValueError:
                    print("Digite apenas números inteiros!")
        case 2:
            V1G2 = 'X'
            while True:
                try:
                    V1G1 = int(input('Digite o valor inicial da primeira grandeza: '))
                    V2G1 = int(input('Digite o valor final da primeira grandeza: '))
                    V2G2 = int(input('Digite o valor final da segunda grandeza: '))
                    break
                except ValueError:
                    print("Digite apenas números inteiros!!")
        case 3:
            V2G1 = 'X'
            while True:
                try:
                    V1G1 = int(input('Digite o valor inicial da primeira grandeza: '))
                    V1G2 = int(input('Digite o valor inicial da segunda grandeza: '))
                    V2G2 = int(input('Digite o valor final da segunda grandeza: '))
                    break
                except ValueError:
                    print("Digite apenas números inteiros")
        case 4:
            V2G2 = 'X'
            while True:
                try:
                    V1G1 = int(input('Digite o valor inicial da primeira grandeza: '))
                    V1G2 = int(input('Digite o valor inicial da segunda grandeza: '))
                    V2G1 = int(input('Digite o valor final da primeira grandeza: '))
                    break
                except ValueError:
                    print("Digite apenas números inteiros!!")
           
    # Pedir pro usuário informar se é a regra é diretamente ou inversamente proporcional.
    while True:
            user = input('Digite se as grandezas são diretamente [D] ou inversamente [I] proporcionais: ').upper()
            if (user == 'D') or (user =='I'):
                break
            elif (user != 'D') or (user != 'I'):
                print("Digite corretamente")
    
    os.system('cls')      
    '''
    [D] - DIRETAMENTE PROPORCIONAL
    [I] - INDIRETAMENTE PROPORCIONAL
    '''
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
        