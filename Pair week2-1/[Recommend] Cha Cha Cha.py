"""[Recommend] Cha Cha Cha"""

def main():
    """input"""
    day = int(input())
    count = 0
    for _ in range(day):
        hour = float(input())
        if hour % 1 != 0:
            hour += 1
        hour //= 1
        count += hour
    print("%d" %(count*8720))
main()
