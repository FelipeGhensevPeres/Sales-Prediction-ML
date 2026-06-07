import pandas as pd
from sklearn.metrics import mean_absolute_error,r2_score

def avaliar_modelo(nome_modelo:str,
                   y_teste,
                   pred):
    
    mae_modelo = mean_absolute_error(y_true=y_teste,
                                     y_pred=pred)
    
    r2_modelo = r2_score(y_true=y_teste,
                         y_pred=pred)
    
    
    dataframe_avaliacao = pd.DataFrame({'Modelo': [nome_modelo],
                  'MAE': [round(mae_modelo,2)],
                  'R²': [round(r2_modelo,2)]
                  })
    
    return dataframe_avaliacao