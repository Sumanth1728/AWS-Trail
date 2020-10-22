import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Invoice.csv")

data.head()

data.info()

data.describe()

df=pd.DataFrame(data)

df.drop(['Amount 1'],axis=1,inplace=True)

df =df.iloc[:, ~df.columns.str.contains('Unnamed')]

df.info()

import datetime
df['year']=pd.DatetimeIndex(df['AccountingDate']).year
df['month']=pd.DatetimeIndex(df['AccountingDate']).month
df.info()

df['AccountingDate'].min()
df['month']
df["month"]=df["month"]. astype(str)
df["year"]=df["year"]. astype(str)
df["month_year"]=df[["month","year"]].agg('-'.join,axis=1)
df.isnull().sum()
print(df.columns.tolist())

df.groupby("month_year").sum()["Amount "].reset_index()
df["Amount "]=df["Amount "].astype(int)
df["Amount "]
df_sales=df.groupby("month_year").sum()["Amount "].reset_index()
plt.figure(figsize=(15,6))
sns.barplot(x="month_year",y="Amount ",data=df_sales)
plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("analysis of sales")
plt.show()
df_sales
plt.figure(figsize=(15,6))
sns.countplot(x="AmountCurrency",data=df)
plt.xlabel("AmountCurrency")
plt.ylabel("higest currency used")
plt.title("currency analysis")
plt.show()
df_supplier=df.groupby("SupplierId").sum()["Amount "].reset_index()
plt.figure(figsize=(120,20))
sns.barplot(x="SupplierId",y="Amount ",data=df_supplier)
plt.xlabel("Supplier")
plt.ylabel("Amount")
plt.title("analysis of supplier sales")
plt.xticks(rotation='vertical',size=10)
plt.ylim(1000,100000)
plt.show()

df_location=df.groupby("SupplierLocationId").sum()["Amount "].reset_index()

plt.figure(figsize=(40,10))
sns.barplot(x="SupplierLocationId",y="Amount ",data=df_location)
plt.xlabel("SupplierLocationId")
plt.ylabel("Amount")
plt.title("analysis of supplierlocation sales")
plt.xticks(rotation='vertical',size=10)
plt.show()