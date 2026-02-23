import matplotlib.pyplot as plt 
import numpy as np 

# Historgram = A visual representation of quantitative data.
                # They group values into bins (intervals)
                # and counts how many fall in each range.

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=1""0,
                 color="lightgreen",
                 edgecolor="black")

plt.title("Exam Scores")

plt.xlabel("Scores")
plt.ylabel("No of Students")

plt.show()