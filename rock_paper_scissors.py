# THE FAMOUS, *ROCK PAPER SCISSORS GAME*

#defining computer values by randomizing
import random
computer = random.choice([1,2,3])

#creating dictionaries which will store numeric values 
gamedict = {"r":1, "p":2, "s":3}
revdict = {1:"rock", 2:"paper", 3:"scissors"}

#defining user values by input
youstr = input("(r for rock, p for paper, s for scissors) \n Enter your choice: ")
you = gamedict[youstr]

#displaying the choices of user and computer 
print(f"You chose {revdict[you]} \nComputer chose {revdict[computer]}")

#logic 
if (computer-you == -1 or computer-you == 2):
    print("You win")
elif(computer-you == 1 or computer-you == -2):
    print("You lose")
else:
    print("It's a draw")

# #logic
# if (computer == you):
#     print("It's a draw")
# else:
#     if ( computer==1 and you==2 ):
#         print("You won")
#     elif ( computer==1 and you==3 ):
#         print("You lost")
#     elif ( computer==2 and you==1 ):
#         print("You lost")
#     elif ( computer==2 and you==3 ):
#         print("You won")
#     elif ( computer==3 and you==1 ):
#         print("You won")
#     elif ( computer==3 and you==2 ):
#         print("You lost")

