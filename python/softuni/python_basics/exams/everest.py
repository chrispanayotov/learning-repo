current_height = 5364
target = 8848
days = 1
climbed_meters = 0
camp = input()

while True:
    if camp == "END":
        break
    elif camp == "Yes":
        days += 1
    if days > 5:
        break

    climbed_meters = int(input())
    current_height += climbed_meters
    
    if current_height >= target:
        break
    camp = input()
    
if current_height >= target:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{current_height}")