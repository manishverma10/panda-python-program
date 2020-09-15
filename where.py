import pandas as pd 
  
idx1 = pd.Index([900, 45, 21, 145, 38, 422]) 
idx2 = pd.Index([1100, 1200, 1300, 1400, 1500, 1600]) 
  

# result = idx1.where(idx1 < 100, idx2) 
result = idx1.where((idx2 - 1200) < idx1, idx2)
print(result) 