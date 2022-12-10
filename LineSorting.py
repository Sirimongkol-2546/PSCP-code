"""LineSorting"""
def main():
    """input"""
    line = []
    num = int(input())
    for _ in range(1, num+1):
        text = input()
        line.append(text)
        line.sort(key=len)
    for i in line:
        print(i)
main()
