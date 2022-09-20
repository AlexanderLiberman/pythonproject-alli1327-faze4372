def flippblipp(n):
    if (n%3 == 0) and (n%5 == 0):
        return 'flipp blipp'
    elif n%5 == 0:
        return 'blipp'
    elif n%3 == 0:
        return 'flipp'
    else:
        return n

gameStart = True
print("	", 1)

n = 1 #sets a base-arg

while(gameStart):
    n = n + 1
    playerInput = input("Nästa: ")
    if playerInput != str(flippblipp(n)):
            gameStart = False
            print("Fel-", flippblipp(n))
            if input("Försök igen? [y/n]: ") == 'y': #restart command
                gameStart = True #resets start-rule
                n = 1 #resets n-counter
                print()
                print("	",1) #starts game



    

