#!/usr/bin/env python
# coding: utf-8

# In[59]:


# Imports:
import pandas as pd
import plotly
import plotly.express as px
from pandas_profiling import ProfileReport
from autoviz.AutoViz_Class import AutoViz_Class


# In[2]:


# -- Settings Plotly template
#      Reference Link:
#      https://plotly.com/python/templates/
#      Try other themes: 'plotly_dark', 'plotly_white', 'ggplot2', 'seaborn', 'simple_white'
template_style = "plotly_white"


# In[3]:


df = pd.read_excel("/Users/AbdurRahman/Downloads/data (1).xlsx", engine="openpyxl")


# In[5]:


df.head()


# # ## Explore Dataset

# ### Traditionally

# In[6]:


# Basic Info about DataFrame
df.info()


# In[7]:


# Describe Method
df.describe()


# In[8]:


# Get a view of unique values in column, e.g. 'Ship Mode'
df["Ship Mode"].unique()


# In[9]:


# NaN count for each column
df.isnull().sum()


# # ### Automated Reports

# ### Pandas Profiling Report

# In[20]:


# Generate Pandas Profiling Report
profile = ProfileReport(df, title="Sales Profiling Report")

#View in Notebook
profile.to_widgets()


# In[77]:


# Export Pandas Profiling Report to HTML
profile.to_file("/Users/AbdurRahman/Desktop/Project/SalesProfilingReport.html")


# # #### Auto Viz Report

# In[ ]:


AV = AutoViz_Class()
df_autoviz = AV.AutoViz("/Users/AbdurRahman/Downloads/data (1).xlsx")


# # # Data Preperation & Analysis

# # ### 🚩 TASKS:
# #### What was the highest Sale in 2020?
# #### What is average discount rate of charis?
# #### Add extra columns to seperate Year & Month from the Order Date
# #### Add a new column to calculate the Profit Margin for each sales record
# #### Export manipulated dataframe to Excel
# #### Create a new dataframe to reflect total Profit & Sales by Sub-Category
# #### Develop a function, to return a dataframe which is grouped by a particular column (as an input)

# # #What was the highest Sale in 2020?

# In[60]:


##highest Sale
df.nlargest(3, "Sales")


# In[61]:


# Highest Sale
df.iloc[df["Sales"].argmax()]


# # ##What is average Discount of charis?

# In[70]:


# Create Boolean mask
mask = df["Sub-Category"] == "Chairs"
df[mask].head()


# In[108]:


# Use Boolean mask to filter dataframe
df[mask]["Discount"].mean()*100


# # ### Add extra columns to seperate Year & Month from the Order Date

# In[71]:


df["Order Date Year"] = df["Order Date"].dt.year
df["Order Date Month"] = df["Order Date"].dt.month
df.head(2)


# # ##Add a new column to calculate the Profit Margin for each sales record 

# In[72]:


df["Profit Margin"] = df["Profit"] / df["Sales"]
df.head(3)


# In[ ]:





# In[76]:


# **Export manipulated dataframe back to excel**
df.to_excel("/Users/AbdurRahman/Desktop/Project/data_output.xlsx", index=False)


# # #### Total Profit &Sales by Sub-Category

# In[82]:


# Group By Sub-Category [SUM]
df_by_sub_category = df.groupby("Sub-Category").sum()

# Reset Index
df_by_sub_category.reset_index(inplace=True)
df_by_sub_category.head()


# # ### Develop a function, to return a dataframe which is grouped by a particular column (as an input)

# In[83]:


# Groupby as a function

def grouped_data(column_name):
    """
    Groupby column and return DataFrame
    Input: Column Name
    """
    df_tmp = df.groupby(column_name).sum()
    df_tmp.reset_index(inplace=True)
    return df_tmp

# Group DataFrame by Segment
grouped_data("Segment")


# In[ ]:





# # # Further Deep Dive & Visualization
# 

# # ### 🚩 Objective:
# 
# #### Further Analysis/Deep Dive using various kind of Charts
# #### Prepare/Refactor Dataframe for different Charttypes
# ### Generate & Export 'Ready-To-Present- Charts': Clean & Interactive
# 
# # #### 📊 Chart Types:
# ### [x]  Histogram
# ### [x] Boxpot
# ### [x] Various Barplots
# ### [x] Scatterplot
# ### [x] Linechart

