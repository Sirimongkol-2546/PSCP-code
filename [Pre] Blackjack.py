"""Blackjack"""
def main():
    """input"""
    num = int(input())
    score = 0
    ace = 0
    for _ in range(num):
        card = input()
        if card == 'J' or card == 'Q' or card == 'K' or card == "10":
            score += 10
        elif card in "23456789":
            score += int(card)

        elif card == 'A':
            score += 11
            ace += 1

    while score > 21 and ace > 0:
        score -= 10
        ace -= 1
    print(score)
main()
