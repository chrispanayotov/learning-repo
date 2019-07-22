class Website:
    Host = ''
    Domain = ''
    Queries = []

    def __init__(self, inputLine):
        self.parseInput(inputLine)

    def parseInput(self, inputLine):
        lineData = inputLine.split(' | ')
        self.Host = lineData[0]
        self.Domain = lineData[1]
        if len(lineData) > 2:
            self.Queries = lineData[2].split(',')

    def getOutput(self):
        queryString = ''
        if len(self.Queries) > 0:
            queryString = '/query?=[' + ']&['.join(self.Queries) + ']'
        return 'https://www.' + self.Host + '.' + self.Domain + queryString


websites = []
data = input().splitlines()
for line in data:
    if line != 'end':
        websites.append(Website(line))

for website in websites:
    print(website.getOutput())
