# 1)
# Create bar graph from following data
#
# Generate bar graph from above data and assing following properties one by one.
# 1) Give title to graph ( State wise covid cases )
# 2) Give label to x axes ( state names ) and y axes ( covid cases )
# 3) Change color of bar graph
# 4) Change color of each bar from bar graph
# 5) Assign cases to each bar ( print cases in / top of the bar )

from matplotlib import pyplot as plt

states = ["Gujarat", "Maharashtra", "Rajasthan", "Madhya Pradesh", "Goa"]
cases = [4279, 1258, 3000, 900, 1450]


def addLabels(states, cases):
    for i in range(len(states)):
        plt.text(i, cases[i] - 1000, states[i])


plt.bar(states, cases, color=['r', 'g', 'b', 'c', 'k'])
plt.xlabel("State name")
plt.ylabel("covid cases")
plt.title("Total Covid Cases")
addLabels(states, cases)
plt.show()

# 2)
# Create pie chart from following data

# Branches = ["CE","CSE","IT","MEC","CIVIL"]
# Strength = [180,87,65,35,15]

# Give title of pie chart
# Give label to each and every slice
# Explode any one slice
# Add percentage inside slice
# Change color of each slice
# Add value inside slice

from matplotlib import pyplot as plt

Branches = ['CE', 'CSE', 'IT', 'MEC', 'CIVIL']
Strength = [180, 87, 65, 35, 15]
myexplode = [0.05, 0, 0, 0.05, 0]
mycolors = ["k", "hotpink", "b", "#4CAF50", "c"]

plt.pie(Strength, labels=Branches, explode=myexplode, shadow=True, colors=mycolors, autopct='%.2f%%', startangle=90,
        frame=True, radius=0.8, rotatelabels=True)
plt.title('All Branches')
plt.legend(title='Covid-90 Cases', bbox_to_anchor=(1, 1))
plt.show()

# 3) Create a Line chart from following data.
#
# Add x label
# Add y label
# Add plot title
# Change color of line

time = ['9.15', '9.30', '9.45', '10.00', '10.15', '10,30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00']
bob = [180, 187, 174, 160, 155, 157, 140, 145, 155, 150, 147, 142]
#
plt.plot(time, bob, ls='-.', color='r')
plt.ylabel('Runs')
plt.xlabel('Time')
plt.title('Line chart')
plt.show()

# 4) Create multiple line graph from following data
#
# Add x label, y label , plot tile
# Change color of each line
# Add legend which line is used for which stock
# Change color of lines

from matplotlib import pyplot as plt

time = ['9:15', '9:30', '9:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00']
bob = [180, 187, 174, 160, 155, 157, 140, 145, 155, 150, 147, 142]
icici = [220, 225, 227, 229, 215, 211, 210, 208, 198, 194, 200, 202]
iob = [95, 97, 96, 96, 98, 100, 102, 100, 97, 95, 94, 96]

plt.plot(time, icici, label='ICICI', marker='*', color='r')
plt.plot(time, bob, label='BOB', marker='o')
plt.plot(time, iob, label='IOB', marker='+')
plt.title('Share market plot')
plt.xlabel('Time duration')
plt.ylabel('Banks')
plt.legend(title='Banks', bbox_to_anchor=(1, 1))
plt.show()

# 5) Create Multiple bar graph from following data
# Assign legend
import numpy as np

Matches = ["Match 1", "Match 2", "Match 3", "Match 4", "Match 5"]
Rohit = [120, 25, 70, 0, 45]
Kohli = [25, 75, 5, 59, 150]
Dhawan = [15, 5, 90, 45, 35]

x_axis = np.arange(len(Matches))

a = plt.bar(x_axis - 0.15, Rohit, 0.15, label='Rohit')
b = plt.bar(x_axis, Kohli, 0.15, label='Kohli')
c = plt.bar(x_axis + 0.15, Dhawan, 0.15, label='Dhawan')

plt.bar_label(a, Rohit)
plt.bar_label(b, Kohli)
plt.bar_label(c, Dhawan)

plt.xticks(x_axis, Matches)
plt.title('Match data')
plt.xlabel('Matches')
plt.ylabel('Scores')
plt.legend(title="Player's")
plt.show()
