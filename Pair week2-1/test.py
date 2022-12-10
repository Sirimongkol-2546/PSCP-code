"""[Recommend] RockPaperScissor"""
def main():
    """[Recommend] RockPaperScissor"""
    game_value = input()
    player_a_score, player_b_score = 0, 0
    for _ in range(len(game_value)):
        player = game_value[0:2:2]
        if player == "RS" or player == "PR" or player == "SP":
            player_a_score += 1
        elif player == "SR" or player == "RP" or player == "PS":
            player_b_score += 1
    if player_a_score > player_b_score:
        print("A win %d-%d" %(player_a_score, player_b_score))
    elif player_a_score < player_b_score:
        print("B win %d-%d" %(player_b_score, player_a_score))
    else:
        print("DRAW %d" %(player_a_score))      
main()