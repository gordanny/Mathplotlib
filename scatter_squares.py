import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlOrBr, edgecolors="none", s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

plt.tick_params(axis="both", which="major", labelsize=14)
plt.axis([0, 5100, 0, 5000**3 + 100])

#plt.show()
plt.savefig("scatter_squares.png", bbox_inches="tight")