"""[Recommend] Tax"""
def main():
    """[Recommend] Tax"""
    old = int(input())
    cc_car = int(input())
    total1 = 0
    total2 = 0

    if cc_car <= 600:
        total1 += cc_car*0.5
    elif cc_car <= 1800:
        total1 += ((cc_car - 600) * 1.5) + 300
    elif cc_car > 1800:
        total1 += ((cc_car - 1800)*4) + 2100

    if old == 6:
        total2 = total1 * 0.9
    elif old == 7:
        total2 = total1 * 0.8
    elif old == 8:
        total2 = total1 * 0.7
    elif old == 9:
        total2 = total1 * 0.6
    elif old >= 10:
        total2 = total1 * 0.5

    if old <= 5:
        print('%.2f' %total1)
    else:
        print('%.2f' %total2)
main()
