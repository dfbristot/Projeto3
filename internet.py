"""
Projeto 3
Escreva um programa em Python que colete dados de notícias políticas na
páagina do G1 e os salve em um arquivo no formato html.
Coloque o cóodigo e o arquivo html no seu GitHub.

Daniel Francisco Bristot
08/09/2022 - versão 0.0.1
"""

import requests
print('Iniciando o programa com a abertura da página')
pagina = requests.get('https://g1.globo.com/politica/')
print(pagina.status_code)

with open('G1.html', 'wb') as arquivo:
    for texto in pagina.iter_content(10000):
        arquivo.write(texto)


print('Finalizado o programa...')
