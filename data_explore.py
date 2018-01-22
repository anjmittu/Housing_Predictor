# data analysis and wrangling
import pandas as pd
import data_cleanup as dc
import seaborn as sns

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

train = train.drop(["Id"], axis=1)
train.head()
train.describe()

#Looksing at the categorical vars
var = ["MSSubClass", "MSZoning", "Street", "Alley", "LotShape", "LandContour"]
for v in var:
    data = pd.concat([train['SalePrice'], train[v]], axis=1)
    f, ax = plt.subplots(figsize=(8, 6))
    fig = sns.boxplot(x=v, y="SalePrice", data=data)
    fig.axis(ymin=0, ymax=800000);
    print(train[[v, 'SalePrice']].groupby([v], as_index=False).mean().sort_values(by='SalePrice', ascending=False))


grid = sns.FacetGrid(train, col='Survived', row='CabinLetter', size=2.2, aspect=1.6)
grid.map(plt.hist, 'Fare', alpha=.5, bins=20)
grid.add_legend();


train.head()
