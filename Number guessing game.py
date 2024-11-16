import random
print("Hello, I am NumBot.")
z=input("Do you want to play a game with me? (y/n): ")
z=z.lower()
def game():
    x=random.randint(0,10)
    print("I have a number between 0 to 10 in my mind. Lets see if you can guess it in three tries!")
    for i in range(0,3):
        y=input("guess a number between 0 to 10: ")
        if y.isdigit():
            y=int(y)
        else:
            print("Sorry, invalid input")
            break
        if y==x and y>=0 and y<=10:
            print("your guess is correct")
            print("*****YOU WON*****")
            break
        elif y>x and y>=0 and y<=10:
            print("your guess is too high")
            if i==2:
                print("*****YOU LOST*****")
                print("The number in my mind was: ",x)
        elif y<x and y>=0 and y<=10:
            print("your guess is too low")
            if i==2:
                print("*****YOU LOST*****")
                print("The number in my mind was: ",x)
        else:
            print("Sorry, invalid input")    
    z=input("Do you want to play again? (y/n): ")
    z=z.lower()
    return z
while True:
    if z=="y":
        z=game()
    elif z=="n":
        print("Thank You, Bye")
        break
    else:
        print("Sorry, invalid input")
        break
