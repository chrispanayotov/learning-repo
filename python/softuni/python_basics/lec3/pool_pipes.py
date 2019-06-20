v = int(input()) # pool volume in litres
p1 = int(input()) # debit of pipe1 /hour
p2 = int(input()) # debit of pipe2 /hour
h = float(input()) # how many hours the worker is missing

volume_p1 = h * p1
volume_p2 = h * p2
total_volume = volume_p1 + volume_p2

if total_volume <= v:
    percent_filled = (total_volume / v) * 100 # % of the pool filled in
    percent_p1 = (volume_p1 / total_volume) * 100 # % of contribution of p1
    percent_p2 = (volume_p2 / total_volume) * 100 # % of contribution of p2
    print(f"The pool is {percent_filled:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
else:
    total_overfilled = abs(v - total_volume)
    print(f"For {h:.2f} hours the pool overflows with {total_overfilled:.2f} liters.")