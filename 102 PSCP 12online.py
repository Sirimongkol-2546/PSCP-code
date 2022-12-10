"""12 ก.ย online PSCP"""
"""functions"""
import math

#print(int('111', 2))
#print(int('A', 16))
#print(int('B', base=16))
#help(math)

#hypot รับargument กี่ตัวก็ได้
#print(math.hypot(3, 4))
#print(math.hypot(1,1,1,1,1,1,1))


virus = "Oooooooooo"
count = 0
for char in virus:
    if char == "o":
        count += 1
print(count)

help(str)