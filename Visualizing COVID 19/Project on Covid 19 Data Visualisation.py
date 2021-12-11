import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep
import seaborn as sb

#URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
URL_DATASET = r'C:\Users\HP\AppData\Local\Programs\Python\Python38-32\Dataset.csv'
df = pd.read_csv(URL_DATASET)
print(df.head(3)) #  Get first 3 entries in the dataframe
print(df.tail(3))  # Get last 3 entries in the dataframe

#India


df_india = df[df['Country'] == 'India']
print(df_india.tail(5))
#plt.bar('Date', 'Confirmed', color = 'red', data=df_india )
plt.bar('Date', 'Deaths', color = 'red', data=df_india ) #You can also create line plot
plt.xlabel("Date from 22nd-Jan to 30th-Aug")
plt.ylabel("Total number of Deaths")
plt.title("India")
plt.show()

#Italy
df_italy = df[df['Country'] == 'Italy']
print(df_italy.head(10))

plt.xlabel("Date from 22nd-Jan to 30th-Aug")
plt.ylabel("Total number of Deaths")
plt.title("Italy")
#plt.bar('Date', 'Confirmed', color = 'blue', data=df_italy )
plt.bar(x = 'Date', height = 'Deaths', color = 'blue', data=df_italy )
plt.show()

#China
df_china = df[df['Country'] == 'China']
print(df_china.head(10))
plt.xlabel("Date from 22nd-Jan to 30th-Aug")
plt.ylabel("Total number of Deaths")
plt.title("China")
#plt.bar('Date', 'Confirmed', color = 'orange', data=df_china )
plt.bar(x = 'Date', height = 'Deaths', color = 'orange', data=df_china)
plt.show()

#US
df_us = df[df['Country'] == 'US']
print(df_us.head(10))
plt.xlabel("Date from 22nd-Jan to 30th-Aug")
plt.ylabel("Total number of Deaths")
plt.title("US")
#plt.bar('Date', 'Confirmed', color = 'green', data=df_us )
plt.bar(x = 'Date', height = 'Deaths', color = 'green', data=df_us)
plt.show()


#Spain
df_spain = df[df['Country'] == 'Spain']
print(df_spain.head(10))
plt.xlabel("Date from 22nd-Jan to 30th-Aug")
plt.ylabel("Total number of Deaths")
plt.title("Spain")
#plt.bar('Date', 'Confirmed', color = 'brown', data=df_spain )
plt.bar(x = 'Date', height = 'Deaths', color = 'brown', data=df_spain)
plt.show()


# In[77]:


df5 = df.query('Country in ["India", "China", "US"]')
print(df5)


# In[78]:


#fig, ax = plt.subplots(figsize=(15,12))
##sb.pairplot(df5,hue = 'Country',diag_kind = "hist",kind = "scatter",palette = "husl")
#sb.stripplot(x='Date', y='Deaths', hue='Country', data=df5)
#plt.show()


# In[80]:

#Creating Animation
#Step-2
list_dates = df['Date'].unique()
print(list_dates)

#### --- Step 3:- Pick 5 countries. Also create ax object

fig, ax = plt.subplots(figsize=(15, 8))
# We will animate for these 5 countries only
list_countries = ['India', 'China', 'US', 'Italy', 'Spain']
# colors for the 5 horizontal bars
list_colors = ['black', 'red', 'green', 'blue', 'yellow']


# In[86]:


def plot_bar(some_date):
    df2 = df[df['Date'].eq(some_date)]
    ax.clear()
    #print(df2)
    # Only take Deaths column in descending order
    df3 = df2.sort_values(by = 'Deaths', ascending = False)
    print(df3)
    # Select the top 5 Confirmed countries
    df4 = df3[df3['Country'].isin(list_countries)]
    print(df4)  # Uncomment to see that df is only for 5 countries
    sleep(0.2)  # To slow down the animation
    # ax.barh() makes a horizontal bar plot.
    return ax.barh(df4['Country'], df4['Deaths'], color= list_colors)


# In[87]:



my_anim = animation.FuncAnimation(fig = fig, func = plot_bar, 
                    frames= list_dates, blit=True, 
                    interval=20)


# In[88]:


plt.show()


# In[ ]:




