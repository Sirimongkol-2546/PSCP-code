"""Century"""
import math
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        year = input()
        year_front = year[0:4]
        year_back = int(year[5:]) # B.E. 2564
        if year_front == "B.E." and year_back >= 544:
            year_back = int(year_back) - 543
            year_back = year_back/100
            print(math.ceil(year_back))

        elif year_front == "A.D." and year_back >= 1:
            year_back = int(year_back)/100
            print(math.ceil(year_back))

        else:
            print("ERROR")
main()
