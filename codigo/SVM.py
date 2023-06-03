# -*- coding: utf-8 -*-
"""
Script: Treinar SVM
Autor: Daniel Lucas Gomes de Oliveira
GitHub: https://github.com/dlgo99
Data de criação: 03/06/2023
Descrição: Treina a classificação da SVM das eleições;
"""

import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Carregar os dados CSV em dataframes separados
fake_news_df = pd.read_csv('../csv/politifact_fake.csv')
real_news_df = pd.read_csv('../csv/politifact_real.csv')

# Adicionar a coluna de classe aos dataframes
fake_news_df['class'] = 0  # 0 para notícias falsas
real_news_df['class'] = 1  # 1 para notícias reais

# Combinar os dataframes em um único dataframe
data = pd.concat([fake_news_df, real_news_df], ignore_index=True)

# Dividir os dados em conjuntos de treinamento e teste
X = data['title']  # Características (títulos das notícias)
y = data['class']  # Classes (0 para falsas, 1 para reais)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vetorizar os títulos das notícias usando TF-IDF
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Treinar o modelo SVM
svm = SVC(kernel='linear')
svm.fit(X_train_vectorized, y_train)

# Fazer previsões com o modelo treinado
y_pred = svm.predict(X_test_vectorized)

# Avaliar o desempenho do modelo
accuracy = accuracy_score(y_test, y_pred)
print("\nAcurácia:", accuracy)
print(classification_report(y_test, y_pred))

# Nome do arquivo de saída
arquivo_saida = '../svm_fakenews.pkl'

# Salvar o modelo SVM em um arquivo .pkl
with open(arquivo_saida, 'wb') as file:
    pickle.dump(svm, file)

# Carregar o modelo SVM treinado a partir do arquivo
with open(arquivo_saida, 'rb') as file:
    svm = pickle.load(file)
