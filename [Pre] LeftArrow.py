"""[Pre] LeftArrow"""
def main():
    """LeftArrow"""
    wide = int(input()) #ความกว้างของป้ายไฟ #row
    high = int(input()) #ความสูงป้ายไฟ (เลขคี่) #col
    high //= 2
    for i in range(high):
        for _ in range(high):
            print('', end='')
        for _ in range(wide):
            print('*', end='')
        print()

    for i in range(high):
        for _ in range(0, i):
            print(' ', end='')
        for _ in range(wide):
            print('*', end='')
        print()
main()
