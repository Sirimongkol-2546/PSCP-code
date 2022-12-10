"""Difference"""
def setisus():
    """ถ้ายังทำผิดอีก ฉันว่าฉันลาออกไปเป็นโคโยตี้ดีกว่า"""
    set_a, set_b = set(), set()
    num_n, num_m = int(input()), int(input())
    for _ in range(num_n):
        num_a = int(input())
        set_a.add(num_a)
    for _ in range(num_m):
        num_b = int(input())
        set_b.add(num_b)
    val = set_a - set_b
    val = sorted(val)
    for i in val:
        print(i, end=" ")

setisus()
