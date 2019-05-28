wins = 0
loses = 0
total_matches = 0

while True:
    tournament_name = input()

    if tournament_name == "End of tournaments":
        break

    n_games = int(input())

    for game in range(1, n_games + 1):
        score_team1 = int(input())
        score_team2 = int(input())
        if score_team1 > score_team2:
            wins += 1
            print(f"""Game {game} of tournament {tournament_name}: win with {score_team1 - score_team2} points.""")
        else:
            loses += 1
            print(f"Game {game} of tournament {tournament_name}: lost with {score_team2 - score_team1} points.")

print(f"{wins / (wins + loses) * 100:.2f}% matches win")
print(f"{loses / (wins + loses) * 100:.2f}% matches lost")