"""Inflation"""
def main():
    """input"""
    price_n = int(float(input())*100)
    year_k = int(input())
    for _ in range(year_k):
        price_n = price_n + ((price_n*381)//10000)
    print("%d.%02d" %(price_n//100, price_n%100))
main()
