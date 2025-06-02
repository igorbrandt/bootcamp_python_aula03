### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
try:
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    if quantidade > 0 and preco > 0:
        print("Dádos válidos.")
    else:
        print("Dados inválidos.")
except ValueError as e:
    print(f"Erro: {e}")
    
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
while True:
    try:
        temperatura = float(input("Digite a tempertura: "))
    except ValueError:
        print("Digite um valor para a temperatura")
        continue

    if temperatura < 18:
        print("Temperatura baixa")
    elif 18 <= temperatura <= 26:
        print("Temperatura normal")
    else:
        print("Temperatura alta")
    break
    
### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log["level"] == "ERROR":
    print(log["message"])
else:
    pass

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
import re
def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if not 18 <= idade <= 65:
                print("Sua idade deve estar entre 18 e 65 anos.")
                continue
            else:
                return idade
        except ValueError:
            print("Você não digitou uma idade válida.")

def validar_email():
    while True:
        email = input("Digite seu email: ")
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if valid:
            print("Email válido.")
            return email
        else:
            print("Email inválido.")
            continue

idade = validar_idade()
email = validar_email()
print(f"Idade: {idade}, Email: {email}")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
transacoes = [{"valor": 12000, "hora": 20},
            {"valor": 9000, "hora": 18}]
for transacao in transacoes:
    if transacao["valor"] > 10000 or transacao["hora"] < 9 or transacao["hora"] > 18:
        print("Transação suspeita.")
    else:
        print("Transação normal.")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "Fui ao mercado comprar banana, mas não tinha banana no mercado"
novo_texto = texto.replace(",","")
palavras = novo_texto.split(" ")
contagem_palavras = {} 
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
usuarios_incompletos = []
dados_usuarios = [
    {"nome" : "igor", "idade" : "29"},
    {"nome" : "pedro","idade" : "62"},
    {"nome" : "roberto","idade" : ""}
]
for usuario in dados_usuarios:
    if usuario["nome"] == "" or usuario["idade"] == "":
          usuarios_incompletos.append(usuario)
    else:
        pass
print(usuarios_incompletos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = [1, 2, 3, 4, 99, 555, 786, -2, -1, 0]
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(numeros_pares)     

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor
print(total_por_categoria)

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
entrada = ""
while entrada.lower() != 'sair':
    entrada = input("Digite uma palavra. Para encerrar o programa, digite 'sair': ")
    continue

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
n = int(input("Digite um número de 1 a 10: "))

while n not in range(1, 10):
    print("Número fora do intervalo.")
    n = int(input("Tente novamente: "))

print("Número válido.")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
pagina_atual = 1
total_de_paginas = 5

while pagina_atual <= total_de_paginas:
    print(f"Processando página {pagina_atual} de {total_de_paginas}")
    ## código que processa os dados da pagina_atual
    pagina_atual += 1

print("Totas as páginas foram processadas.")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
NUMERO_SECRETO = 2
LIMITE_TENTATIVAS = 3
tentativa = 1

while tentativa <= LIMITE_TENTATIVAS:
    try:
        print(f"Tentativa {tentativa} de {LIMITE_TENTATIVAS}")
        entrada = int(input("Digite o número secreto: "))
        if entrada == NUMERO_SECRETO: # supondo que a conexão foi bem-sucedida
            print("Conectado com sucesso.")
            break
        else: 
            tentativa += 1
            continue
    except ValueError:
        print("Digite um número.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# solução com FOR
lista = [1, 3, 8, 9, "parar", 78, 66, 546]
for i in lista:
    if i == "parar":
        print("'parar' encontrado. Encerrando programa...")
        break
    print(f"Processando item {i}")

# solução com WHILE
lista = [1, 3, 8, 9, "parar", 78, 66, 546]
i = 0
while i < len(lista):
    if lista[i] == "parar":
        print("'parar' encontrado. Encerrando programa...")
        break
    else:
        print(f"Processando item número {i} de {len(lista)}")
        i += 1