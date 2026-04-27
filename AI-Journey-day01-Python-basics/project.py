import random



def get_choices():
    player_choice=input("enter a choice(rock,paper,scissors:")
    option=["rock","paper","scissors"]
    computer_choice=random.choice(option)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

choices=get_choices()
print(choices)


a=int(input("Enter number: "))
b=int(input("Enter number: "))
print("Sum",a+b)
