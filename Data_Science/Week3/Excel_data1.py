import xlrd

loc = ('mydata.xlsx')
work_book = xlrd.open_workbook(loc)
sheet = work_book.sheet_by_index(0)

# 1) Print word CRICKET from excel file.
print(sheet.cell_value(0, 0))

# 2) Print 34 from above excel file
print(int(sheet.cell_value(5, 1)))

# 3) Print 65 from above excel file
print(int(sheet.cell_value(8, 3)))

# 4) Print total number of rows
print(sheet.nrows)

# 5) Print total number of columns
print(sheet.ncols)

# 6) Print total number of matches
matches = []
for i in range(2, sheet.nrows):
    matches.append(int(sheet.cell_value(i, 0)))
print(len(matches))

# 7) Print name of all players ( using for loop )
players = []
for i in range(1, sheet.ncols):
    players.append(sheet.cell_value(0, i))
print(players)

# 8) Print score of ROHIT in all matches ( using for loop )
Rohit = []
for i in range(2, sheet.nrows):
    Rohit.append(int(sheet.cell_value(i, 1)))
print(Rohit)

# 9) Allow user to enter name of the player. Print Player Found or Player not found
user_input = input("Enter player name: ")
players = []
for i in range(1, sheet.ncols):
    players.append(sheet.cell_value(0, i))

for j in range(0, len(players)):
    if user_input == players[j]:
        print("Player found")
        break
else:
    print("Player does not found")

# 10)Allow user to enter name of the player. Print scores of all matches of that player.
user_input = input("Enter player name: ")

for j in range(1, sheet.ncols):
    if user_input == sheet.cell_value(colx=j, rowx=0):
        for i in range(2, sheet.nrows):
            print(int(sheet.cell_value(rowx=i, colx=j)))
        break
else:
    print("Player does not found")

# 11)Allow user to enter name of the player. Print score of last match of that player.
user_input = input("Enter player name: ")

for j in range(1, sheet.ncols):
    if user_input == sheet.cell_value(colx=j, rowx=0):
        for i in range(-1, sheet.nrows):
            print(int(sheet.cell_value(rowx=i, colx=j)))
            break
        break
else:
    print("Player does not found")

# 12)Print all data as below format
MATCH = []
ROHIT = []
KOHLI = []
DHAWAN = []

for i in range(2, sheet.nrows):
    MATCH.append(int(sheet.cell_value(i, 0)))
    ROHIT.append(int(sheet.cell_value(i, 1)))
    KOHLI.append(int(sheet.cell_value(i, 2)))
    DHAWAN.append(int(sheet.cell_value(i, 3)))

for j in range(0, len(MATCH)):
    print("MATCH ", MATCH[j])
    print('score of: ROHIT IS', ROHIT[j])
    print('score of: KOHLI IS', KOHLI[j])
    print('score of: DHAWAN IS', DHAWAN[j])
    print('-------------------------')

# 13)Allow user to insert name of the player. Print Total and average score of that player
user_input = input("Enter player name: ")
player_data = 0

for j in range(1, sheet.ncols):
    if user_input == sheet.cell_value(0, j):
        for i in range(2, sheet.nrows):
            player_data = player_data + int(sheet.cell_value(i, j))
        print('Total is: ', player_data)
        print('Average score:', player_data / (sheet.nrows - 2))
        break
else:
    print("Player does not found")

# 14) Allow user to insert name of the player. Print Highest score of that player.
user_input = input("Enter player name: ")
Highest_score = 0

for i in range(1, sheet.ncols):
    if user_input == sheet.cell_value(0, i):
        for j in range(2, sheet.nrows):
            if Highest_score < int(sheet.cell_value(j, i)):
                Highest_score = int(sheet.cell_value(j, i))
        print(Highest_score)
        break
else:
    print("Player does not found")
