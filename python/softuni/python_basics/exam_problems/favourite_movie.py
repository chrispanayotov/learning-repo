import sys
total = 0
max_score = -sys.maxsize-1
best_movie = None
counter = 0

for i in range(1, 8):
    movie = input()

    if movie == "STOP":
        break
    
    for j in range(len(movie)):
        total += (ord(movie[j]))

        if ord(movie[j]) > 64 and ord(movie[j]) < 90:
            total -= len(movie)
        elif ord(movie[j]) > 96 and ord(movie[j]) < 123:
            total -= len(movie) * 2

    if total > max_score:
        max_score = total
        best_movie = movie
    
    total = 0
    counter += 1

if counter == 7:
    print(f"The limit is reached.")

print(f"The best movie for you is {best_movie} with {max_score} ASCII sum.")