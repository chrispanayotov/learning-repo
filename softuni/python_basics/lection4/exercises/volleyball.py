import math
leap = input() # leap or normal year
p = int(input()) # vacation days wihout weekends
h = int(input()) # weekends when travelling to home town

weekends_sf = 48 - h
games_sf = weekends_sf * .75
games_ht = h
games_sf_vac = p * (2.0 / 3)
total_games = games_sf + games_ht + games_sf_vac

if leap == "leap":
    total_games += total_games * 0.15

print(f"{math.floor(total_games)}")