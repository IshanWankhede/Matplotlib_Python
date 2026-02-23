import matplotlib.pyplot as plt
import numpy as np

#Bar Chart = compare categories of data by representing each category with a bar

catrogories = ["Grains", "Vegetables", "Meat", "Sweets", "Diary", "Protiens"]

values = np.array([4, 3, 2, 1, 5, 4])

plt.bar(catrogories, values, color="red")
# plt.barh(catrogories, values, color="red")   horizontal bar chart

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()