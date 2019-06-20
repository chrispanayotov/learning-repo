n_edin_lev = int(input())
n_dva_leva = int(input())
n_pet_leva = int(input())
amount = int(input())

for i in range(0, n_edin_lev+1):
    for j in range(0, n_dva_leva+1):
        for k in range(0, n_pet_leva+1):
            if i * 1 + j * 2 + k * 5 == amount:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {amount} lv.")