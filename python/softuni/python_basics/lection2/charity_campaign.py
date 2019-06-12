# Make a program that calculates the gathered funds at a charity campaign
# The gathered money need to be formatted to the 2nd decimal point
campaign_days = int(input())
bakers = int(input())
cakes = int(input())
gaufrettes = int(input())
pancakes = int(input())

cakes_price = cakes * 45
gaufrettes_price = gaufrettes * 5.80
pancakes_price = pancakes * 3.20
total_day = (cakes_price + gaufrettes_price + pancakes_price) * bakers
total_campaign = total_day * campaign_days
result = total_campaign - (total_campaign * 0.125)
print(f"{result:.2f}")
