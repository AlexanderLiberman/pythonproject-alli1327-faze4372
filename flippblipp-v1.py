n = 15 #is edited depending on what max number user wants to use
for n in range(1, n):
    n = n +1
    if (n%3 == 0) and (n%5 == 0):
        print('flipp blipp')
    elif n%5 == 0:
        print('blipp')
    elif n%3 == 0:
        print('flipp')
    else:
        print(n)