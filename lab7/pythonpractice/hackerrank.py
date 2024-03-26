#1
print("Hello, World!")

#2
import math
import os
import random
import re
import sys


def check_weirdness(n):
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

n = int(input().strip())

check_weirdness(n)

#3
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)


#4
a = int(input())
b = int(input())

print(a // b)
print(a / b)

#5
n = int(input())
for i in range(n):
    print(i ** 2)

#6
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input())
print(is_leap(year))

#7
n = int(input())

for i in range(1, n + 1):
    print(i, end="")

#8
n = int(input())
scores = list(map(int, input().split()))
unique_scores = sorted(set(scores), reverse=True)
print(unique_scores[1])

#9
n = int(input())
students = []
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

second_lowest_grade = sorted(set(score for name, score in students))[1]
second_lowest_students = sorted([name for name, score in students if score == second_lowest_grade])
for student in second_lowest_students:
    print(student)

#10
    n = int(input())

student_records = {}

for _ in range(n):
    name, *marks = input().split()
    student_records[name] = list(map(float, marks))

query_name = input()

average_marks = sum(student_records[query_name]) / len(student_records[query_name])

print("{:.2f}".format(average_marks))
