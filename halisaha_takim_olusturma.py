import random

team_1 = []
team_2 = []
team_1_str = ""
team_2_str = ""

with open ("oyuncular_2.txt", "r") as file:
    file = list(file)
    random.shuffle(file)
    half_file_len = int(len(file) / 2)

    if len(file) % 2 == 0:
        for i in file[0:half_file_len]:
            team_1.append(i)
        for i in file[half_file_len:]:
            team_2.append(i)
    else:
        file.pop()
        for i in file[0:half_file_len]:
            team_1.append(i)
        for i in file[half_file_len:]:
            team_2.append(i)

    for i in team_1:
        team_1_str += i
    for i in team_2:
        team_2_str += i

    print(team_1_str)
    print(team_2_str)

open("takim_1.txt", "w")
file_1 = open("takim_1.txt", "w")
file_1.write(team_1_str)

open("takim_2.txt", "w")
file_2 = open("takim_2.txt", "w")
file_2.write(team_2_str)


