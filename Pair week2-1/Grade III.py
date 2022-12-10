"""Grade III"""
def main():
    """Grade III"""
    subject = int(input())
    score = 0

    for _ in range(subject):
        num = float(input())
        if num >= 95 and num <= 100:
            score += 4
        elif num >= 90 and num < 95:
            score += 3.5
        elif num >= 85 and num < 90:
            score += 3
        elif num >= 80 and num < 85:
            score += 2.5
        elif num >= 75 and num < 80:
            score += 2
        elif num >= 70 and num < 75:
            score += 1.5
        elif num >= 65 and num < 70:
            score += 1
        elif num >= 60 and num < 65:
            score += 0.5
        elif num >= 0 and num < 60:
            score += 0
    print("%.2f" %(int((score/subject)*100)/100))

main()
