"""[Recommend] Restaurant"""
def main():
    """input"""
    current = float(input())
    promotion = float(input())
    discount = float(input())
    offer = float(input())
    if current + offer >= promotion:
        pay1 = (current+offer)*(100-discount)/100
    else:
        pay1 = current+offer

    if current >= promotion:
        pay2 = current*(100-discount)/100
    else:
        pay2 = current

    diff = abs(pay1 - pay2)
    if pay1 < pay2:
        print("Yes %.3f" %diff)
    elif pay1 > pay2:
        print("No %.3f" %diff)
    else:
        print("Yes")

main()
