"""Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    xxx = int(input())
    per_alice = abs(xxx - alice)
    per_bob = abs(xxx - bob)
    if per_alice > per_bob:
        print("Bob", per_bob)
    elif per_alice < per_bob:
        print("Alice", per_alice)
    else:
        print("Sundaes", per_bob)
main()
