"""RockPaperScissor"""

def main():
    """RockPaperScissor"""
    game_value = input()
    player_a_score, player_b_score = 0, 0
    temp_idx = 0
    while temp_idx < len(game_value):
        player_a = game_value[temp_idx]
        player_b = game_value[temp_idx + 1]
        
        if player_a == "R" and player_b == "P":
            player_b_score += 1
        elif player_a == "P" and player_b == "R":
            player_a_score += 1
        
        if player_a == "S" and player_b == "P":
            player_a_score += 1

        temp_idx += 2
    
    if player_a_score == player_b_score:
        print("DRAW %d" % player_a_score)
    elif player_a_score > player_b_score:
        print("A win %d-%d" % (player_a_score, player_b_score))
    else:
        print("B win %d-%d" % (player_b_score, player_a_score))

        
            
    # player_a = []
    # player_b = []
    # players_score = [0, 0]
    # temp_idx = 1
    # for value_x in game_value:
    #     if temp_idx % 2 == 1:
    #         player_a.append(value_x)
    #     elif temp_idx % 2 == 0:
    #         player_b.append(value_x)
    #     temp_idx += 1
        
    # print(player_a)
    # print(player_b)

    # for idx in range(len(player_a)):
    #     if player_a[idx] == player_b[idx]: #เสมอ
    #         players_score[0] += 1
    #         players_score[1] += 1
    #         continue

    #     if player_a[idx] == "R" and player_b[idx] == "P":
    #         players_score[1] += 1
    #     elif player_b[idx] == "P" and player_a[idx] == "R":
    #         players_score[0] += 1

    #     if player_a[idx] == "S" and player_b[idx] == "P":
    #         players_score[0] += 1
    #     elif player_b[idx] == "P" and player_a[idx] == "S":
    #         players_score[1] += 1
            

    
main()
# txt = input() #PRPRRSSRRRSSSSRRPSPPPRSR len
#               #01234567
# txt_index = 0
# while ...
#     a = txt[0] #2
#     b = txt[1] #3
#     if ... a == "" and b == ""

#     suma
#     if ... b == "" and a == ""
#     sumb
#     txt_index += 2

