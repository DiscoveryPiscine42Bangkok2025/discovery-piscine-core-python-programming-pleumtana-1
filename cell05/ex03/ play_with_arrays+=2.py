#!/usr/bin/env python3
number = [2, 8, 9, 48, 8, 22, -12, 2]

qq = []
print(number)
for x in number:
    if x > 5:
        value = x + 2
        if value not in qq:
            qq.append(value)

print(qq)
