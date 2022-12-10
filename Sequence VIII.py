"""Sequence VIII"""
def kat(numstart, numstop):
    """AjanKat"""
    for too in range(1, numstop+1):
        if too == numstop:
            for phavit in range(1, numstart+1):
                print('{:02}'.format(phavit), end=" ")
        else:
            print('  ', end=" ")
    print()

def main():
    """Sequence VIII"""
    num = int(input())
    for i in range(1, num+1):
        kat(i, num-i+1)
main()
