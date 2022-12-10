"""Sequence N"""
def main():
    """Sequence N"""
    num = int(input())
    for row in range(num):
        for col in range(num):
            con1 = col == 0
            con2 = col == num - 1
            con3 = col == row
            if con1 or con2 or con3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main()
