"""[Recommend] Ball"""
def main():
    """input"""
    hight = float(input())
    total = -1
    while hight >= 0.01:
        hight = hight * (3/5)
        total += 1
    print(total)
main()
