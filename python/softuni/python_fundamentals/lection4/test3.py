class User:
    Username = ''
    ReceivedMessages = []
    
    def __init__(self, Username):
        self.Username = Username
        
    def addMessage(self, fromUser, content):
        self.ReceivedMessages.append(Message(fromUser, content))

class Message:
    Content = ''
    Sender = User
    
    def __init__(self, sender, content):
        self.Content = content
        self.Sender = sender
    
users = dict()

inputLine = input()
while inputLine != 'exit':
    lineData = inputLine.split(' ')
    if lineData[0] == 'register':
        # register line
        userName = lineData[1]
        users[userName] = User(lineData[0])
    else:
        # message line
        fromUser = lineData[0]
        toUser = lineData[2]
        message = lineData[3]
        if set([fromUser, toUser]).issubset(users.keys()):
            # both users are registered
            # get user objects:
            sender = users[fromUser]
            receiver = users[toUser]
            receiver.addMessage(sender, message)

    inputLine = input()

conversationUsers = input().split(' ')
fromUser = conversationUsers[0]
toUser = conversationUsers[1]


if set([fromUser, toUser]).issubset(users.keys()):
    # check if both users are registered
    firstUser = users[fromUser]
    secondUser = users[toUser]
    # get max of both users' messages count
    messagesCount = max(len(firstUser.ReceivedMessages), len(secondUser.ReceivedMessages))
    for i in range(0, messagesCount - 1):
        if i < len(firstUser.ReceivedMessages):
            # check if we haven't ran out of messages for the first user
            message = firstUser.ReceivedMessages[i]
            print(message.Sender.Username + ': ' + message.Content)
        if i < len(secondUser.ReceivedMessages):
            # check if we haven't ran out of messages for the second user
            message = secondUser.ReceivedMessages[i]
            print(message.Content + ' :' + message.Sender.Username)