#Python

import string

# Contador de acertos
acertos = 0

# Dicionário de Perguntas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Função para a primeira pergunta
def primeira_pergunta():
    global acertos
    print (perguntas[0]['Pergunta'])
    opcao = (perguntas[0]['Opções'])
    resultado = ('4', 'c', 'C')

    for i, opc in enumerate(opcao):
        letra = string.ascii_uppercase[i]
        print (f'{letra}){opc}')

    resposta = input('Escolha uma opção: ')
    if resposta in resultado:
        acertos += 1
        print ('Acertou!')

    else:
        print ('Errou!')

    print (f'Você acertou {acertos} de 3 até agora!')

# Função para a segunda pergunta
def segunda_pergunta():
    global acertos
    print (perguntas[1]['Pergunta'])
    opcao = (perguntas[1]['Opções'])
    resultado = ('25', 'a', 'A')

    for i, opc in enumerate(opcao):
        letra = string.ascii_uppercase[i]
        print (f'{letra}){opc}')

    resposta = input('Escolha uma opção: ')
    if resposta in resultado:
        acertos += 1
        print ('Acertou!')

    else:
        print ('Errou!')

    print (f'Você acertou {acertos} de 3 até agora!')

# Função para a terceira pergunta
def terceira_pergunta():
    global acertos
    print (perguntas[2]['Pergunta'])
    opcao = (perguntas[2]['Opções'])
    resultado = ('5', 'b', 'B')

    for i, opc in enumerate(opcao):
        letra = string.ascii_uppercase[i]
        print (f'{letra}){opc}')

    resposta = input('Escolha uma opção: ')
    if resposta in resultado:
        acertos += 1
        print ('Acertou!')

    else:
        print ('Errou!')

    print (f'Você acertou {acertos} de 3 até agora!')

# Função para a mensagem final
def mensagem_final():
    if acertos == 3:
        print ('Parabéns você acertou todas as perguntas!')

    elif acertos == 2:
        print ('Que bom! Você acertou duas perguntas, continue a estudar!')

    elif acertos == 2:
        print ('Infelizmente você não acertou nenhuma resposta, mas não desista e estude!')

primeira_pergunta()
segunda_pergunta()
terceira_pergunta()
mensagem_final()
