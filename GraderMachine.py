"""GraderMachine"""
def main():
    """GraderMachine"""
    numstart = int(input())
    numstop = int(input())
    total = 0
    print("pass :", end=" ")
    if numstart <= numstop:
        for i in range(numstart, numstop+1):
            if i%2 == 0:
                total += i
                print(i, end=" ")
    else:
        for i in range(numstart, numstop-2, -1):
            if i%2 == 0:
                total += i
                print(i, end=" ")
    print("\nSum :", total)
main()
