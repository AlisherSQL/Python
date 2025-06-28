import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

1.Rename column names using function. "First Name" --> "first_name", "Age" --> "age"

df.rename(columns={'First Name':'first_name','Age':'age'},inplace=True)
df

2.Print the first 3 rows of the DataFrame

df.head(3)

3.Find the mean age of the individuals

age= df['age'].mean()
print(age)

4.Select and print only the 'Name' and 'City' columns

df[['first_name','City']]

5.Add a new column 'Salary' with random salary values

import numpy as np
df['Salary']=np.random.randint(10,100, size=len(df))

6.Display summary statistics of the DataFrame

df.describe()


Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses',
 representing monthly sales and 
expenses data. Use below table.

   import pandas as pd

data={
    'Month':['Jan', 'Feb', 'Mar','Apr'],
    'Sales':[200,300,400,500],
    'Expensis':[250,350,450,550]

}

table_1=pd.DataFrame(data)
print(table_1)


a=table_1['Sales'].max()
b=table_1['Expensis'].max()
print(f'\nEng yukori Sales {a}')
print(f'Eng yukori Expensis {b}')


a=table_1['Sales'].min()
b=table_1['Expensis'].min()
print(f'\nEng past sotuvlar Sales {a}')
print(f'Eng past xarajatlar Expensis {b}')


a=table_1['Sales'].mean()
b=table_1['Expensis'].mean()
print(f'\nO‘rtacha sotuvlar Sales {a}')
print(f'O‘rtacha xarajatlar Expensis {b}')


Create a DataFrame named expenses with columns 'Category', 'January', 'February',
 'March', and 'April', representing monthly expenses for
 different categories. Use below table.

import pandas as pd

data= {
    'Category': ['Rent','Utilities','Groceries','Entertainment'],
    'January':[1200,200,300,150],
    'February':[1300,220,320,160],
    'March' :[1400,240,330,170],
    'April' :[1500,250,350,180]
}


tb=Tabl_2=pd.DataFrame(data)

2.Calculate and display the maximum expense for each category.

tb['Tabl']=tb[['January','February','March','April']].max(axis=1)

max_2= tb.groupby("Category")['Tabl'].max()

max_2= tb.groupby("Category")['Tabl'].max().sort_values()

3.Calculate and display the minimum expense for each category.

tb['minss']=tb[['January','February','March','April']].min(axis=1)

W=tb.groupby('Category')['minss'].min().sort_values()


3.Calculate and display the average expense for each category.

tb['teb_avg']=tb[['January','February','March','April']].mean(axis=1)

avg_mean=tb.groupby('Category')['teb_avg'].mean().sort_values()




































