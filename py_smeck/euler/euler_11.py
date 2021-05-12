import pandas as pd

data = pd.read_csv('euler_11_grid.csv', header=None)

# calculate horizontal products
for i in range(1,20):
    df = data[i:i+4]
    prod = (df.Series([]).prod())


# calculate vertical products
for i in range(1,20):
    df = data[i:i+4]
    print(df)

# calculate diagogal products
for i in range(1,20):
    df = data[i:i+4]
    print(df)
