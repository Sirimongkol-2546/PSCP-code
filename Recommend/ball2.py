"""ball2"""
def main():
    """input"""
    num = float(input())
    total = 0
    while True:
        num = num  * (3/5)
        if num < 0.01:
            break
        total = 0
    print(total)
main()
