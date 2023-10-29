import random
rock='✊🏼'
paper='✋🏼'
scissors='✌️'

game_images=[rock,paper,scissors]
a=int(input("enter your choice:- 0-rock,1-paper,2-scissors: "))
if(a<0 or a>=3):
    print("Oops!! INVALID CHOICE")
else:
    print(game_images[a])
    c = random.randint(0, 2)
    print(f"computer's choice is {c}")
    print(game_images[c])
    if (c == a):
        print("It's a tie")
    elif (a == 2 and c == 0):
        print("you lose")
    elif (a == 0 and c == 2):
        print("you win")
    elif (c > a):
        print("you lose")
    elif (a > c):
        print("you win")
