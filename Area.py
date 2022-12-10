"""Area"""
def main():
    """Area"""
    num = int(input())
    count = 0
    for _ in range(num):
        text = input().replace(" ", "")
        count += len(text)
    print(count)
main()
