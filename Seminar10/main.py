import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'human', ['human', 'robot']] = 1, 0
data.loc[data['whoAmI'] == 'robot', ['human', 'robot']] = 0, 1
data[['human', 'robot']] = data[['human', 'robot']].astype(int)
data.head(30)