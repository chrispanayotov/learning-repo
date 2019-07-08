# Sort out a database full of information about employees
# If input value is int, store it as name and age
# If input value is float, store it as name and salary
# If input value is string, store it as name and position

data = input()

salaries = {}
positions = {}
age_dict = {}

while data != 'filter base':
    data = data.split(' -> ')
    # Checks if the string from value is an int or float and casts it accordingly
    try:
        data[1] = int(data[1])
    except:
        try:
            data[1] = float(data[1])
        except:
            pass

    # Store the information in the corresponding dictionary according to the
    # data type that's stored in value
    if isinstance(data[1], int) == True:
        age_dict[data[0]] = data[1]
    elif isinstance(data[1], float) == True:
        salaries[data[0]] = data[1]
    else:
        positions[data[0]] = data[1]

    data = input()

# Print the corresponding dictionary according to the received keyword 
data = input()

def output(dict_type, key_word):
    for k, v in dict_type.items():
        print(f"Name: {k}\n{key_word}: {v}")
        print("=" * 20)


if data == 'Age':
    output(age_dict, data)
elif data == 'Salary':
    output(salaries, data)
else:
    output(positions, data)