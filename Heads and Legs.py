"""Heads and Legs"""
def main():
    """Heads and Legs"""
    head = int(input())
    legs = int(input())
    rabbit, ghost = divmod(legs-2 * head, 2)
    bird = head - rabbit
    if rabbit >= 0 and bird >= 0 and ghost == 0:
        print(rabbit, bird)
    else:
        print("Impossible")
main()
