"""snake water gun
select one random.choice and then take input from user
using logic snake>water,water>gun,gun>snake play the
game with user 10 times and then show both's score"""

import random
list1=['snake','water','gun']


def game(a,b):
    if a=='snake' and b=='water':
        c='snake drinks the water!'
        return c
    elif a=='snake' and b=='gun':
        d='gun kills the snake'
        return d
    elif a=='water' and b=='gun':
        e='the water dissolves the gun'
        return e        

    elif a=='gun' and b=='snake':
        return d
    elif a=='water' and b=='snake':
        return c
    elif a=='gun' and b=='water':
        return e 


chances=1
user=0
computer=0

print("this is snake water gun game!")


while(chances<=10):
    g=int(input("enter your choice: 1)snake 2)water 3)gun\n"))
    
    r=random.choice(list1)
    #instead of writing code for draw 3 times,write only once:
    #if g==r:
    #    print("draw!!!")
    
    if g==1 and r=='snake':
        print("draw!!")
       
    elif g==1 and r=='water':
        print('YOU won-the snake drinks the water :)') 
        user=user+1

    elif g==1 and r=='gun':
        print('YOU lose-the gun kills the snake :(') 
        computer=computer+1

    elif g==2 and r=='water':
        print("draw!!")
    
    elif g==2 and r=='snake':
        print('YOU LOSE-the snake drinks the water :(') 
        computer=computer+1

    elif g==2 and r=='gun':
        print('YOU WON-the water dissolves the gun :)')   
        user=user+1

    elif g==3 and r=='gun':
        print("draw!!")
    
    elif g==3 and r=='water':
        print('YOU LOSE-the water dissolves the gun :(') 
        computer=computer+1

    elif g==3 and r=='snake':
        print('YOU WON-the gun kills the snake :)')   
        user=user+1
    chances=chances+1    

    
if chances>10:
    print('game over')
    print("user's score: ",user)
    print("computer's score: ",computer)













