import xlrd
import numpy as np
from matplotlib import pyplot as plt

loc = ("mydata.xlsx")
work_book = xlrd.open_workbook(loc)
sheet1 = work_book.sheet_by_index(0)

# 1) Print Multiple bar graph of matches vs players from above excel
Matches = []
Rohit_score = []
Kohli_score = []
Dhawan_score = []

index = np.arange(sheet1.nrows - 2)
bar_width = 0.15

for i in range(2, sheet1.nrows):
    Matches.append(int(sheet1.cell_value(i, 0)))
    Rohit_score.append(int(sheet1.cell_value(i, 1)))
    Kohli_score.append(int(sheet1.cell_value(i, 2)))
    Dhawan_score.append(int(sheet1.cell_value(i, 3)))

plt.bar(index + bar_width, Rohit_score, width=bar_width, label='ROHIT')
plt.bar(index, Kohli_score, width=bar_width, label='KOHLI')
plt.bar(index - bar_width, Dhawan_score, width=bar_width, label='DHAWAN')
plt.xticks(index, Matches)
plt.title('Bar Graph of Matches vs Player Scores')
plt.xlabel('Matches')
plt.ylabel('Player Scores')
plt.legend()
plt.show()

# 2) Allow user to insert name of player, print matches vs score bar graph of that player. """
user_input = input("Enter player name: ")

Matches = []
player_score = []

for i in range(2, sheet1.nrows):
    Matches.append(int(sheet1.cell_value(i, 0)))

for j in range(1, sheet1.ncols):
    if user_input == sheet1.cell_value(0, j):
        for k in range(2, sheet1.nrows):
            player_score.append(int(sheet1.cell_value(k, j)))


def myLabel(Matches, player_score):
    for i in range(0, len(Matches)):
        plt.text(i, Matches[i], player_score[i])


plt.bar(Matches, player_score)
plt.title('Bar Graph of Matches vs Player Scores')
plt.xlabel('Matches')
plt.ylabel('Player Scores')
myLabel(Matches, player_score)
plt.show()

# 3) Print pie chart of total of all players ( single pie chart based on total of each player )
Player_name = []
Rohit_score = []
Kohli_score = []
Dhawan_score = []
Players = []

for i in range(2, sheet1.nrows):
    Rohit_score.append(int(sheet1.cell_value(i, 1)))
    Kohli_score.append(int(sheet1.cell_value(i, 2)))
    Dhawan_score.append(int(sheet1.cell_value(i, 3)))

Rohit_Total = np.sum(Rohit_score)
Kohli_Total = np.sum(Kohli_score)
Dhawan_Total = np.sum(Dhawan_score)

Players.append(Rohit_Total)
Players.append(Kohli_Total)
Players.append(Dhawan_Total)

plt.pie(Players, autopct="%.1f%%")
plt.title('Player score')
plt.show()

# 4) Sub plot : Print pie chart of match wise percentage score of each player (who scored how much percentage ?
fig, axs = plt.subplots(2, 4, figsize=(27, 9))
match1 = []
match2 = []
match3 = []
match4 = []
match5 = []
match6 = []
match7 = []

for i in range(1, sheet1.ncols):
    match1.append(int(sheet1.cell_value(1, i)))
    match2.append(int(sheet1.cell_value(2, i)))
    match3.append(int(sheet1.cell_value(3, i)))
    match4.append(int(sheet1.cell_value(4, i)))
    match5.append(int(sheet1.cell_value(5, i)))
    match6.append(int(sheet1.cell_value(6, i)))
    match7.append(int(sheet1.cell_value(7, i)))

labels = ["ROHIT", "KOHLI", "DHAWAN"]
axs[0, 0].pie(match1, autopct='%1.1f%%')
axs[0, 0].set_title('Match 1')

axs[0, 1].pie(match2, autopct='%1.1f%%')
axs[0, 1].set_title('Match 2')

axs[0, 2].pie(match3, autopct='%1.1f%%')
axs[0, 2].set_title('Match 3')

axs[0, 3].pie(match4, autopct='%1.1f%%')
axs[0, 3].set_title('Match 4')

axs[1, 0].pie(match5, autopct='%1.1f%%')
axs[1, 0].set_title('Match 5')

axs[1, 1].pie(match6, autopct='%1.1f%%')
axs[1, 1].set_title('Match 6')

axs[1, 2].pie(match7, autopct='%1.1f%%')
axs[1, 2].set_title('Match 7')
plt.tight_layout()
plt.show()
