import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([50, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([19, 34, 3, 52])

line_style = dict(marker=".",
                  markersize=20,
                  markerfacecolor="gold",
                  markeredgecolor="gold",
                  linestyle="dashed",
                  linewidth=4,
                  )


plt.plot(x, y1, color="green", **line_style)  # **line_style we are unpacking the dict

plt.plot(x, y2, color="red", **line_style)

plt.plot(x, y3, color="blue", **line_style)

plt.show()  

# -  Constructor syntax (dict()):

# line_style = dict(marker=".",
#                   markerfacecolor="gold",
#                   markeredgecolor="gold",
#                   linestyle="dashed",
#                   linewidth=4,
#                   color="red")

# - Literal syntax:

# line_style = {
#     "marker": ".",
#     "markerfacecolor": "gold",
#     "markeredgecolor": "gold",
#     "linestyle": "dashed",
#     "linewidth": 4,
#     "color": "red"
# }

# How to Unpack a Dictionary
# - **dict_name expands the dictionary into keyword arguments.
# - Each key becomes the argument name, and each value becomes the argument value.

# example:=>
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# info = {"name": "Ishan", "age": 25}

# # Unpack dict into function arguments
# greet(**info)   # Equivalent to greet(name="Ishan", age=25)