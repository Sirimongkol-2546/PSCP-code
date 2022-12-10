"""[Recommend] RockPaperScissor"""
def main():
    """[Recommend] RockPaperScissor"""
    game = input()
    score_a, score_b = 0, 0
    for player in game:
        if player[0] == "S" and player[1] == "P" or\
            player[0] == "P" and player[1] == "R" or\
            player[0] == "R" and player[1] == "S":
            score_a += 1
        else:
            score_b += 1  

    if score_a > score_b:
        print("A win %d-%d" %(score_a, score_b))
    elif score_a < score_b:
        print("B win %d-%d" %(score_b, score_a))
    else:
        print("DRAW %d" %score_b)
main()
