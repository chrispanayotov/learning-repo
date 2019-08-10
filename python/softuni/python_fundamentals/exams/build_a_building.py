budget = float(input()) # budget required to finish the building
capital = float(input()) # total capital collected
n_investors = int(input()) # number of investors

collected_money = 0
is_funded = False

for investor in range(1, n_investors+1):
	if capital >= budget:
		is_funded = True
		break
	investment = float(input())
	capital += investment
	print(f"Investor {investor} gave us {investment:.2f}.")

if is_funded or capital >= budget:
	print(f"We will manage to build it. Start now! Extra money - {abs(capital - budget):.2f}.")
else:
	print(f"Project can not start. We need {abs(budget - capital):.2f} more.")