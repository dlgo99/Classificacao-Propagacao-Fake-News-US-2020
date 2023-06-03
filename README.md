# Código para classificação e propagação de fake news nas eleições dos Estados Unidos de 2020.

---

## Como executar
* Execute o arquivo limpar.py (Trata o .csv das hashtag donald trupo)
* Altere o nome do arquivo gerado de hashtag_donaldtrump_limpada.csv para hashtag_donaldtrump_tratada.csv
* Elimine manualmente linhas mal formatadas
* Execute o arquivo grafo.py
* O arquivo sempre analisará os mesmos 2 tweets, altere conforme quiser em grafo.py

---

O SVM treinado obteve uma precisão média de 85\% de acerto dentre os tweets utilizados para fazer o treinamento, o treinamento foi feito pelo conteúdo do tweet e classificado de acordo se esse tweet estava no arquivo de notícias verdadeiras ou notícias falsas.

Para os dois usuários selecionados, um foi classificado como tendo feito um tweet com notícia verdadeira, nó em verde, e o outro usuário como tendo feito um tweet com notícia falsa, nó em vermelho. Para esses usuários analisou-se os seus amigos, e cada um de seus amigos também tiveram os amigos analisados, formando então uma grande rede conexa.

Ao todo a rede teve 1856 nós, e ao analisar o efeito de cascata dos nós que fizeram o tweet, percebe-se que cada um deles consegue alcançar as outras 1855 pessoas pertencentes e este grafo, mostrando que mesmo em uma grande rede com milhares de pessoas, é possível que uma notícia se propague muito facilmente, em menos de 10 saltos entre os amigos qualquer notícia chega a outra pessoa neste grafo.

![Grafo](grafso.png)

---

## Fonte dos datasets
* [SVM](https://github.com/KaiDMML/FakeNewsNet)
* [US Election 2020 Tweets](https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets?select=hashtag_donaldtrump.csv)
* [Twitter Friends](https://www.kaggle.com/datasets/hwassner/TwitterFriends)

---
