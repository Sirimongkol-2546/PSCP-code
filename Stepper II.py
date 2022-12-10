"""Stepper II"""
def main():
    """Stepper II input"""
    num_m = int(input())
    num_n = int(input())
    if num_m < num_n:
        for i in range(num_m, num_n+1, 1):
            print(i)

    elif num_m >= num_n:
        for i in range(num_m, num_n-1, -1):
            print(i)
main()
