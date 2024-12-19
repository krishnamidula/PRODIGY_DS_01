#histogram plot for categorical data 1:country name
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\KRISHNAMIDULA K\\OneDrive\\task 1\\task1.csv")
df=pd.DataFrame(data)
count1=df['CountryName'].value_counts()
print(count1)
plt.figure(figsize=(10,6))
sns.histplot(df['CountryName'],bins=5,kde=True,color='purple')
plt.xlabel('CountryName')
plt.ylabel('Frequency')
plt.title('Histogram of CountryName')
plt.show()

#data visualization of categorical data 2: indicator code

import seaborn as sns
import pandas as pd

data=pd.read_csv('C:\\Users\\KRISHNAMIDULA K\\OneDrive\\task 1\\task1.csv')
df=pd.DataFrame(data)
count2=df['CountryCode'].value_counts()
print(count2)
#plotting

sns.histplot(x=df['CountryCode'],bins=8,kde=True,color='red')
plt.xlabel('CountryrCode')
plt.ylabel('frequency')
plt.title('barplot for indicatorcode')
plt.show()


