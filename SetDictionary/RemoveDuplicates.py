test_list = [1,5,3,6,3,5,6,1]

# its draw back is that order is not preserved.

test_list = list(set(test_list))
print(test_list)