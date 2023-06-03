# -*- coding: utf-8 -*-
"""
Script: Gerar Grafo de propagação.
Autor: Daniel Lucas Gomes de Oliveira
GitHub: https://github.com/dlgo99
Data de criação: 03/06/2023
Descrição: Gera Grafo dos dois usuários que fizeram os tweets, e depois classifica.
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import csv
import SVM as classificador

# cria o grafo
G = nx.Graph()

# carrega os dados do CSV com os tweets a serem analisados
with open('../csv/hashtag_donaldtrump_tratada.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader][:50000]  # seleciona as primeiras 50 linhas

users = []
tweets = []
user_friends = []

for row in rows:
    users.append(row['user_id'])
    tweets.append(row['tweet'])

users = ['706668452', '52404615', '2729019485', '18845255', '134838620', '2167158764']
users = ['706668452', '52404615']
for user in users:
        target_id = user
        position = users.index(target_id)
        prediction = classificador.svm.predict(classificador.vectorizer.transform([tweets[position]]))
        # Interpretar o resultado
        if prediction[0] == 0: # fake
            G.add_node(user, color='red')
            print(f"Nó {user}: fake")
        else: # real
            G.add_node(user, color='green')
            print(f"Nó {user}: real")
print()

# carrega os dados do CSV de amigos
with open('../csv/data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader][2000:3000]  # seleciona as primeiras x linhas

for row in rows:
    user_id = row['id']
    if user_id in users:
        amigos = (str(row)[int((str(row).index('\'friends\': ')))+12:].replace('None: [', '').replace(' ', '').replace('\'', '').replace('"', '').replace(']}', ''))
        amigos =  str(amigos)[int((str(amigos).index('['))):].strip().split(',')

        for amigo in amigos:
            user_friends.append(amigo)
            G.add_node(amigo, color='blue')
            G.add_edge(user_id, amigo)

# adiciona as arestas ao grafo
for row in rows:
    amigos = (str(row)[int((str(row).index('\'friends\': ')))+12:].replace('None: [', '').replace(' ', '').replace('\'', '').replace('"', '').replace(']}', ''))
    amigos =  str(amigos)[int((str(amigos).index('['))):].strip().split(',')

    user_id = row['id']
    for amigo in amigos:
        if amigo in G:
            G.add_edge(user_id, amigo)

# define a posição dos vértices
pos = nx.spring_layout(G)

# desenha o grafo
nx.draw_networkx_nodes(G, pos, node_size=50, node_color=[G.nodes[n].get('color', 'blue') for n in G.nodes()])
nx.draw_networkx_edges(G, pos, width=0.2, edge_color='gray')
plt.axis('off')

# # calcula as métricas de centralidade
degree = nx.degree_centrality(G)
closeness = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)

print(f"Degree do nó '{users[0]}': {degree[users[0]]}")
print(f"Closeness do nó '{users[0]}': {closeness[users[0]]}")
print(f"Betweenness do nó '{users[0]}': {betweenness[users[0]]}")
print()
print(f"Degree do nó '{users[1]}': {degree[users[1]]}")
print(f"Closeness do nó '{users[1]}': {closeness[users[1]]}")
print(f"Betweenness do nó '{users[1]}': {betweenness[users[1]]}")

# Detecção de comunidades
communities = nx.algorithms.community.greedy_modularity_communities(G)
print("\nComunidades:")
for i, community in enumerate(communities):
    print(f"Comunidade {i + 1}: {len(community)}")

# Cascata de um nó aleatório
channel_name = random.choice(list(G.nodes))
cascade1 = nx.descendants(G, users[0])
cascade2 = nx.descendants(G, users[1])
print('\nCascatas:')
print(f"Alcance do nó '{users[0]}': {len(cascade1)}")
print(f"Alcance do nó '{users[1]}': {len(cascade2)}")
print()

# exibe o grafo
plt.show()
