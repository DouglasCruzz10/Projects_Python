def input_letras(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isalpha():
            return entrada
        else:
            print("Por favor, insira apenas letras.")

# Exemplo de uso:
# texto = input_letras("Digite apenas letras: ")
# print("Você digitou:", texto)
