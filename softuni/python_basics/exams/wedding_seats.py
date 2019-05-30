last_sector = input()
total_rows = int(input())
odd_seats_total = int(input())

total_seats = 0
sector_start = 65
sector_end = ord(last_sector)
seats_start = 97
seats_end = seats_start + odd_seats_total

for sector in range(sector_start, sector_end + 1):
    if sector > sector_start:
        total_rows += 1
    for row in range(1, total_rows + 1):
        if row % 2 == 0:
            for seat_even in range(seats_start, seats_end + 2):
                total_seats += 1
                print(f"{chr(sector)}{row}{chr(seat_even)}")
        else:
            for seat_odd in range(seats_start, seats_end):
                total_seats += 1
                print(f"{chr(sector)}{row}{chr(seat_odd)}")

print(f"{total_seats}")