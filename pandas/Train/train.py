import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
df = pd.read_csv("pandas/Train/train.csv")

def Sex(k):
  if k=='M':
    return 1
  else:
    return 0
df['Sex']=df['sex'].apply(Sex)
df.drop('sex',axis=1,inplace=True)
def Alone(s):
  if s=='3 persons or less':
    return 0
  else:
    return 1
df['Alone']=df['famsize'].apply(Alone)
df.drop('famsize',axis=1,inplace=True)
def living(d):
  if d=='Urban':
    return 1
  else:
    return 0
df['living']=df['address'].apply(living)
df.drop('address',axis=1,inplace=True)
def Higher(l):
  if l=='yes':
    return 1
  else:
    return 0
df['Higher']=df['higher'].apply(Higher)
df.drop('higher',axis=1,inplace=True)
def FMedu(s):
  if s=='primary education (4th grade)':
    return 1
  elif s=='5th to 9th grade':
    return 2
  elif s=='secondary education':
    return 3
  elif s=='higher education':
    return 4
  else:
    return 0
df['Fedu'] = df['Fedu'].apply(FMedu)
df['Medu'] = df['Medu'].apply(FMedu)
def FMjob(s):
  return s+'*'
df['Fjob'] = df['Fjob'].apply(FMjob)
df[list(pd.get_dummies(df['Fjob']).columns)] = pd.get_dummies(df['Fjob'])
df.drop('Fjob', axis = 1, inplace = True)
df['Mjob'] = df['Mjob'].apply(FMjob)
df[list(pd.get_dummies(df['Mjob']).columns)] = pd.get_dummies(df['Mjob'])
df.drop('Mjob', axis = 1, inplace = True)
def Way(j):
  if j=='less than 15 min.':
    return 0
  elif j=='15 to 30 min.':
    return 1
  elif j=='30 min. to 1 hour':
    return 2
  else:
    return 3 
df['Way']=df['traveltime'].apply(Way)
df.drop('traveltime',axis=1,inplace=True)
def Study(p):
  if p=='less than 2 hours':
    return 0
  elif p=='2 to 5 hours':
    return 1
  elif p=='5 to 10 hours':
    return 2
  else:
    return 3
df['Studytime']=df['studytime'].apply(Study)
df.drop('studytime',axis=1,inplace=True)
def OthReas(s):
  if s == 'other':
    return 'other_reason'
  else:
    return s
df['reason'] = df['reason'].apply(OthReas)
df[list(pd.get_dummies(df['reason']).columns)] = pd.get_dummies(df['reason'])
df.drop('reason', axis = 1, inplace = True)
df.drop('ID',axis=1,inplace=True)
df.drop('guardian', axis = 1, inplace = True)
def School(i):
  if i =='yes':
    return 1
  else:
    return 0
df['School']=df['schoolsup'].apply(School)
df.drop('schoolsup',axis=1,inplace=True)
def Family_Support(j):
  if j=='yes':
    return 1
  else:
    return 0
df['Famsup']=df['famsup'].apply(Family_Support)
df.drop('famsup',axis=1,inplace=True)
def Money(h):
  if h=='no':
    return 1
  else:
    return 0
df['Money']=df['paid'].apply(Money)
df.drop('paid',axis=1,inplace=True)
def Hobby(k):
  if k=='yes':
    return 1
  return 0
df['Activities']=df['activities'].apply(Hobby)
df.drop('activities',axis=1,inplace=True)
def Medicin(k):
  if k=='yes':
    return 1
  return 0
df['Nursery']=df['nursery'].apply(Medicin)
df.drop('nursery',axis=1,inplace=True)
def Net(s):
  if s=='yes':
    return 1
  return 0
df['Internet']=df['internet'].apply(Net)
df.drop('internet',axis=1,inplace=True)
def Family_Relationship(x):
  if x=='good':
    return 4
  elif x=='excellent':
    return 3
  elif x=='normal':
    return 2
  elif x=='bad':
    return 1
  return 0 
df['Famrel']=df['famrel'].apply(Family_Relationship)
df.drop('famrel',axis=1,inplace=True)
def Adventure_Time(o):
  if o=='very high':
    return 4
  elif o=='high':
    return 3
  elif o=='medium':
    return 2
  elif o=='low':
    return 1
  return 0 
df['Freetime']=df['freetime'].apply(Adventure_Time)
df.drop('freetime',axis=1,inplace=True)
def Absence(j):
  if j<=10:
    return 0
  else:
    return 1
df['Absent']=df['absences'].apply(Absence)
df.drop('absences',axis=1,inplace=True)

y = df['result']
X = df.drop('result', axis = 1) 
X_train,X_test,y_train,y_test= train_test_split(X, y, test_size = 0.082)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
classifier = KNeighborsClassifier(n_neighbors = 13)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(accuracy_score(y_test, y_pred) * 100)