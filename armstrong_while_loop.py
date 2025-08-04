num = int(input('Enter a number: '))
temp = num
sum = 0
le = len(str(num))

while temp != 0:
    sum = sum + (temp % 10) ** le
    temp = temp // 10

if num == sum:
    print('This number is Armstrong number')
else:
    print('This number is not Armstrong number')