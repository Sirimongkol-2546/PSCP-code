"""Sequence III"""
def main():
    """Sequence III"""
    num = int(input())
    for i in range(2, num+2, 1): #col
        for j in range(i, i+num):
            print(j, end=" ")
        print()
main()
