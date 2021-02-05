from itertools import  chain


s1 = "Geeks"
s2 = "for"
s3 = "Geeks"

res = list(chain(s1,s2,s3))
print(res)