#normal function

"""
def doubled(x):
    return x*2
print(doubled(2))

"""
# lambda function

doubled = lambda x: x*2
print(doubled(2))

add  = lambda x,y: x+y
print(add(2,3))

# map 
numbers = [1,2,3,4,5]
# doubled_numbers = map(lambda x: x*2,numbers)
doubled_numbers = list(map(doubled,numbers))
print(doubled_numbers)

# filter 

actors = [
    {'name': 'john', 'age': 25},
    {'name': 'jane', 'age': 30},
    {'name': 'peter', 'age': 35},
    {'name': 'jeff', 'age': 40},
    {'name': 'mike', 'age': 45},
]

juniors = filter(lambda x: x['age'] < 40, actors)
print(list(juniors))