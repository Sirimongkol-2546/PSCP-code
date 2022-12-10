"""HowLong"""
def main():
    """input"""
    num = int(input())
    total = abs(num)
    look = 0
    for _ in str(total):
        look += 1
    print(look)
main()
