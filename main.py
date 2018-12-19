import matplotlib.pyplot as plt
import csv

chess_wins = '2016_CvH.csv'
white_winner = 0
black_winner = 0
draws = 0
white_clock = []
black_clock = []
with open(chess_wins) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        if row[17] == "White":
            white_winner += 1
        elif row[17] == "Black":
            black_winner += 1
        elif row[17] == "Draw":
            draws += 1
    print(white_winner)
    print(black_winner)
x = []
lsts = ["white wins", "black wins", "draw"]
performance = [white_winner,black_winner,draws]

plt.bar(lsts, performance, align='center', alpha=0.5, color="red")
plt.xticks(lsts, rotation=20)
plt.ylabel('Games', fontsize=16)
plt.xlabel("Winners", fontsize=16)
plt.title('Wins and draws of all 2016 chess official competitions')

plt.show()
