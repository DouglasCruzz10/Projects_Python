from funct.input_number import input_numbers
from funct.input_letters import input_letras
def regra_simples():
    greatness = []
    initial_value = []
    final_value = []
    
    great_one =input_letras('Digite a primeira grandeza: ')
    great_two = input_letras('Digite a segunda grandeza: ')
    pop_up = input_letras(f'{great_one}{great_two} = ','Você confirmas estas grandezas ?: [S/N]').upper()
    while True:
        if pop_up == 'S':
            greatness.append(great_one,great_two)
            break      
        else:
            print('Digite Novamente')

regra_simples()