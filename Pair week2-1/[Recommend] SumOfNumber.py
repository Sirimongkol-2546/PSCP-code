"""[Recommend] SumOfNumber"""
def main():
    """input"""
    total = int(input())
    mysum = 0
    while True:
        num = int(input())
        if num == -1:
            break
        mysum += num
        if mysum == total:
            break
    print(mysum)
main()
