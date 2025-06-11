#Python

import string

# Contador de acertos
acertos = 0

# Dicionário de Perguntas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': ('4', 'c', 'C')
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': ('25', 'a', 'A')
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': ('5', 'c', 'C')
    },
]

for pergunta in perguntas:
    print ('Pergunta:', pergunta ['Pergunta'])
    print ()

    for i, opcao in enumerate(pergunta['Opções']):
        letra = string.ascii_uppercase[i]
        print (f'{letra}) {opcao}')
    print()

    escolha = input ('Escolha uma opção: ')
    if escolha in pergunta ['Resposta']:
        acertos += 1
        print ('Acertou!')
        print()

    else:
        print ('Errou!')
        print()

if acertos >= 2:
    print (f'Parabéns você acertou {acertos} perguntas!')

elif acertos == 1:
    print (f'Você acertou apenas {acertos} pergunta.')

else:
    print ('Você não acertou nenhuma pergunta.')
