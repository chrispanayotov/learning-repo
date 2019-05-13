exam_h = int(input())
exam_m = int(input())
arrival_h = int(input())
arrival_m = int(input())

exam_in_minutes = (exam_h * 60) + exam_m
arrival_in_minutes = (arrival_h * 60) + arrival_m

late = arrival_in_minutes - exam_in_minutes
early = exam_in_minutes - arrival_in_minutes

if late > 0:
    print("Late")
    if late <= 59:
        print(f"{late} minutes after the start")
    else:
        hours = late // 60
        minutes = late % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif 0 <= early <= 30:
    print("On time")
    if early != 0:
        print(f"{early} minutes before the start")
elif early > 30:
    print("Early")
    if 30 <= early <= 59:
        print(f"{early} minutes before the start")
    else:
        hours = early // 60
        minutes = early % 60
        print(f"{hours}:{minutes:02d} hours before the start")