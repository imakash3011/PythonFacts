import heapq

lis = [6,7,9,4,3,5,8,10,1]
heapq.heapify(lis)

print("The 3 largest numbers in list are ; ", end=" ")
print(heapq.nlargest(3, lis))
