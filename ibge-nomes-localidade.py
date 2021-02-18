import requests
import pprint

base = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/"

print("Informe um nome para ver a frequência com que ele aparece no Brasil ao longo dos períodos: ")

# Campo para o informe do nome
nome = str(input("Nome: "))

# Conversão do nome recebido em letras minúsculas
nome = nome.lower()

# Concatenação entre url de base e nome informado
url = base + nome

# Variável dado recebe 
dado = requests.get(url).json()

# Função
def dados(dado):
        # Variável que guarda adiciona a resposta da API em uma lista
        bdados = []

        # Loop que itera sobre a largura do dado recebido
        for i in range(0, len(dado)):
                bdados.append(dado[0])
        return bdados

# Armazenagem do retorno da função dados() em uma variável
bd = dados(dado)
print("=" * 50)
print("Resultado")
print("=" * 50)
pprint.pprint(bd)
