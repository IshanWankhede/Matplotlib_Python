import matplotlib.pyplot as plt
import numpy as np

# scatter graph = Shows the relationship between two variables
#                 Helps to identify a correlation (+, -, None)
#                 Example: Study hours vs. Test scores

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])  # Hours studied
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])  # Grades

x2 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])  # Hours studied
y2 = np.array([52, 21, 32, 62, 68, 70, 75, 78, 82, 85, 87])  # Grades

plt.scatter(x1, y1, color="blue",
            alpha=0.4,
            s=200,
            label="Class-A")

plt.scatter(x2, y2, color="red",
            alpha=0.4,
            s=200,
            label="Class-B")

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grades")

plt.legend()
plt.show()