"""Heron of Alexandria"""
import math
def heron():
    """How to calculate"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    cal_s = (num_a+num_b+num_c)/2
    area = math.sqrt(cal_s*(cal_s-num_a)*(cal_s-num_b)*(cal_s-num_c))
    print("%.3f" %area)
heron()
