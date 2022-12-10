"""Meteorite"""
def meteo():
    """input"""
    wight_a = float(input())
    broken_b = int(input())
    wight_c = float(input())
    count = 0
    rate = 0
    while wight_a >= wight_c:
        wight_a = wight_a/broken_b
        total = broken_b**rate
        rate += 1
        count += total
    print(count)
meteo()
