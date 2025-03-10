n, m = [int(x) for x in input().split()]
rankings = {i: f"T{i}" for i in range(1, n+1)}
for i in range(m):
    winner, loser = input().split()
    for rank,team in rankings.items():
        if team == winner:
            winning_rank = rank
        elif team == loser:
            losing_rank = rank
    if winning_rank > losing_rank:
        rankings[winning_rank] = loser
        for j in range(winning_rank-losing_rank-1):
            rankings[losing_rank+j] = rankings[losing_rank+j+1]
        rankings[winning_rank-1]=winner
for rank, team in rankings.items():
    print(team, end=" ")

    
        
