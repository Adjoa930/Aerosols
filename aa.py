import numpy as np
import xarray as xr
import pandas as pd
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#import datasets
df1 = xr.open_dataset('aqua.nc')
df2 = xr.open_dataset('terra.nc')
aqua = df1['AOD_550_Dark_Target_Deep_Blue_Combined_Mean_Mean']
terra = df2['AOD_550_Dark_Target_Deep_Blue_Combined_Mean_Mean']

#select area of interest
#fig = plt.figure(figsize=(12,10))
West_Africa = aqua.sel(time=slice('2003-01','2019-12')).sel(lon=np.arange(-25,20,0.5),lat=np.arange(0, 25, 0.5),method= 'nearest').mean(dim=('lon', 'lat'))
#West_Africa.plot()

#selecting the time and values from the dataset
#x_time = West_Africa.time.values
#y_value = West_Africa.values 

#print(x_time)

#West_Afr = pd.concat([x_time, y_value],axis = 1)
#West.columns = ['Month', 'AOD']
x = West_Africa.to_dataframe()
#print(x)
y = x.reset_index()
y.columns = ['Date','AOD']
#print(y)



#deseasonalising the datasets
deseason = x-x.shift()
#print(deseason)

#removing missing values
WA = deseason.dropna()
#print(WA)

West = WA.reset_index()
West.columns = ['Date','AOD']
#print(West)

x_t = np.array(pd.to_datetime(West['Date']).index.values,dtype = float)
y_val = np.array(West['AOD'].values, dtype = float)



#reshaping the datasets
xx = x_t.reshape(-1,1)

yy = y_val.reshape(-1,1)






#print(xx.shape, yy.shape)


#plotting the series
#plt.scatter(xx,yy)
#plt.show()


#training the datasets
x_train,x_test,y_train,y_test = train_test_split(xx,yy,test_size=0.2)

#linear regression
model = LinearRegression()
model.fit(x_train,y_train)

#predicting 
y_pred = model.predict(x_test)
acc = model.score(x_test, y_pred)
print(acc)
print(model.coef_)
print(model.intercept_)



