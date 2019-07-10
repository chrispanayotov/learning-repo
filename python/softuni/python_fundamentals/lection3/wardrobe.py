# Search through a wardrobe and look for a certain garment (X) to wear
# If the clothing and color matches X (is in the wardrobe) print (found!)
# Also, print out the contents of the wardrobe and the amount for each item

n = int(input())
wardrobe = {}

# Filling in the wardrobe
for i in range(n):
    data = input()
    color, clothes = data.split(' -> ')
    clothes = clothes.split(',')

    if color not in wardrobe.keys():
        wardrobe[color] = []
    wardrobe[color].extend(clothes)

# Target color and dress that we are searching for
color, dress = input().split(' ')

wardrobe_counted = {}

# Counting the items in the wardrobe and searching for the target dress
for key, value in wardrobe.items():
    wardrobe_counted[key] = {item: value.count(item) for item in value}

for key, clothes_list in wardrobe_counted.items():
    print(f"{key} clothes:")
    # Getting out each garment from the list of clothes and printing out their number
    for item, counted in clothes_list.items():
        if color in key and dress in item:
            print(f"* {item} - {counted} (found!)")
        else:
            print(f"* {item} - {counted}")