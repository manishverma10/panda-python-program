import pandas as pd
import numpy as np

df = pd.DataFrame([['dog', True, 5],
                   ['cat', False, 1]],
                  columns=['animal', 'bark', 'age'])

df.head()

# np.where(df['animal'] > 2, True, False)

df['hasError']= np.where(df['age'] > 2, 'True', 'False' )
df.head()

print df