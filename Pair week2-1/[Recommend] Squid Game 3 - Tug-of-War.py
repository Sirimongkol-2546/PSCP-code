"""[Recommend] Squid Game 3 - Tug-of-War"""

def main():
    """input"""
    counta = 0
    countb = 0
    for _ in range(10):
        num = int(input())
        counta += num
    for _ in range(10):
        num = int(input())
        countb += num
    if counta > countb:
        print("B")
    elif counta < countb:
        print("A")
    else:
        print("AB")
main()
