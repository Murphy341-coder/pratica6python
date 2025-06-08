import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url).json()

    if "erro" in resposta:
        print("CEP inválido.")
    else:
        print("Logradouro:", resposta['logradouro'])
        print("Bairro:", resposta['bairro'])
        print("Cidade:", resposta['localidade'])
        print("Estado:", resposta['uf'])

# Exemplo de uso
cep = input("Digite o CEP (somente números): ")
consultar_cep(cep)
