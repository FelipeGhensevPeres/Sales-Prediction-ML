# 📈 Sales Prediction with Machine Learning

Projeto de Machine Learning para previsão de vendas com base em investimentos realizados em diferentes canais de publicidade.

O objetivo foi identificar quais canais de marketing possuem maior impacto nas vendas e desenvolver um modelo capaz de prever resultados futuros a partir dos investimentos em TV, Rádio e Jornal.

---

# 🎯 Problema de Negócio

A empresa realiza investimentos em diferentes meios de comunicação e precisava responder algumas perguntas estratégicas:

* Qual canal de marketing possui maior influência nas vendas?
* É possível prever as vendas futuras com base nos investimentos realizados?
* Qual modelo de Machine Learning apresenta melhor desempenho para esse problema?
* Como otimizar a distribuição do orçamento de marketing?

As vendas presentes na base de dados são representadas em milhões.

---

# 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git
* GitHub

---

# 📂 Estrutura do Projeto

```text
Sales-Prediction-ML/
│
├── data/
│   ├── advertising.csv
│   ├── novos.csv
│   └── novos_gerados.csv
│
├── functions/
│   ├── __init__.py
│   ├── avaliacoes.py
│   └── visualizacoes.py
│
├── notebooks/
│   └── main.ipynb
│
├── scripts/
│   └── gerar_dados_novos.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Responsabilidade dos módulos

### avaliacoes.py

* Funções reutilizáveis para avaliação dos modelos
* Cálculo de métricas de desempenho
* Padronização da apresentação dos resultados

### visualizacoes.py

* Funções reutilizáveis para geração de gráficos
* Comparação entre valores reais e previstos
* Comparação entre modelos de Machine Learning

### gerar_dados_novos.py

* Geração de novos cenários de investimento
* Criação de dados para realização de previsões futuras

---

# 📈 Etapas da Análise

## 🔹 Análise Exploratória

Realizei uma análise de correlação entre as variáveis para identificar quais investimentos apresentam maior relação com as vendas.

Os resultados mostraram:

* TV possui a maior correlação com as vendas
* Rádio apresenta influência moderada
* Jornal possui baixa correlação

---

## 🔹 Treinamento dos Modelos

Foram utilizados dois algoritmos de regressão:

### Linear Regression

Utilizado como modelo baseline pois é simples e fácil de interpretar.

### Random Forest Regressor

Escolhido pela capacidade de capturar relações não lineares e interações mais complexas entre as variáveis.

---

## 🔹 Avaliação dos Modelos

Os modelos foram avaliados usando:

* MAE (Mean Absolute Error)
* R² Score

O Random Forest teve melhor desempenho em ambas as métricas.

---

# 📊 Importância das Variáveis

A análise de Feature Importance do Random Forest mostrou:

| Variável | Importância |
| -------- | ----------- |
| TV       | 85%         |
| Rádio    | 13%         |
| Jornal   | 2%          |

Os investimentos em TV são os principais responsáveis pelas previsões realizadas pelo modelo.

---

# 🔍 Principais Insights

## 📺 TV

O investimento em TV apresentou o maior impacto nas vendas, sendo o principal fator considerado pelo modelo.

## 📻 Rádio

Os investimentos em rádio também contribuíram para as previsões, porém com influência significativamente menor que a TV.

## 📰 Jornal

O investimento em jornal apresentou baixa relevância para a previsão das vendas.

---

# 🤖 Modelo Final

Após a comparação entre os modelos, o Random Forest foi selecionado como modelo final.

* Menor erro médio (MAE)
* Maior capacidade explicativa (R²)
* Melhor desempenho geral nas previsões

---

# 📈 Previsão de Novos Cenários

Gerei um codigo como novo cenário de investimento para simular previsões futuras.

O modelo foi utilizado para estimar as vendas esperadas para cada combinação de investimentos em TV, Rádio e Jornal.

Os resultados reforçaram a importância dos investimentos em TV como principal impulsionador das vendas.

---

# 💡 Conclusões

Com base na análise realizada, foi possível concluir que:

* Os investimentos em TV possuem o maior impacto sobre as vendas
* Rádio apresenta influência complementar
* Jornal possui baixa relevância para o problema analisado
* O modelo Random Forest apresentou melhor desempenho que a Regressão Linear
