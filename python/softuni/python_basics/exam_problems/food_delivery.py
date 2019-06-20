chicken_menus = int(input()) * 10.35
fish_menus = int(input()) * 12.40
veggie_menus = int(input()) * 8.15

total = chicken_menus + fish_menus + veggie_menus
dessert = total * .20
resut = total + dessert + 2.50

print(f"Total: {resut:.2f}")