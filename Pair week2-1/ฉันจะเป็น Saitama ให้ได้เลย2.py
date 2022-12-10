"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main():
    """input"""
    need1, need2, need3, need4 = int(input()), int(input()), int(input()), int(input())
    do1, do2, do3, do4 = int(input()), int(input()), int(input()), int(input())
    day1 = math.ceil(need1 / do1)
    day2 = math.ceil(need2 / do2)
    day3 = math.ceil(need3 / do4)
    day4 = math.ceil(need4 / do3)
    count = 0
    if count < day1:
        count = day1
    if count < day2:
        count = day2
    if count < day3:
        count = day3
    if count < day4:
        count = day4
    print(count)
main()
