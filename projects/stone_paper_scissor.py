import random

"""
1 --> stone 
-1--> paper
0 --> scissor
"""
print("🎮 Welcome to Stone-Paper-Scissors Game!")
computer = random.choice([-1,0,1])
# userstr = input("Enter your choice: ")
userstr = input("\nEnter your choice: (stone/paper/scissor)\n")

userDict = {
    "stone": 1 ,
    "paper":-1,
    "scissor": 0 
}
revDict = {
    1 :"stone",
    -1:"paper",
    0 :"scissor"
}
user = userDict[userstr]

print(f'You choose {revDict[user]} \nComputer choose {revDict[computer]}')

if(computer == user ):
    print("Its draw")
else:
    if(computer == 1 and user == -1):
        print("You Win")
    elif(computer == 1 and user == 0):
        print("You Lose")
    elif(computer == -1 and user == 1):
        print("You Lose")
    elif(computer == -1 and user == 0):
        print("You Win")
    elif(computer == 0 and user == -1):
        print("You Lose")
    elif(computer == 0 and user == 1):
        print("You Win")
    else:
        print("Something went wrong")