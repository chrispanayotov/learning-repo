# Create a dict, which knows how to reference itself
# Example - Input: Entry1 = 10000 Entry2 = 12345 Entry3 = 10101 Entry4 = Entry1
# Entry2 = Entry3 Entry3 = Entry4 end
# Output: Entry1 === 10000 Entry2 === 10101 Entry3 === 10000 Entry4 === 10000

data_input = input().split(' = ')

names_dict = {}

while not data_input[0] == 'end':
    if data_input[1].isdigit():
        key = data_input[0]
        value = int(data_input[1])
        names_dict[key] = value
    else:
        if data_input[1] in names_dict.keys():
            names_dict[data_input[0]] = names_dict[data_input[1]]

    data_input = input().split(' = ')

for k, v in names_dict.items():
    print(f"{k} === {v}")