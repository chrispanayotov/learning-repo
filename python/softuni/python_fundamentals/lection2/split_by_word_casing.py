# Read a text, split it into words and distribute them into 3 lists.
# • Lower-case words like “programming”, “at” and “databases” – consist of lowercase letters only.
# • Upper-case words like “PHP”, “JS” and “SQL” – consist of uppercase letters only.
# • Mixed-case words like “C#”, “SoftUni” and “Java” – all others.

data = input()
lower_case = []
mixed_case = []
upper_case = []

# Remove any unnecessary symbols from the list
cleaner = (',',';', ':', '. ', '!', '(', ')', '"', "'", '\\', '/', '[', ']',"''",'  '," .",'.')

for char in cleaner:
    data = data.replace(char, " ")

words = [word for word in data.split()]

for word in words:
    if word == word.lower() and word.isalpha() == True:
        lower_case.append(word)
    elif word == word.upper() and word.isalpha() == True:
        upper_case.append(word) 
    else:
        mixed_case.append(word)

print(f"Lower-case: {', '.join(str(x) for x in lower_case)}")
print(f"Mixed-case: {', '.join(str(x) for x in mixed_case)}")
print(f"Upper-case: {', '.join(str(x) for x in upper_case)}")