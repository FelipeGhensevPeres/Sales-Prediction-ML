# 🤖 Sales Prediction - Machine Learning

Projeto de Ciência de Dados desenvolvido para prever vendas com base em investimentos em marketing realizados em TV, Rádio e Jornal.

Utilizando técnicas de análise exploratória de dados e Machine Learning para identificar quais canais possuem maior impacto nas vendas e construir modelos capazes de realizar previsões futuras.

---

## 🎯 Problema de negócio

Uma empresa deseja prever suas vendas futuras com base nos investimentos realizados em diferentes canais de publicidade.

O objetivo é responder perguntas como

* Qual canal gera maior impacto nas vendas?
* É possível prever vendas futuras utilizando dados históricos?
* Qual modelo de Machine Learning apresenta melhor desempenho?

---

## 🛠️ Tecnologias utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## 📂 Estrutura do projeto

```text id="wd6x3k"
main.ipynb       -> análise, treinamento e avaliação dos modelos
advertising.csv  -> base histórica de vendas para análise
novos.csv        -> novos dados para previsão
```

---

## 📈 Etapas do projeto

### 🔹 Tratamento e exploração dos dados

* Leitura da base
* Análise de correlação
* Visualização dos relacionamentos entre variáveis
* Interpretação dos dados

---

### 🔹 Modelagem de Machine Learning

Foram utilizados dois modelos de regressão:

* Linear Regression
* Random Forest Regressor

---

### 🔹 Separação dos dados

Os dados foram divididos em:

* treino
* teste

Utilizando `train_test_split`.

---

### 🔹 Avaliação dos modelos

Os modelos foram avaliados utilizando:

* MAE (Mean Absolute Error)
* R² Score

---

## 📊 Resultados obtidos

### 📌 Linear Regression

* MAE: 1.16
* R²: 0.91

---

### 📌 Random Forest

* MAE: 1.01
* R²: 0.94

---

## 🏆 Modelo escolhido

O modelo Random Forest apresentou melhor desempenho geral:

* menor erro médio
* maior capacidade preditiva
* melhor adaptação às relações não lineares

Por esse motivo, foi escolhido como modelo final para previsão de vendas.

---

## 🔍 Principais insights encontrados

### 📌 Investimentos em TV apresentaram maior correlação com as vendas

---

### 📌 Rádio também demonstrou impacto relevante nas vendas

---

### 📌 Jornal apresentou baixa influência nos resultados

---

### 📌 O Random Forest conseguiu capturar melhor os padrões dos dados

---

## 🔮 Previsão com novos dados

O modelo final foi utilizado para prever vendas futuras com novos investimentos em publicidade.

Exemplo de previsões geradas:

```python id="v4mggc"
[ 7.726   9.919  20.2695]
```

* Meu LinkedIn: https://www.linkedin.com/in/felipe-ghensev-peres-7a7427343/
* GitHub: https://github.com/FelipeGhensevPeres
