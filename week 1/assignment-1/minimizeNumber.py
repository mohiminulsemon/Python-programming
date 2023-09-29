n = int(input())
a = list(map(int, input().split()))

max = 0
flag = 1
while (1):
    
    for num in range(n):
        if a[num] % 2  == 0:
            a[num] = a[num] / 2
        else :
            flag = 0
            break
    if flag:
        max += 1
    else: 
        break

print(max)