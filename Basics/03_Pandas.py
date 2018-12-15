import urllib
import pandas as pd

url = "https://raw.githubusercontent.com/GokuMohandas/practicalAI/master/data/titanic.csv"
response = urllib.request.urlopen(url)
html = response.read()
with open('titanic.csv', 'wb') as f:
    f.write(html)


df = pd.read_csv("titanic.csv", header=0)

df.head()

df.describe()

df["age"].hist()


