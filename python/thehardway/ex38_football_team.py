# Find 10 examples of things in the real world that would fit in a list.
# Try writing some scripts to work with them.

# A football team can consist of up to 28 players. 
# 11 main players and the rest are substitutes.
# Practicing making lists with an object in real life - Bayern Munich FC
# Dict of Goalkeepers

goalkeepers = {1: 'Neuer', 26: "Ulreich", 36: "Fructhl", 39: "Hoffmann"}
# Dict of Defenders
defenders = {4: 'Sule', 5: 'Hummels', 8: 'Martinez', 13: 'Rafinha',
            17: 'Boateng', 27: 'Alaba', 32: 'Kimmich'}
# Sort the defenders alphabetically
print(sorted(defenders.items(), key=lambda x: x[1]))
# List of midfielders
midfielders = [["Thiago", "Ribery", "Robben", "Rodriguez", 
                "Goretzka", "Davies", "Gnabry", "Tolisso"
                "Coman", "Sanches"], [6, 7, 10, 11, 18, 19, 22, 24, 29, 35]]

#List of forwards
fowards = [["Lewandowski", "Muller"], [9, 25]]

main_team_numbers = [1, 5, 8, 13, 17, 6, 7, 10, 11, 9, 25]

main_team_names = ["Neuer", "Hummels", "Martinez", "Rafinha", 
                    "Boateng", "Thiago", "Ribery", "Robben", 
                    "Rodriguez", "Lewandowski", "Muller"]

#sub_team_numbers = [26, 36, 39]

#sub_team_names = ["Ulreich", "Fruchtl", "Hoffmann"]