# In[84]:


# Quick Stats Overview for Sales
df["Sales"].describe()


# In[113]:


# Create Chart
fig = px.histogram(df, x="Sales", template=template_style)
# Plot Chart
fig.show()


# In[ ]:





# In[93]:


# **Show the distribution and skewness of Sales [Boxplot]**
# Create Chart
fig = px.box(df, y="Sales", range_y=[0, 1000], template=template_style)
# Plot Chart
fig.show()


# In[96]:



# **Plot Sales by Sub-Category**
# Create Dataframe
data = grouped_data("Sub-Category")
data.head()


# In[97]:



# Create Chart
fig = px.bar(
    data,
    x="Sub-Category",
    y="Sales",
    title="<b>Sales by Sub Category</b>",
  
    template=template_style,
)

# Display Plot
fig.show()



# In[100]:


# Export Chart to HTML
plotly.offline.plot(fig, filename="/Users/AbdurRahman/Desktop/Project/Sales_Sub_Cat.html", auto_open=False)


# In[101]:



# **Plot Profit by Sub-Category**
# Create Chart
fig = px.bar(
    data,
    x="Sub-Category",
    y="Profit",
    title="<b>Profit by Sub Category</b>",
    template=template_style,
)
# Display Plot
fig.show()


# In[ ]:


# Export Chart to HTML
plotly.offline.plot(fig, filename="/Users/AbdurRahman/Desktop/Project/Sales_Sub_Cat.html", auto_open=False)


# In[103]:


# **Plot Sales & Profit by Sub-Category**
# Create Chart
fig = px.bar(
    data,
    x="Sub-Category",
    y="Sales",
    color="Profit",
    color_continuous_scale=["red", "yellow", "green"],
    template=template_style,
    title="<b>Sales & Profit by Sub Category</b>",
)

# Display Plot
fig.show()


# In[119]:


# Export Chart to HTML
plotly.offline.plot(fig, filename="/Users/AbdurRahman/Desktop/Project/Profit_Sales_Sub_Cat.html", auto_open=False)


# In[104]:


# #### Inspect Negative Profit of Tables
# Is there any linear correlation between Sales/Profit & Discount? [Scatterplot]
# Create Chart
fig = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Discount",
    template=template_style,
    title="<b>Scatterplot Sales/Profit</b>",
)

# Display Plot
fig.show()


# In[114]:


# Export Chart to HTML

plotly.offline.plot(fig, filename="/Users/AbdurRahman/Desktop/Project/Profit_Sales_Sub_Cat.html", auto_open=False)


# In[121]:


# **Check Discount mean by Sub Category**
# Create new dataframe: Group by 'Sub-Category' and aggregate the mean of 'Discount'
df_discount = df.groupby("Sub-Category").agg({"Discount": "mean", "Profit": "sum"})

# Display first 5 rows of new dataframe
df_discount.head()


# In[122]:


# **Plot Mean Discount by Sub Category**
# Create Chart
fig = px.bar(
    df_discount,
    x=df_discount.index,
    y="Discount",
    color="Profit",
    color_continuous_scale=["red", "yellow", "green"],
    template=template_style,
    title="<b>Mean Discount by Sub Category</b>",
)

# Display Plot
fig.show()


# # #Plot Sales & Profit Development for the year 2020

# In[115]:


# Sort Values by Order Date
df_sorted = df.sort_values(by=["Order Date"])


# In[116]:


# Add cummulative Sales & Profit
df_sorted["cummulative_sales"] = df_sorted["Sales"].cumsum()
df_sorted["cummulative_profit"] = df_sorted["Profit"].cumsum()

# Print tail & head of sorted dataframe
df_sorted.tail(3)


# In[127]:


df['Profit'].sum()


# In[128]:


df['Sales'].sum()


# In[ ]:





# In[117]:


# Create Chart
fig = px.line(
    df_sorted,
    x="Order Date",
    y=["cummulative_sales", "cummulative_profit"],
    template=template_style,
    title="<b>Sales/Profit Development</b>",
)

# Display Plot
fig.show()


# In[120]:


# Export Chart to HTML
plotly.offline.plot(
    fig, filename="/Users/AbdurRahman/Desktop/Project/Sales_Profit_Development.html", auto_open=False
)


# In[ ]:



# # End of the project 🚀

