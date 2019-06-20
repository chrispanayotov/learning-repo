budget = float(input())
n_series = int(input())

total_price = 0

for i in range(n_series):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        total_price += series_price - (series_price * .50)
    elif series_name == "Lucifer":
        total_price += series_price - (series_price * .40)
    elif series_name == "Protector":
        total_price += series_price - (series_price * .30)
    elif series_name == "TotalDrama":
        total_price += series_price - (series_price * .20)
    elif series_name == "Area":
        total_price += series_price - (series_price * .10)
    else:
        total_price += series_price
    
if budget >= total_price:
    print(f"You bought all the series and left with {abs(budget - total_price):.2f} lv.")
else:
    print(f"You need {abs(budget - total_price):.2f} lv. more to buy the series!")