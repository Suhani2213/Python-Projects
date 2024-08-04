'''We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.

Rules:
Snake wins over Water: Snake drinks Water (Snake > Water)
Water wins over Gun: Water puts out Gun (Water > Gun)
Gun wins over Snake: Gun shoots Snake (Gun > Snake)
'''


'''
1 for for snake
-1 for water
0 for gun

'''


import random

computer = random.choice([1, 0, -1])


youstr = input("Enter your choice from g, s, w: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"} # made for printing on screen Computer choose\ converting number to string: s {reverseDict[computer]}

you = youDict[youstr] # print(youDict[youstr]) ##output: Enter your choice: w resut -1

# By now we have 2 numbers (variables), you and computer

print(f"You Chose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")


if (computer == you):
    print("It's a tie!")

else:

    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went Wrong")