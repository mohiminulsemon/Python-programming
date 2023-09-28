# set is a unique collection, it keeps no duplicates

numbers = [1, 2, 5, 4, 5, 6, 7, 8, 9, 8]
print(numbers)

#converting list to set
numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(55)
print(numbers_set)

numbers_set.remove(5)
print(numbers_set)

for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('exists')


A = {1, 2, 3}
B = {3, 4, 5}

print(A & B) # intersection
print(A | B) # union
print(A - B) # difference
print(A ^ B) # symmetric difference
