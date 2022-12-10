"""Bill"""
def main():
    """input"""
    money = float(input())
    total = money * (10/100) #ค่าบริการ
    if total < 50:
        total = 50
    elif total >= 1000:
        total = 1000

    total = money + total
    total = total * (107/100)
    print("%.2f" %total)
main()
