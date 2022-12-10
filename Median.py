"""Median"""
import math
def median():
    """input"""
    med = []
    num = int(input())
    for _ in range(1, num+1):
        num2 = int(input())
        med.append(num2)
        med.sort()

    check = len(med)
    check2 = check % 2
    check3 = check / 2
    if check2 % 2 != 0 and check3 != 0: #odd
        check3 = math.ceil(check3)
        print("%.1f" %med[check3-1])
    if check2 % 2 == 0 and check3 != 0:
        total = (med[int(check3-1)] + med[int(check3)])/2
        print("%.1f" %total)
median()
