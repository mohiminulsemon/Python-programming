def sum(num1,num2):
    return num1+num2

res = sum(2,3)
print(res)


def sum1(num1,num2):
    sum = num1+num2
    mult = num1*num2
    sub = num1-num2
    return sum,mult,sub

res = sum1(2,3)
print(res)

#concept of global variables
print('concept of global variables')
x = 10

def test():
    global x # to use global varible
    x = 20
    print(x)

test()
print(x)