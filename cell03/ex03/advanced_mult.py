#!/usr/bin/env python3
import sys
y=0
if len(sys.argv) > 1:
    arg = sys.argv[1]

    if arg.isdigit():
       pass
    else:
        print("none")
        
for y in range(11):
    print("table be",y, end=" :")
    x=0
    while x <= 10:        
        print(x*y , end=' ')
        x=x+1
    print()