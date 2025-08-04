def arms(n):
    num = n
    sum = 0
    size = len(str(n))
    temp = n
    steps = []  # To store steps
    
    while temp > 0:
        dig = temp % 10
        steps.append(f"{dig}^{size}")
        sum += dig ** size
        temp = temp // 10

    if sum == num:
        print(f"{num} = " + " + ".join(steps))
        return sum

print(arms(9474))