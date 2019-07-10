# Write a program that receives a list of username-password pairs in 
# the format “{username} -> {password}” and stores them in a dictionary.
# After that the when the user tries to login, check if the info match.
# Example - Input: ivan_ivanov -> java123; Output (when usr & pass are correct): ivan_ivanov: logged in successfully
data = input()
database = {}

# Creating the database
while data != 'login':
    username, password = data.split('->')
    username, password = username.strip(), password.strip()
    database[username] = password
    data = input()

# Receiving the logins and checking if username and pass are correct
data = input()
failed_logins = 0

while data != 'end':
    username, password = data.split('->')
    username, password = username.strip(), password.strip()
    if username in database.keys() and password in database.values():
        print(f"{username}: logged in successfully")
    else:
        print(f"{username}: login failed")
        failed_logins += 1
    data = input()

print(f"unsuccessful login attempts: {failed_logins}")