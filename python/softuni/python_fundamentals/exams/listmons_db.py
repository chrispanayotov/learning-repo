class Player:
    def __init__(self, player_name, score_list):
        self.player_name = player_name
        self.score_list = score_list


players_list = []

while True:
    data = input().split(' -> ')
    name = data[0]

    if name == 'report':
        break

    scores = list(map(int, data[1].split(', ')))

    player = Player(name, scores)
    players_list.append(player)

command = input().split()

while command[0] != 'end':

    if command[0] == 'score':

        summed_scores_list = []

        for player in players_list:
            summed_score = sum(player.score_list)
            summed_score_player = Player(player.player_name, summed_score)
            summed_scores_list.append(summed_score_player)

        if command[1] == 'ascending':
            for player in sorted(summed_scores_list, key=lambda p: (p.score_list, p.player_name)):
                print(f"{player.player_name}: {player.score_list}")
        if command[1] == 'descending':
            for player in sorted(summed_scores_list, key=lambda p: (-p.score_list, p.player_name)):
                print(f"{player.player_name}: {player.score_list}")

    elif command[0] == 'numberOfGames':

        number_of_games_list = []

        for player in players_list:
            number_of_games = len(player.score_list)
            n_games_player = Player(player.player_name, number_of_games)
            number_of_games_list.append(n_games_player)

        if command[1] == 'ascending':
            for player in sorted(number_of_games_list, key=lambda p: (p.score_list, p.player_name)):
                print(f"{player.player_name}: {player.score_list}")
        if command[1] == 'descending':
            for player in sorted(number_of_games_list, key=lambda p: (-p.score_list, p.player_name)):
                print(f"{player.player_name}: {player.score_list}")

    command = input().split()