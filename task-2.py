# Exercise:
# Plot a line graph to show the population growth of a city over a period of 5 years. The population data is given below:

""" 
Year Population
2018 100000
2019 110000
2020 120000
2021 130000
2022 140000 
"""
import matplotlib.pyplot as plt

data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Population": [100000, 110000, 120000, 130000, 140000],
    "label": "Town Population by Year"
}

plt.plot(data["Year"], data["Population"], label=data["label"])

plt.xlabel("Year")
plt.ylabel("Population")
plt.title(data["label"])

plt.legend()

# Removing decimal points from x-axis labels dont know why I had to do this!
plt.xticks(data["Year"], [str(year) for year in data["Year"]])

plt.show()
