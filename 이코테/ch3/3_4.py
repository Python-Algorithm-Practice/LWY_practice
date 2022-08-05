n, k = map(int, input().split())

ans = n%k
n -= n%k

while(n > 1):
    n //= k
    ans += 1
    
print(ans)