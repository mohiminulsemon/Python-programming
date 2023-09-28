numbers = [12, 45 ,98 , 10 , 30 , 45, 50]

numbers.append(56) # will add 56 to the end of the list
print(numbers)

numbers.insert(2, 81) # will add 81 at index 2
print(numbers)

numbers.remove(98) # will remove 98 from the list
print(numbers)

#write way to remove 
if 56 in numbers: 
    numbers.remove(56)
print(numbers)

last = numbers.pop() # will remove the last element 
print(last, numbers)


index = numbers.index(45)
print(index)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)