import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url).json()

    if f"{moeda}BRL" not in resposta:
        print("Moeda inválida ou não encontrada.")
    else:
        dados = resposta[f"{moeda}BRL"]
        print("Moeda:", dados["name"])
        print("Valor atual:", dados["bid"])
        print("Valor máximo:", dados["high"])
        print("Valor mínimo:", dados["low"])
        print("Última atualização:", dados["create_date"])

# Exemplo de uso
codigo = input("Digite o código da moeda (ex: USD, EUR): ")
consultar_cotacao(codigo)
