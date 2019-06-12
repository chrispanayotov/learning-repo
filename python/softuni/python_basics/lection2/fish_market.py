# Calculate how much money Gosho needs to buy fish from the market

skumria = float(input()) # Price for a kg
caca = float(input())  # Price for a kg

palamud = float(input()) # Amount in kg
safrid = float(input()) # Amount in kg
midi = int(input()) # 7.50 bgn

palamud_price = skumria + skumria * 0.60
safrid_price = caca + caca * 0.80
total_palamud = palamud * palamud_price
total_safrid = safrid * safrid_price
total_midi = midi * 7.50
total =  total_palamud + total_safrid + total_midi
print(f"{total:.2f}")