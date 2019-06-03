import sys
name = input()

score = 0
top_score = -sys.maxsize-1

while name != "STOP":
    for letter in range(len(name)):
        score += (ord(name[letter]))
    
    if score > top_score:
        top_score = score
        winner = name
        
    score = 0
    name = input()

print(f"Winner is {winner} - {top_score}!")