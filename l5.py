n = int(input("Введите целое число: "))
x = 0
while x <= n:
    print(x)
    x += 1


n = int(input("Введите число: "))
x = 0
while x <= n:
    print(x, end=" ")
    x += 1
print()


x= input("Введите строку: ")
n = int(input("Введите число: "))
for i in range(1, n + 1):
    print(i, ":", x, sep="")


n = int(input("Введите число: "))
for i in range(n, -1, -1):
    print(i)
print("Пуск!")


n = int(input("Введите число: "))
for i in range(n + 1):
    cube = i ** 3
    print("Куб числа", i, "равен", cube)


n = int(input("Введите число: "))
if n < 0:
    print("Факториал не определён для отрицательных чисел.")
else:
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)


n = int(input("Введите числа: "))
total = 0
for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    total += num
print("Сумма чисел", total)


n = int(input("Введите числа: "))
x = 1
for _ in range(n):
    num = int(input())
    if num != 0:
        x *= num
print("Произведение (нули пропущены):", x)


n = int(input("Введите числа: "))
print(n, end=": ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")


n = int(input(("Введите числа: ")))
total = 0
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        total += num
    else:
        total -= num
print("Знакочередующаяся сумма:", total)
