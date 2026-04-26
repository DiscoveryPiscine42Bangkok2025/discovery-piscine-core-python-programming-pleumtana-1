#!/usr/bin/env python3
age=int(input("Tell me your age:"))
x=10
print(end="You are currently ")
print(age,end='')
print(end=" years old.")
print()
while x<=30:
    print(end="In ")
    print(x,end='')
    print(end=" years")
    print(end="you'll be ")
    print(age+x,end='')
    print(" years old.")
    x=x+10
