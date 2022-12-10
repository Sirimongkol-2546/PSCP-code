"""Compound Interest"""
def main():
    """ช่วยมาคุมพฤติกรรมอีสันดานนี่หน่อย"""
    money = int(input())
    interest = float(input())
    year = int(input())
    for _ in range(year):
        money = money*(1+(interest/100))
    print("%.2f" %money)
main()
