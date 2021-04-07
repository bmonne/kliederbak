import pandas as pd

data = pd.read_csv('euler_11_grid.csv', header=None)

for i in range(1,20):
    df = data[i:i+4]
    print(df)


