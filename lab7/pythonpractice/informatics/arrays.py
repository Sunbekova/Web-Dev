a = input().split()
for i in range(0, len(a), 2):
    print(a[i])

s=input()
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')


a = map(int, input().split())
n = 0
for i in a:
    if i > 0:
        n += 1
print(n)

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)

index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)