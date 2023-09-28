#index  = [ 0, 1, 2, 3, 4, 5 ,6, 7 ,8]
numbers = [ 2, 4, 6, 8, 9, 1, 3, 5, 7]
#index  = [-9,-8,-7,-6,-5,-4,-3,-2,-1]


print(numbers[3],numbers[-3])
print(numbers[1:4]) #[start:end] step default 1 / it can be written also [1:4:1]
print(numbers[1:7:2]) #[start:end:step]
print(numbers[4:]) #start index 4 to end
print(numbers[:4]) #start index 0 to before 4
print(numbers[1::2]) #[start:end:step]
print(numbers[:]) #start index 0 to end  / shortcut to copy a list
print(numbers[::-1]) # will reverse the list / shortcut to reverse a list
