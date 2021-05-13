import pandas as pd

data = pd.read_csv('euler_11_grid.csv', header=None)

# calculate horizontal products
n = 0
for i in range(1,18):
    subset = data.iloc[[0], [0+n, 1+n, 2+n, 3+n]]
    print(subset)
    prod = subset.product()
    prod = subset[0] * subset[1] * subset[2] * subset[3]
    n += 1
    print(prod)
    # prod = (df.Series([]).prod())

#
# # calculate vertical products
# for i in range(1,20):
#     df = data[i:i+4]
#     print(df)
#
# # calculate diagogal products
# for i in range(1,20):
#     df = data[i:i+4]
#     print(df)
