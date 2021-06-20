import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk(5000)
rw.fill_walk()
point_numbers = list(range(rw.num_points))

plt.figure(figsize=(6.4, 3.6), dpi=300)
plt.plot(rw.x_values, rw.y_values, linewidth=2)
#plt.scatter(0, 0, c="green", edgecolors="none", s=20)
#plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=20)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
#plt.savefig("cloud7_FM.png", bbox_inches="tight")
plt.show()