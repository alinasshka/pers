'''Задание 1'''
a = True
b = False

print(a and b) #1
print((a and b) or b ) #2
print((a and b) or (not(a and b))) #3
print( a and b or (not(a and b)) or b) #4
print( b and b or not(a) and (a or b or a) or not(a or b)) #5
print( 1 << 2 ) #6
print( 1 and 0 | 1 >> 1 ) #7
print( 1 & 0 | 1 >> 0 ) #8
print( 0b101 & 0b111 ^ 0b111 | 0b010 ) #9

'''Задание 2'''
a = int(input("Введите a: "))
b = int(input("Введите b:"))
if a < b:
    print(a)
else:
    print(b)

'''Задание 3'''
var1 = int(input("Введите var1:"))
var2 = int(input("Введите var2:"))
var3 = int(input("Введите var3:"))
if var1 > var2 and var1 > var3:
    print("Наибольшее значение:", var1 )
elif var3 > var1 and var3 > var2:
    print("Наибольшее значение:",var3 ) 
else:
    print("Наибольшее значение:",var2 )
    
'''Задание 4'''

a1 = int(input("Ввелите значение:"))
a2 = int(input("Введите значение:"))
a3 = int(input("Введите значение:"))
if (a1 != a2 and a2 != a3 and a1 != a3):
    print("Все числа уникальны")
elif a1 == a2 and a2 != a3 and a1 != a3:
    print("2 числа уникальных")
if a1 != a2 and a2 == a3 and a1 != a3:
    print("2 числа уникальны")
if a1 != a2 and a2 == a3 and a1 == a3:
    print("2 числа уникальны")
if a1 == a2 and a2 == a3 and a1 == a3:
    print("1 число уникально")



