import pandas as pd
import matplotlib.pyplot as plt
dict={'date':['30-1-20','5-8-12','12-4-12','12-5-20'],
'price':[1000,20,52,8000],
'product_id':[101,102,103,104],
'quantity_purchased':[20,10,1,3],
'serial_no':[1,8,6,9],
'usr_id':[11,22,33,44],
'usr_type':['a','b','c','d'],
'usr_class':['upr','mid','low','mid'],
'pur_week':['mon','wed','tue','fri']}
df=pd.DataFrame(dict)
df.to_csv("df.csv")
df.head()
print(df)
stats=df.describe(include='all')
print(stats)
df.plot(x='usr_id',y='price',kind='line')
plt.show()
df[['quantity_purchased','pur_week']].plot.box()
plt.title('quantity and week value distribution')
plt.show()
