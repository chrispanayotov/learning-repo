# WORK IN PROGRESS, CAN'T SOLVE FOR NOW

class User:
    def __init__(self, username, received_msgs):
        self.username = username
        self.received_messages = received_msgs

    def receive_msg(self):
        pass


class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


data = input()
users_to_register = []
users_array = []
received_msgs = []


def create_user(username):
    new_user = User(username)
    return new_user


while data[0] != 'exit':
    if data[0] == 'r':
        data = data.split(' ')
        users_to_register.append(data[1])
    else:
        sender, _, receiver, message = data.split(' ')


        
    data = input()