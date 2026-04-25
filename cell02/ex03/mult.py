#!/usr/bin/env python3
x=int(input("Number1:"))
y=int(input("number2:"))
c=x*y
print(x,"*",y,"=",c)

if c>0:
    print("The result is positive.")
if c<0:
    print("The result is negative.")
if c==0:
    print("The result is positive and negative.")