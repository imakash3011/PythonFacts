 #  No switch statement in python

def Cal(a):
    dic = {
        1: x+y,
        2: x-y,
    }
    return dic.get(a,"invalid")

if __name__=="__main__":
    a = int(input("Enter your choice : 1-Addition, 2-Substraction \n"))
    x = int(input())
    y = int(input())
    print(Cal(a))