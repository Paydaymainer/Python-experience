import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("pandas/Coastline/countries_of_the_world.csv")
df=df.dropna()
def Coast(n):
    n = n.replace(',','.')
    n = float(n)
    if n>0:
        return True
    else:
        return False
df['Coastline (coast/area ratio)'] = df['Coastline (coast/area ratio)'].apply(Coast)
def Agro(n):
  n=str(n)
  if n=='nan':
    return n
  else:
    n = n.replace(',','.')
    n = float(n)
    n*=10
    return n
df['Agriculture']=df['Agriculture'].apply(Agro)
print(df[df['Coastline (coast/area ratio)']==True]['Agriculture'].mean())
print(df.groupby(by='Coastline (coast/area ratio)')['GDP ($ per capita)'].agg(['min','max','mean']))
df.plot(x = 'Agriculture', y = 'GDP ($ per capita)', kind = 'scatter')
plt.show()
df['Infant mortality (per 1000 births)']
df.plot(x = 'Infant mortality (per 1000 births)', y = 'Pop. Density (per sq. mi.)', kind = 'scatter')
plt.show()
