import random 

choices = ("stone","paper","scissor")
n = random.choice(choices)
while True:
    human = input("enter your choice : ")
    if human == n:
        print("computer choice ",n)
        print("play again")
    elif human == "stone" and n == "paper":
        print("computer choice ",n)
        print("computer win !!")    
    elif human == "stone" and n == "scissor":
        print("computer choice ",n)
        print("you win !!") 
    elif human == "paper" and n == "stone":
        print("computer choice ",n)
        print("you win !!")    
    elif human == "paper" and n == "scissor":
        print("computer win !!") 
    elif human == "scissor" and n == "stone":
        print("computer choice ",n)
        print("computer win !!")   
    elif human == "scissor" and n == "paper":
        print("computer choice ",n)
        print(" you win !!")