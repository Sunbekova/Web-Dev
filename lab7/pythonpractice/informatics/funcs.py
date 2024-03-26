a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a, b, c, d))

def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a

    result = 1
    for _ in range(n):
        result *= a
    
    return result


a = float(input())
n = int(input())

print(power(a, n))


def xor(x, y):
    if x + y == 1:
        print(1)
    else:
        print(0)
x = int(input())
y = int(input())
xor(x, y)