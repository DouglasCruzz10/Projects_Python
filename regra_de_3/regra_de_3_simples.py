from modules.input_letters import input_letras
from modules.get_input import valida_numero

def regra_simples():
    greatness = []
    initial_value = []
    final_value = []

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
            greatness.append(great_one,great_two)
            break
        else:
            great_one = input_letras('Digite a primeira grandeza: ')
            great_two = input_letras('Digite a segunda grandeza: ')
            confirm = input_letras(f'{great_one}, {great_two}: Deseja confirmar: [S/N]> ').upper()

            

                
    
    
    
regra_simples()



        