from functools import cmp_to_key

def cmp_fun(a,b):
    if a[-1]>b[-1]:
        return 1
    elif a[-1]<b[-1]:
        return -1
    else:
        return 0

list1 = ['geeks', 'for', 'geeks']
l = sorted(list1, key=cmp_to_key(cmp_fun))
print('sorted list : ', l)