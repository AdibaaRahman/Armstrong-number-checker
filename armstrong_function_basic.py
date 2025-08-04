def armstrong(n):    
    num = n
    temp = str(n)
    size = len(temp)
    add = 0
    for i in range(size):
        add += (n % 10) ** size
        n = n // 10
    if add == num:
        return 'Armstrong number'
    else:
        return 'Number is not Armstrong'    

value = int(input('Enter the number: '))
print(armstrong(value))