from collections import deque
from dataclasses import replace

# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(2)
# print(d) # integers/Numeric
# d.clear()
# d.extend('1')
# print(d) # String
# d.extendleft('23458976')
# print(d)
# print(d.count)
# d.pop() # removes extreme right element
# print(d)
# d.popleft() # removes extreme right element
# print(d)
# d.rotate()
# print(d)
"""
The underscore _ is a conventional placeholder variable name in Python. 
It signals to anyone reading the code that the value assigned to this variable during each iteration of the loop is intentionally being 
ignored because it is not used within the loop's body. If the iteration number were needed, a descriptive variable name like i or 
index would be used instead (e.g., for i in range(n):).
"""
n = int(input())
d = deque()

for _ in range(n):
    line = input().split()
    method_name = line[0]

    if len(line) == 2:
        value = line[1]
        if method_name == "append":
            d.append(value)
        elif method_name == "appendleft":
            d.appendleft(value)
    elif method_name == "pop":
        d.pop()
    elif method_name == "popleft":
        d.popleft()

print(*d)
