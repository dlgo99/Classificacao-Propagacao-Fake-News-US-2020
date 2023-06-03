# -*- coding: utf-8 -*-
"""
Script: Limpar dataset hashtag_donaldtrump.csv
Autor: Daniel Lucas Gomes de Oliveira
GitHub: https://github.com/dlgo99
Data de criação: 03/06/2023
Descrição: Deixa o dataset formatado par ao funcionamento correto do código.
"""

# Nome do arquivo de entrada e saída
arquivo_entrada = '../csv/hashtag_donaldtrump.csv'
arquivo_saida = '../csv/hashtag_donaldtrump_limpada.csv'

# Abrir o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(arquivo_entrada, 'r', encoding='utf-8') as file_in, open(arquivo_saida, 'w', encoding='utf-8') as file_out:
    # Escrever o cabeçalho no arquivo de saída
    file_out.write('user_id,tweet,likes\n')

    # Ler cada linha do arquivo de entrada
    for linha in file_in:
        # Verificar se a linha contém 21 vírgulas e começa com "created_at" ou "2020"
        if linha.count(',') == 20 and (linha.startswith('created_at') or linha.startswith('2020')):
            # Separar os campos da linha em uma lista
            campos = linha.split(',')

            # Verificar se o user_id não contém o caractere "+"
            if '+' not in campos[6]:
                # Remover o ".0" dos user_id
                user_id = campos[6].replace('.0', '').strip()

                # Verificar se o user_id é um número válido
                if user_id.isdigit():
                    # Modificar o campo do user_id na lista
                    campos[6] = user_id

                    # Remover o ".0" do campo likes
                    campos[3] = campos[3].replace('.0', '').strip()
                    if not campos[3].isdigit() and not campos[3] == 'likes':
                        # Atribuir 0 se não for possível converter
                        campos[3] = '0'

                    # Salvar apenas as tags "user_id", "tweet" e "likes" no arquivo de saída
                    tags = ','.join([campos[6], campos[2], campos[3]])  # user_id, tweet, likes
                    file_out.write(tags + '\n')

import pandas as pd

# Name of the input and output files
arquivo_entrada = '../csv/hashtag_donaldtrump_tratada.csv'
arquivo_saida = '../csv/teste.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(arquivo_entrada)

# Sort the DataFrame by the "likes" column in descending order
df_sorted = df.sort_values(by='likes', ascending=False)

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv(arquivo_saida, index=False)