things = 'pen', 'tripod', 'paper', 'book'

print(things)
print(things[0])
print(things[-1])

# methods are same as list

if 'phone' in things:
    print('exists')
else: print('not exists')

print(len(things))

# tuples are immutable
# things[0] = 'phone' # not possible

mega =([1,2,3], [4,5,6], [7,8,9])
print(type(mega))

print(mega[0])
#mega[0] = [2,3,4] # not possible
mega[0][1] = 100 # means whole tuple is not changable but list inside it is changable
print(mega)
