a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')


x=int(input("x"))
y=int(input("y"))
print(("NO","YES")[(x==1)==(y==1)])


x = int(input())
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)


a = int(input())
b = int(input())
if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)
