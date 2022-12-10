"""Quadrant"""
def main():
    """Quadrant"""
    num = int(input()) #x
    num2 = int(input()) #y
    if num > 0 and num2 > 0: #++
        print("Q1")
    elif num < 0 and num2 > 0: #-+
        print("Q2")
    elif num < 0 and num2 < 0: #--
        print("Q3")
    elif num > 0 and num2 < 0: #+-
        print("Q4")
    elif num > 0 or num < 0 and num2 == 0:
        print("X")
    elif num2 > 0 or num2 < 0 and num == 0:
        print("Y")
    elif num == 0 and num == 0:
        print("O")
main()
