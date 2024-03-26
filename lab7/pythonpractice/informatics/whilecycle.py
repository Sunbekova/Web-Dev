N = int(input())

number = 1
while number ** 2 <= N:
    print(number ** 2, end=" ")
    number += 1

number = int(input())

for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        print(i)
        break
else:
    print(number)


N = int(input())
power_of_two = 1
while power_of_two <= N:
    print(power_of_two, end=' ')
    power_of_two *= 2


N = int(input())
if N == 1:
    print("YES")
else:
    while N > 1:
        if N % 2 != 0:
            print("NO")
            break
        N //= 2
    else:
        print("YES")


N = int(input())
k = 0
power_of_two = 1
while power_of_two < N:
    k += 1
    power_of_two *= 2

print(k)
