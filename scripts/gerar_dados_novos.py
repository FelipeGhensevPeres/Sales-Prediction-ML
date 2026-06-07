import pandas as pd
import numpy as np

np.random.seed(42)

novos = pd.DataFrame({'TV': np.random.uniform(0,300,100),
                      'Radio': np.random.uniform(0,50,100),
                      'Jornal': np.random.uniform(0,120,100)})


novos = novos.round(1)



novos.to_csv(r'data/novos_gerados.csv',index=False)


