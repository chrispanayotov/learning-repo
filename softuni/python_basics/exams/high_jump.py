import sys
target_height = int(input())

starting_ledge_height = target_height - 30
total_jumps = 0
failed_jumps = 0

for height in range(starting_ledge_height, target_height + 1, 5):
    for i in range(3):
        current_jump = int(input())
        if current_jump > height:
            total_jumps += 1
            failed_jumps = 0
            break
        elif current_jump <= height:
            failed_jumps += 1
            total_jumps += 1
            if failed_jumps == 3:
                print(f"Tihomir failed at {height}cm after {total_jumps} jumps.")
                sys.exit()

print(f"Tihomir succeeded, he jumped over {height}cm after {total_jumps} jumps.")