"""Duplicate I"""
def main():
    """ใครมันมือบอนเขียนชื่อตัวเองไปสองกลุ่ม"""
    num1 = int(input())
    num2 = int(input())
    set_m = set()
    set_n = set()
    for _ in range(num1):
        password_m = input()
        set_m.add(password_m)
    for _ in range(num2):
        password_n = input()
        set_n.add(password_n)

    who = set_m.intersection(set_n)
    who_2 = (sorted((who), reverse=True)) #วนจากล่างขึ้นมา
    if who == set():
        print("Nope")
    else:
        for i in who_2:
            print(i)
main()
