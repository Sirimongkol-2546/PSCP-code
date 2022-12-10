"""Circular II"""
def main():
    """Circular II"""
    x_1 = float(input())
    y_1 = float(input())
    rad = float(input())
    x_2 = float(input())
    y_2 = float(input())
    rad2 = float(input())

    top = (x_2 - x_1)**2
    bottom = (y_2 - y_1)**2
    total = (top + bottom)**0.5
    if total < rad+rad2:
        print("Yes")
    elif total >= rad+rad2:
        print("No")
main()
