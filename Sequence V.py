"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    pom = 1
    for i in range(num, 0, -1):
        if pom%7 == 0:
            print(i)
        else:
            print(i, end=" ")
        pom += 1
main()
