a, b = map(int, input().split())

for num in range(a, b + 1):
    if num % 2 == 0:
        print(num, end=" ")

a, b, c, d = map(int, input().split())

found = False

for num in range(a, b + 1):
    if num % d == c:
        print(num, end=" ")
        found = True

if not found:
    print("Нет чисел на отрезке от", a, "до", b, "с остатком", c, "при делении на", d)


a, b = map(int, input().split())

found = False

for num in range(a, b + 1):
    if int(num ** 0.5) ** 2 == num:
        print(num, end=" ")
        found = True

if not found:
    print("Нет полных квадратов на отрезке от", a, "до", b)


x, d = map(int, input().split())

count = str(x).count(str(d))
print(count)


x = input()


sum_of_digits = 0

for digit in x:
    sum_of_digits += int(digit)

print(sum_of_digits)


x = input()
print(x[::-1])

x = int(input())


for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
        print(i)
        break
else:
    print(x)


x = int(input())


divisors = []

for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        divisors.append(i)
        if i != x // i:
            divisors.append(x // i)

divisors.sort()
for divisor in divisors:
    print(divisor, end=' ')


x = int(input())

divisors_count = 1

for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
        exponent = 0
        while x % i == 0:
            x //= i
            exponent += 1
        divisors_count *= (exponent + 1)

if x > 1:
    divisors_count *= 2

print(divisors_count)

total_sum = 0

for _ in range(100):
    number = int(input())
    total_sum += number

print(total_sum)


N = int(input())

total_sum = 0

for _ in range(N):
    number = int(input())
    total_sum += number

print(total_sum)

binary_number = input()

decimal_number = 0
power = len(binary_number) - 1

for digit in binary_number:
    decimal_number += int(digit) * 2 ** power
    power -= 1

print(decimal_number)


N = int(input())
zero_count = 0
for _ in range(N):
    number = int(input())
    if number == 0:
        zero_count += 1

print(zero_count)
