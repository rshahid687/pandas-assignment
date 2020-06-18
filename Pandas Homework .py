#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
file = "Resources/purchase_data.csv"
data = pd.read_csv(file)

main_df = data 

main_df.head()


# In[19]:


#Total Players

totalPlayers = len(data["SN"].unique())

totalPlayers_df = pd.DataFrame(columns = ['Total Players'])

totalPlayers_df.loc[0,'Total Players'] = totalPlayers

totalPlayers_df


# In[20]:


# ## Purchasing Analysis (Total)

itemCount = len(data["Item Name"].value_counts()) 
avgPrice = data['Price'].mean()
purchases = data['Price'].count()
revenue = data['Price'].sum()
summaryPurchases = pd.DataFrame({"Number of Unique Items": itemCount,
                              "Average Price": avgPrice,
                              "Number of Purchases": purchases,
                              "Total Revenue": revenue},index=[0])
summaryPurchases


# In[21]:


# Regroup Data by Gender into newData

summaryPurchases = summaryPurchases.dropna(how='any')
summaryPurchases

genderData = data.set_index("Gender")
genderData.head()

genderData2 = df.loc[:, ["Gender", "SN", "Age"]]
genderData3 = genderData2.drop_duplicates()
genderGroup = genderData3.groupby(["Gender"])
genderGroupCounter = genderGroup.count() # new df
newData = genderGroupCounter.rename(columns={"SN":"Total Counts"}) 


# In[23]:


# ##Gender Demographics

genderPercentage = round(newData["Total Counts"] / totalPlayers,2)*100

newData['Age'] = genderPercentage

newData.rename(columns={'Age':'Percentage of Players'})

newData


# In[25]:


## Gender Purchase Analysis

genderData4 = data.loc[:, ["Gender","SN","Price"]]
genderGroup2 = genderData4.groupby(["Gender"])
genderGroupCounter2 = genderGroup2.count()
newData2 = genderGroupCounter2.rename(columns={"SN":"Purchase Count"})

avgPurchase = round(genderGroup2['Price'].mean(),2)

totalPurchase = round(genderGroup2['Price'].sum(),2)

avgTotalPurchasePer = round(totalPurchase / newData['Total Counts'],2)

summaryPurchases2 = pd.DataFrame({ "Purchase Count": newData2['Purchase Count'],
                             "Average Purchase Price": avgPurchase,
                              "Total Purchase Value": totalPurchase,
                             "Avg Total Purchase per Person":avgTotalPurchasePer})

summaryPurchases2


# In[31]:


## Age Demographics

bins = ([0,9,14,19,24,29,34,39,999])
groups = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
gender3["Total Count"] = pd.cut(genderData3["Age"], bins, labels=groups, include_lowest=True)

totalCount = pd.DataFrame(genderData3["Total Count"].value_counts())
totalCount["Percentage of Players"] = ((totalCount["Total Count"]/(totalCount["Total Count"].sum())) * 100).round(2)


summaryTable = totalCount.sort_index()

summaryTable


# In[32]:


#Purchasing Analysis (age)

data['Age Ranges'] = pd.cut(data['Age'], bins, labels=groups, include_lowest=True)
ageData = data.groupby('Age Ranges')                        


purchasesCount = ageData['Purchase ID'].count()
avgPurchasePrice = round(ageData['Price'].mean(),2)
totalPurchases = ageData['Price'].sum()


ageSummary = pd.DataFrame({"Purchase Count": purchasesCount,
                                 "Average Purchase Price": avgPurchasePrice,
                                 "Total Purchase Value": totalPurchases})
ageSummary


# In[34]:


#Top 5 spenders

spenderData =data.groupby('SN')

spenderCounts =spenderData['Purchase ID'].count()

avgPrice = spenderData['Price'].mean()

totalPurchase =spenderData['Price'].sum()

topSpenders =pd.DataFrame({'Purchase Count': spenderCounts,
                        'Average Purchase' : avgPrice,
                        'Total Purchase Value' : totalPurchase})


top5 = topSpenders.nlargest(5,'Total Purchase Value')

top5.style.format({'Average Purchase Price':"${:,.2f}", 'Total Purchase Value':"${:,.2f}"})

top5


# In[35]:


#Most Popular Items

mostPopular = data[['Item ID', 'Item Name', 'Price']]

idName = mostPopular.groupby(['Item ID', 'Item Name'])

count = idName['Item ID'].count()

itemPrice = round(idName['Price'].sum()/count,2)

price = idName['Price'].sum()

top5 = pd.DataFrame({'Purchase Count': idName,
                       'Price': itemPrice,
                       'Total Purchase Value': price})
top5 = top5_df.nlargest(5,'Purchase Count')

top5


# In[16]:


# Most Profitable 

largestProfits = top5.nlargest(5,'Total Purchase Value')

largestProfits


# In[ ]:




