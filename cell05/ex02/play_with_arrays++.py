#!/usr/bin/env python3
number=[2, 8, 9, 48, 8, 22, -12, 2]
new=[]
add=[]
print(number)

for x in number:
    new.append(x+2)
    if x > 5:
        add.append(x+2)

print(add)
