"""Sequence VI"""
def main():
    """Sequence VI"""
    num = int(input())
    for i in range(1, num+1):
        for too in range(1, i+1):
            if i == too:
                print(too)
            else:
                print(too, end=" ")
main()
