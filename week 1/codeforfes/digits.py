test = int(input())
for i in range(test):
    n = int(input())
    string_n = str(n)
    for j in string_n[::-1]:
        print(j,end=' ')
    print()
