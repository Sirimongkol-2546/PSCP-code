"""GCD_v1"""
def main():
    """ฉันเหนื่อยมากนะพี่จี้"""
    num1 = int(input())
    num2 = int(input())
    range1 = max(num1, num2)
    for i in range(range1, 0, -1):
        if num1 %i == 0 and num2 % i == 0:
            print(i)
            break
main()
