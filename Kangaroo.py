"""Kangaroo"""
def main():
    """จิงโจ้"""
    num_a = int(input()) # 3
    num_b = int(input()) # 5
    num_c = int(input()) # 9
    num_x = max(num_c - num_b, num_b - num_a)
    print(num_x - 1)
main()
