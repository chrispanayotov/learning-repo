movie_name = input()
n_days = int(input())
n_tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())

ticket_price_per_day = n_tickets * ticket_price
total_profits = n_days * ticket_price_per_day
profit_for_cinema = (total_profits * cinema_percent) / 100
total = total_profits - profit_for_cinema

print(f"The profit from the movie {movie_name} is {total:.2f} lv.")