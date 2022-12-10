"""Sequence VII"""

def kat(numstop):
    """AjarnKat"""
    for phavit in range(1, numstop+1):
        if phavit == numstop:
            print(phavit)
        else:
            print(phavit, end=" ")

def main():
    """Sequence VII"""
    num = int(input())
    for i in range(1, 2*num):
        if i > num:
            kat(i-(i%num)*2)
        else:
            kat(i)
main()
