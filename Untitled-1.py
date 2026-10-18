n = int(input())
s = 0
for i in range(1, n+1, 2):
    t = int(input())
    if t % 2 == 0:
        s += 1
print(s)