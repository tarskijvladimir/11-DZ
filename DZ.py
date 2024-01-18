import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot вид
one_hot = pd.get_dummies(data['whoAmI'])
data = data.drop('whoAmI', axis=1)
data = data.join(one_hot)
data.head()
