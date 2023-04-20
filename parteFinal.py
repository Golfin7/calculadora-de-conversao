# Lista de unidades de medida
unidades = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

# Função que converte uma quantidade de uma unidade para outra
def converter(quantidade, unidade_origem, unidade_destino):
    fatores = {
        "bit": 1,
        "byte": 8,
        "KB": 8000,
        "MB": 8000000,
        "GB": 8000000000,
        "TB": 8000000000000,
        "PB": 8000000000000000
    }
    fator_origem = fatores[unidade_origem]
    fator_destino = fatores[unidade_destino]
    quantidade_bits = quantidade * fator_origem
    quantidade_destino = quantidade_bits / fator_destino
    return quantidade_destino

# Função para entrada de dados pelo usuário
def obter_dados():
    quantidade = float(input("Digite a quantidade a ser convertida: "))
    print("Unidades disponíveis:")
    for i, unidade in enumerate(unidades):
        print(f"{i + 1}. {unidade}")
    index_origem = int(input("Digite o número da unidade de origem: ")) - 1
    index_destino = int(input("Digite o número da unidade de destino: ")) - 1
    return quantidade, unidades[index_origem], unidades[index_destino]

# Exemplo de uso da função
quantidade, unidade_origem, unidade_destino = obter_dados()

while unidade_origem != unidade_destino:
    quantidade = converter(quantidade, unidade_origem, unidade_destino)
    index_origem = unidades.index(unidade_origem)
    index_destino = unidades.index(unidade_destino)
    if index_origem < index_destino:
        unidade_origem = unidades[index_origem + 1]
    else:
        unidade_origem = unidades[index_origem - 1]

print(f"{quantidade:.2f} {unidade_destino}")

