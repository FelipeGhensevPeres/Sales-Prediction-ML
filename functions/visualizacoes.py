import matplotlib.pyplot as plt



def plot_previsoes(y_real,
                     y_pred,
                     titulo):
    
    """"
    Exibe um gráfico de dispersão comparando
    valores reais e previstos.
    """
    
    plt.figure(figsize=(15, 6))

    plt.scatter(
        y_real,
        y_pred,
        alpha=0.6,
        s=100,
        color='blue',
        label='Previsões'
    )

    plt.plot(
        [y_real.min(), y_real.max()],
        [y_real.min(), y_real.max()],
        'r--',
        lw=2,
        label='Valor Real'
    )

    plt.xlabel('Vendas Reais (milhões)', fontsize=14)
    plt.ylabel('Vendas Previstas (milhões)', fontsize=14)
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()
    
    

def plot_comparacao(y_real,
                    pred_1,
                    pred_2,
                    label_modelo1:str,
                    label_modelo2:str):
    
    """
    Compara visualmente as previsões de dois modelos
    em relação aos valores reais.
    """
    
    plt.figure(figsize=(15,6))
    
    
    plt.scatter(y_real,
                pred_1,
                alpha=0.6,
                s=80,
                label=label_modelo1)
    
    
    plt.scatter(y_real,
                pred_2,
                alpha=0.6,
                s=80,
                label=label_modelo2)
    
    
    plt.plot([y_real.min(),y_real.max()],
             [y_real.min(),y_real.max()],
             '--',
             lw=2,
             label='Valor Real')
    
    
    plt.xlabel('Vendas Reais', fontsize=14)
    plt.ylabel('Previsões', fontsize=14)
    plt.title('Comparação de Modelos: Previsões vs Valores Reais', fontsize=16, fontweight='bold')
    plt.legend(fontsize=10)
    plt.show()