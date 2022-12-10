"""ATM"""
def main():
    """ATM"""
    money = int(input())
    num = '' # for spilt
    while True:
        num = input().split()
        if num[-1] == "END":
            break
        elif num[0] == "D": # Dคือฝาก W คือถอน
            money += int(num[1])
        elif num[0] == "W":
            if money < int(num[1]):
                money -= money
            elif money >= 0:
                money -= int(num[1])
    print(money)
main()
