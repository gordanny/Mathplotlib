import pygal

from die import Die

# Create a dice and roll it 1000 times.
d1 = 6
d2 = 6
number_of_rolls = 1000000
die_1 = Die(d1)
die_2 = Die(d2)
results = []
for _roll_num in range(number_of_rolls):
    results.append(die_1.roll() + die_2.roll())

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides + 1
frequencies = [results.count(value) for value in range(2, max_result)]

# Visualize the relusts.
hist = pygal.Bar()
hist.title = "Result of rolling D{} and D{} and {} times.".format(d1, d2, number_of_rolls)
hist.x_labels = [str(i) for i in range(2, max_result)]
hist._x_title = "Result"
hist._y_title = "Frequency of result"
hist.add("D{} * D{}".format(d1, d2), frequencies)
hist.render_to_file("die_visual.svg")