"""Hamburger"""
def main():
    """Hamburger"""
    wide_l = int(input())
    wide_r = int(input())
    wide_l2 = "|" * wide_l
    wide_r2 = "|" * wide_r
    meat1 = "*" * wide_l * 2
    meat2 = "*" * wide_r * 2
    print(wide_l2 + meat1 + meat2 + wide_r2)
main()
