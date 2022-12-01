'''задание 1'''
def SumList(x):
    sum = 0
    list = [int(input()) for i in range(x)]
    for i in range(x):
        sum += list[i]
    print(sum)
    print()

SumList(10)

'''задание 2'''
def CountList(x):
    count=0
    list = [int(input()) for i in range(x)]
    for i in list:
        if i == 0:
            count +=  1
    print(count)

CountList(10)

'''задание 3'''
print()

x = int(input())
for i in range(1, x+1):
    for j in range(1, i+1):
        print(j, end='')
    print() 

'''задание 4'''
x = int(input())
for i in range(1, x+1):
    for j in range(1, i+1):
        print(j, end='')
    for j in range(1, i)[::-1]:
        print(j, end='')
    print() 