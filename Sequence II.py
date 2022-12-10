"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    here = 0
    for i in range(1, num*2, 2):
        here += i
        print(here, end=" ")
main()
