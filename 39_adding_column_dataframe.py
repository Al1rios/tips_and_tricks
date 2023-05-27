
import pandas as pd

list1 = ['Tesla','Ford','Fiat']

models = ['X', 'Focus', 'Doblo']

df = pd.DataFrame(list(zip(list1, models)),
                  index=[1,2,3],
                  columns=['Brands','Models']
                )

df['Age'] = [2,4,3]

print(df)

df.drop('Models', inplace=True, axis=1)

print(df)