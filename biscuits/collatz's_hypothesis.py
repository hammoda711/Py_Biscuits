##########long solution
c0 = int(input('Enter a non- negative, non-zero integer: '))
step = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
        if c0 != 1:
            step += 1
            print(' New value is ', c0)
            continue
        elif c0 == 1:
            step += 1
            print(' New value is ', c0)
            break
    elif c0 % 2 == 1:
        c0 = c0 * 3 + 1
        if c0 != 1:
            step += 1
            print(' New value is ', c0)
            continue

print('Total Steps: ', step)
######################################################anothoer sol
#As Nearoo mentioned, c0 % 2 is the same as c0 % 2 != 0 because 1 (when c0 is odd, 'c0 % 2' is 1) has a boolean value of True.

#Here's the correct solution:

n = int(input("Enter a strictly positive integer: "))
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1: 
        n = (3*n) + 1
    steps += 1
    print(int(n))

print (steps)