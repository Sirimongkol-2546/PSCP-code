"""Dart"""
import math
def main():
    """input Dart"""
    num = int(input())
    count = 0
    for _ in range(num):
        pos = input()
        pos = pos.split(" ")
        this_x = int(pos[0])
        this_y = int(pos[1])
        rad = math.sqrt((this_x**2)+(this_y**2))
        if rad <= 2:
            count += 5
        elif rad <= 4:
            count += 4
        elif rad <= 6:
            count += 3
        elif rad <= 8:
            count += 2
        elif rad <= 10:
            count += 1
    print(count)
main()
