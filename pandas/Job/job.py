import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv("pandas\Job\DataAnalyst.csv")
print(df['Salary Estimate'].value_counts())
def format(n):
  if n!='-1':
    n=n.split()
    n=n[0]
    n=n.split('-')
    n1=int(n[0][1:len(n[0])-1])
    n2=int(n[1][1:len(n[1])-1])
    return (n1+n2)/2
  else:
    return 0 
df['Salary Estimate']=df['Salary Estimate'].apply(format)
print(df['Salary Estimate'])
df.plot(x = 'Salary Estimate', y = 'Rating', kind = 'scatter')
plt.show()
print(df[df['Rating']>=2.5]['Salary Estimate'])
print(df[df['Rating']==5]['Salary Estimate'])
