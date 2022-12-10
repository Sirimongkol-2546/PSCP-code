"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    for i in range(1, num**2+1):
        if i%num == 0:
            print(i)
        else:
            print(i, end=" ")
main()

