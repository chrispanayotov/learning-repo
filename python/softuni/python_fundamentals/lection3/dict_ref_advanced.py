# Create a dict, which knows how to reference itself. Advanced version
# Example - 
# I: Donald -> 2, 2, 2; Isacc -> 1; George -> John ; John -> Isacc; end
# O: Donald === 2, 2, 2, Isacc === 1, John === 1

data = input().split(' -> ')
dict_ref = {}

while data[0] != 'end':
    name = data[0]
    item = data[1].split(', ')

    # Checks if item is a number string that can be casted to int. 
    # If it is, creates a list entry:
    if item[0].isdigit():
        if name not in dict_ref.keys():
            dict_ref[name] = []
        dict_ref[name].extend(item)
    # If the item is a name that is already a key in dict_ref, 
    # create a new entry with a reference to the value already stored.
    # If it's not ignore the input:
    else:
        if item[0] in dict_ref.keys():
            if name not in dict_ref.keys():
                dict_ref[name] = []
            dict_ref[name].extend(dict_ref[item[0]])

    data = input().split(' -> ')

for name, value in dict_ref.items():
    print(f"{name} === ", end='')
    print(*value, sep=', ')