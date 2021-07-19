import random 
#Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return False
        elif you == 's':
            return True    
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'r':
            return True    
    elif comp == 's':
        if you == 'r':
            return False
        elif you == 'p':
            return True    

print("Computer Turn: Rock(r) Paper(p) or Scissor(s)? ")
randNo = random.randint(1,3)
if randNo ==1:
    comp = 's'
elif randNo ==2:
    comp = 'w' 
elif randNo ==3:
    comp = 'g'   

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)? ")
a = gameWin(comp , you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")    
else:
    print("You Lose!")    