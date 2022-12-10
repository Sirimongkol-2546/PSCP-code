"""[Recommend] SumOfNumber"""
def main():
    """input"""
    iwant = int(input())
    count = 0
    while True:
        num = int(input())
        if num == -1:
            break
        count += num
        if count == iwant:
            break
    print(count)
main()
