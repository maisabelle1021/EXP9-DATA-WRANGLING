import pandas as pd
bears1 = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
bears2 = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
bears3 = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
bears4 = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}

df1 = pd.DataFrame(bears1,columns=['Student','Math'])
df2 = pd.DataFrame(bears2,columns=['Student','Electronics'])
df3 = pd.DataFrame(bears3,columns=['Student','GEAS'])
df4 = pd.DataFrame(bears4,columns=['Student','ESAT'])

data = pd.merge(df1,df2, how='right',on='Student')
data2 = pd.merge(data,df3, how='right', on='Student')
data3 = pd.merge(data2,df4, how='right', on='Student')

x = pd.melt(data3, id_vars='Student',value_vars=['Math','Electronics','GEAS','ESAT'])
m = x.rename(columns={'variable':'Subject','value':'Grades'})
n = m.sort_values('Student')
o = n.reset_index()
p = o.drop(columns='index')
