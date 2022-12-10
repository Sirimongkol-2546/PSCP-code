"""Tuple's Sad life"""
def main():
    """input"""
    num1 = tuple(input().split(" "))
    findtuple = input()
    for _ in range(num1.count(findtuple)):
        for _ in range(num1.count(findtuple)):
            print(num1.index(findtuple), end=" ")
        print()
main()
