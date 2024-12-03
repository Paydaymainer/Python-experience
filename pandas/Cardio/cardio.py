import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
#import libraries we will use


heart_failure_data = pd.read_csv("pandas\Cardio\heart_failure_clinical_records_dataset.csv")#process the file using pandas
print(heart_failure_data.head())#display the first and last columns

agg_data = heart_failure_data.groupby(['age', 'DEATH_EVENT'], as_index=False).ejection_fraction.count()#grouping by age, show the number of deaths at a given age, counting the number of participants with this age
agg_data.columns = ['Age', 'Death_Event', 'Count']#name columns
print(agg_data.head())#output

sns.relplot(x="Age", y="Count", hue="Death_Event" , aspect=16/9, kind="line", data=agg_data); #making same but with seaborn, using agg_data
sns.relplot(x="serum_creatinine", y="ejection_fraction", hue="DEATH_EVENT", kind="scatter", style="smoking", data=heart_failure_data, aspect=16/9); 
agg_data2 = heart_failure_data.groupby(['age', 'ejection_fraction'], as_index=False).DEATH_EVENT.sum()
agg_data2.columns = ['Age', 'ejection_fraction', 'Deaths'] 
agg_data2_p = agg_data2.pivot(index='Age', columns='ejection_fraction', values='Deaths') #Create another variable for the new visualization of seaborn
agg_data2_p.fillna(0, inplace=True)
agg_data2_p.head(20)
plt.subplots(figsize=(20,15))
sns.heatmap(agg_data2_p, annot=True) #We use a heat map to reflect the data, the color shows the number
plt.show()

X = heart_failure_data.drop('DEATH_EVENT', axis = 1) #using sklearn 
y = heart_failure_data['DEATH_EVENT'] #Х - dataset, but without results,but Y on the contrary, the results column itself
X_train,X_test,y_train,y_test= train_test_split(X, y, test_size = 0.1)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
classifier = KNeighborsClassifier(n_neighbors =15) #choosing number of neighbours
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test) #predict
print(accuracy_score(y_test, y_pred) * 100) #output of percent of acuracy