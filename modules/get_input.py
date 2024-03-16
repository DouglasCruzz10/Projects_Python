def valida_numero_simples(string):
    # Remove espaços em branco e verifica se contém apenas dígitos
    if not string.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():
        return False
    try:
        float(string)  # Tenta converter para float
        return True
    except ValueError:
        return False

# Exemplo de uso:
# entrada = input("Digite um valor: ")
# if valida_numero_simples(entrada):
#     print("A entrada é um número válido.")
# else:
#     print("Digite apenas números!")
