# it is an anonymous function :  a function without any name
data = [("Aman", 5, "20"), ("kumar",1,"5"), ("Gfg",6, "10")]

# x will take x[0] as key to sort the data
data.sort(key=lambda x:x[0])
print(data)

data.sort(key=lambda x:x[1])
print(data)

data.sort(key=lambda x:int(x[2]))
print(data)