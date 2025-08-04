def arm(n):
    num = n
    sum = 0
    size = len(str(n))
    while n > 0:
        dig = n % 10
        sum += dig ** size
        n = n // 10
    if sum == num:    
        return sum

for i in range(0, 1000):
    if arm(i) is not None:
        print('Armstrong number:', i)