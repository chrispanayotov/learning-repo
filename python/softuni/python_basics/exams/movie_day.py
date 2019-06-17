import math
total_shooting_time = int(input())
n_scenes = int(input())
scene_duration = int(input())

preparation = total_shooting_time * .15
shooting_time_req = n_scenes * scene_duration + preparation

if shooting_time_req >= total_shooting_time:
    print(f"Time is up! To complete the movie you need {round(abs(shooting_time_req - total_shooting_time))} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {round(abs(shooting_time_req - total_shooting_time))} minutes left!")