import csv
import sys
import random


# CSV Data from https://www.kaggle.com/datasets/buyuknacar/202122-nba-season-active-nba-players?resource=download Author: MUHAMMET ALI BÜYÜKNACAR Website: Kaggle

def questions(index):
    with open('players.csv') as csv_file:
        csv_reader1 = csv.reader(csv_file, delimiter=',')
        count1 = 0
        guesses = 0
        guessCorrect = False
        questionList = ["Player Team: ", "Player Position: ", "Player Points Per Game: ", "Player Assists Per Game: ", "Player Rebounds Per Game: ", "Player College: ", "Player Height: ", "Player Weight: ", "Player Age: ", "Player Salary: $"]
        questionIndex = [2, 1, 9, 11, 10, 7, 5, 6, 3, 8]
        playerStats = []
        for row1 in csv_reader1:
            count1 = count1 + 1
            if count1 == index:
                #print(f'{row1[0]}')
                for i in range(0, len(questionList) + 1):
                    if i == 0:
                        guess1 = input('Guess a NBA Player:\n')
                    else:
                        print("___________________________")
                        for j in range(0, len(playerStats)):
                            print(f'{playerStats[j]}')
                        print(f'{questionList[i-1]}{row1[questionIndex[i-1]]}')
                        playerStats.append(questionList[i-1] + row1[questionIndex[i-1]])
                        guess1 = input('Guess the NBA Player:\n')
                        if guess1.lower() == row1[0].lower():
                            print(f'Player Guessed Correctly\nPlayer: {row1[0]}\nGuesses: {guesses}')
                            guessCorrect = True
                            break
                        else:
                            guesses = guesses + 1
                if guessCorrect != True:
                    print(f'Player Not Guessed Correctly\nCorrect Player: {row1[0]}')


def rowCounter():
    with open('players.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        rowCount = 0
        for row in csv_reader:
            if count != 0:
                rowCount = rowCount +1
            else:
                count = count + 1

        index = random.randint(count, rowCount)
        questions(index)


rowCounter()