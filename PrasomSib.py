"""PrasomSib"""
def main():
    """input"""
    text = input()
    count = 0
    for i in range(len(text)-1):
        total = 0
        for j in text[int(i):]:
            total += int(j)
            if total == 10:
                count += 1
                break
    print(count)
main()
