def valida_numero(string):
    # Remove espaços em branco e remove eventuais .(pontos) da string e depois
    # verifica se possui apenas digitos númericos, se não tiver digitos númericos retorna falso e a função encerra
    if not ((string.replace(' ', '')).replace('.', '')).isdigit(): 
        return False
    try:
        float(string)  # Tenta converter para float, se conseguir significa que o número é valido e retorna Verdadeiro
        return True
    except ValueError: # se algum erro acontecer ao tentar converter para float acontecer retorna Falso, significando que 
        return False   # a string não era válida

# Exemplo de uso:
# entrada = input("Digite um valor: ")
# if valida_numero_simples(entrada):
#     print("A entrada é um número válido.")
# else:
#     print("Digite apenas números!")
