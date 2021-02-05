num = 11
if num >1:
    for i in range(2, num):
        if(num%i) ==0:
            print(num, "is not a prime number ")
            break
    #         here note that else is not part of if condition
    #         in python else (under the loop) works only when loop
    #  don't get terminated by break statement
    else:
        print(num, 'is a prime number')

else:
    print(num, 'is not a prime number')