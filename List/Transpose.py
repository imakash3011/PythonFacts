matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]

print("Original Matrix")

for row in matrix:
    print(row)

print("Transpose Matrix")
print("\n")

t_matrix = zip(*matrix)

for row in t_matrix:
    print(row)