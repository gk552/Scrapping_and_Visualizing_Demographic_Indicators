from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel(r'C:\Users\Sanuj Goyal\OneDrive\Desktop\Population Prediction Project\Italy_output.xlsx')
print(df)

##################################Converting string data to numeric data#############################################

df['Average population'] = df['Average population'].str.replace(',', '').astype(int)
df['Live births'] = df['Live births'].str.replace(',', '').astype(int)
df['Deaths'] = df['Deaths'].str.replace(',', '').astype(int)
df['Natural change'] = df['Natural change'].str.replace('.',',')
df['Natural change'] = df['Natural change'].str.replace(',', '').astype(int)
#df['Natural change'] = df['Natural change'].str.replace('.', '').astype(int)
print(df)

##################################Converting data colums to lists####################################################

year = df['Year'].tolist()
population = df['Average population'].tolist()
births = df['Live births'].tolist()
deaths = df['Deaths'].tolist()
natural_change = df['Natural change'].tolist()
birth_rate = df['Crude birth rate'].tolist()
death_rate = df['Crude death rate'].tolist()
natural_change_rate = df['Net change'].tolist()
fertility = df['Fertility rate'].tolist()


print(year)
print(population)
print(births)
print(deaths)
print(natural_change)
print(birth_rate)
print(death_rate)
print(natural_change_rate)
print(fertility)

# #####################################MAKING GRPAHS######################################################################

# Line graph for population vs year
x_axis = year
y_axis = population
plt.plot(x_axis, y_axis)
plt.title('Population Growth 1981-2020')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()


#Combined line and bar graph for population and fertility rate
# Set up the figure and axes
fig, ax1 = plt.subplots()

# Bar chart
ax1.bar(year, population, color='blue')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Twin axes for line graph
ax2 = ax1.twinx()

# Line graph
ax2.plot(year, fertility, color='red', marker='o')
ax2.set_ylabel('Fertility Rate', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Set the x-axis labels
ax1.set_xticks(year)
ax1.set_xticklabels(year, rotation=90)

plt.title('Population vs Fertility Rate')
plt.show()


# Combined line graphs for biths and deaths
# Set up the figure and axes
fig, ax1 = plt.subplots()

# Line graph 1
ax1.plot(year, births, color='blue', marker='o')
ax1.set_xlabel('Year')
ax1.set_ylabel('No. of Births', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Twin axes for line graph
ax2 = ax1.twinx()

# Line graph 2
ax2.plot(year, deaths, color='red', marker='o')
ax2.set_ylabel('No. of Deaths', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Set the x-axis labels
ax1.set_xticks(year)
ax1.set_xticklabels(year, rotation=90)

plt.title('Births vs Deaths Year')
plt.show()


# Line graph for number of births, deaths and natural change
x_axis = year
y_axis = births, deaths, natural_change
plt.plot(x_axis, births, label='Births')
plt.plot(x_axis, deaths, label='Deaths')
plt.plot(x_axis, natural_change, label='Natural Change')
plt.title('Absolute change in Births, Deaths and Natural Change')
plt.xlabel('Year')
plt.ylabel('Births, Deaths, Natural Change')
plt.legend()
plt.show()


# Scatter plot for bith rate, death rate and natural change
plt.scatter(year, birth_rate, label='Birth Rate')
plt.scatter(year, death_rate, label='Death Rate')
plt.scatter(year, natural_change_rate, label='Natural Change')
plt.title('Crude rate of change(per 1000)')
plt.xlabel('Year')
plt.ylabel('Birth, Death and Natural change rate(per 1000)')
plt.legend()
plt.show()


# Linear Regression Model for predicting TFR using Number of Births
# Convert list of numpy array
births = np.array(births)

# Reshaping the data
births = births.reshape(-1, 1)

# Making prediction using Linear regression
model = LinearRegression()
model.fit(births, fertility)

# Predict the fertility rate using the model
fertility_rate_pred = model.predict(births)

# Plot the data points and the regression line
plt.scatter(births, fertility, label='Data Points')
plt.plot(births, fertility_rate_pred, color='red', label='Linear Regression')
plt.title('Fertility Rate vs Number of Births')
plt.xlabel('Number of Births')
plt.ylabel('Fertility Rate')
plt.legend()
plt.show()