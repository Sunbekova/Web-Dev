a=int(input())
b=int(input())
c=(a**2+b**2)**0.5
print(c)

n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')

n = int(input())
k = int(input())
x = k // n
y = k - (x * n)
print(x)
print(y)


n = int (input ())
k = int (input ())
x = k // n
y = k - (x * n)
print(k // n)
print(k - (k // n) * n)

a = int(input())
b = int(input())
print((a * b) % 109)