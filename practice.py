"""Howlong"""
def main():
    """input"""
    num = int(input())
    num2 = abs(num)
    total = 0
    for _ in str(num2):
        total += 1
    print(total)
main()