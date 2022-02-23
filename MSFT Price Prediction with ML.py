# End to End Machine Learning Project 3
import numpy as np# we import this package for data array manipulation
import pandas as pd# we import this package for large data array manipulation
import matplotlib.pyplot as plt # we import this package for data visualisation
import seaborn as sns # we import this package for data visualisation
import sklearn



sns.set()
plt.style.use('seaborn-dark-palette')


######################### MSFT Stock Movemenet ######################

data = pd.read_csv('MSFT_ 1Y.csv')
print(data.head())

#plt.figure(figsize=(10,4))
#plt.title('MICROSOFT STOCK PRICES')
#plt.xlabel('Date')
#plt.ylabel('Close')
#plt.plot(data['Close'])
#plt.show()

######################### Correlation of the data set######################
#print(data.corr())
#sns.heatmap(data.corr())
#plt.show()



######################### dataset cleaning & training #########################



x = data[['Open','High','Low']]
y = data['Close']
x = x.to_numpy()
y = y.to_numpy()
y= y.reshape(-1,1)


from sklearn.model_selection import train_test_split
xtrain,xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
data = pd.DataFrame(data={'Predicted Rate': ypred})
print(data.head())


