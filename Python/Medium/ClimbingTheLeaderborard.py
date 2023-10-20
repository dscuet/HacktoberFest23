def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked_scores = sorted(set(ranked), reverse=True)
    player_ranks = []
    i = len(ranked_scores) - 1
    
    for score in player:
        while i >= 0 and score >= ranked_scores[i]:
            i -= 1
        if i == -1:
            player_ranks.append(1)
        else:
            player_ranks.append(i + 2)
    
    return player_ranks