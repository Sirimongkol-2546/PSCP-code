"""Parity"""
def parity():
    """How to parity"""
    num = input()
    text = input()
    count = 0
    for i in num:
        if i == "1":
            count += 1
    if text == "Even":
        if count%2 == 0:
            print(num+"0")
        else:
            print(num+"1")
    if text == "Odd":
        if count%2 != 0:
            print(num+"0")
        else:
            print(num+"1")
parity()
