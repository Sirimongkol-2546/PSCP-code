"""[Recommend] BTSMRT"""
def main():
    """[Recommend] BTSMRT"""
    day = input()
    age = float(input())
    hight = float(input())
    if day == "Children Day" and age < 14 and hight <= 140:
        print("FREE")
    elif age < 14 and hight < 90:
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print("PAY")
main()
