# WORK IN PROGRESS, CAN'T SOLVE FOR NOW

class User:
    def __init__(self, username):
        self.username = username


class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


def create_user(username):
    new_user = User(username)
    return new_user


data = input()
users_array = []
correspondence_dict = {}

while data != 'exit':
    if data[0] == 'r':
        data = data.split(' ')
        users_array.append(data[1])
    else:
        sender, _, receiver, message = data.split(' ')
        correspondence_dict.setdefault((sender, receiver), [])
        correspondence_dict[sender, receiver].append(message)

    data = input()

sender = []
receiver = []

for sender in correspondence_dict.keys():
    # Goes through the messages of the first sender and then goes through
    # the messages of the second sender. Need to figure a way how to print the
    # first msg of the sender and then the response of the second participant
    for i in range(len(correspondence_dict[sender])):
        print(correspondence_dict[sender][i])