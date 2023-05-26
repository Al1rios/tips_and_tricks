
import pandas as pd

list1 = ['Tesla', 'Ford','Fiat']
models = ['X','Focus','Doblo']

df = pd.DataFrame(list(zip(list1, models)),
                    index = [1,2,3],
                    columns = ['Brands', 'Models'])

print(df)