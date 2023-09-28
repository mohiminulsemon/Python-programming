def solve(X,N):
    S = 0
    for i in range(2,N+1,2):
        # if(i%2 == 0):
        #     S += X**i
        S += X**i
    return S

# X = int(input())
# N = int(input())
X, N = map(int, input().split())
print(solve(X,N))