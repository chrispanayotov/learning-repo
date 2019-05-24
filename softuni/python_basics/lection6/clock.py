hours = 0
minutes = 0
seconds = 0

for i in range(86400):
    print(f"{hours} : {minutes} : {seconds}")
    seconds += 1
    if seconds > 59:
        minutes += 1
        seconds = 0
    if minutes > 59:
        hours += 1
        minutes = 0