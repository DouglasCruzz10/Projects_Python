from regra_de_3_simples import regra_simples
from regra_de_3_composta import regra_de_3_composta


def main():
    msg= '''
[1] - Para regra de 3 simples 
[2] - Para regra de 3 composta
'''
    print(msg)
    try:
        user = int(input('Digite a opção que deseja: '))
    except ValueError:
        while True:
            user = int(input('Errooo!! Digite a opção que deseja: '))
 
    match user:
        case 1:
            regra_simples()
        case 2:
            regra_de_3_composta()
    print('Programa finalizado!!')
main()