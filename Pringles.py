"""Pringles"""
def main():
    """input"""
    line1 = input()
    line2 = input()
    line3 = input()
    finger = int(input())
    eat = line2.count(')', 0, finger)
    line2n = ' '*finger + line2[finger:]
    left = line2n.count(')')
    print(eat)
    if left > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(line1)
    print(line2n)
    print(line3)
main()
# __________
#))))))))))|
#__________
#10
