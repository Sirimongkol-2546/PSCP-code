"""Key"""
def main():
    """Key"""
    numbers = input()
    total = 0
    for num in numbers:
        total += int(num)
    last_3_idx = int(numbers[-3:]) * 10
    total += last_3_idx
    if total < 1000:
        total += 1000
    print(str(total)[-4:])
main()
    