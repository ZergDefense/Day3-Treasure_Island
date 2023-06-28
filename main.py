print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer_one = input('Where would you like to turn? Type "left" or "right"').lower()

if answer_one != "left":
    print("You have fallen to a hole. Game over! :(")
else:
    answer_two = input('Nice decision, you still live. Now would you like to swim or wait? Type "wait" or "swim"').lower()
    if answer_two != "wait":
        print("You have been attacked by a trout. Game over! :(")
    else:
        answer_three = input('Very wise, still living. Now you have to choose between 3 doors, which one would you '
                             'like to enter? Type "red" or "blue" or "yellow"').lower()
        if answer_three == "red":
            print("You have been burned by fire heavily. Game over! :(")
        elif answer_three == "blue":
            print("You have been eaten by beasts. Game over! :(")
        elif answer_three == "yellow":
            print("You have found the treasure and won this incredible game. Congratulations! :)")
        else:
            print("Game over! :(")
