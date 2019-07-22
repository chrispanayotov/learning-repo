# You have been tasked to create an ordered database of websites. For the task
# you will need to create a class Website, which will have a Host, a Domain and Queries.
# Input: softuni | bg | user,course,homework;
# Output: https://www.softuni.bg/query?=[user]&[course]&[homework]

class Website:
    def __init__(self, host, domain, querries=None):
        self.host = host
        self.domain = domain
        self.querries_list = querries


websites_list = []

data = input().split(' | ')

while data[0] != 'end':
    host = data[0]
    domain = data[1]

    try:
        querries_list = data[2].split(',')
        website_obj = Website(host, domain, querries_list)
    except:
        website_obj = Website(host, domain)

    websites_list.append(website_obj)

    data = input().split(' | ')

for website in websites_list:
    if website.querries_list != None:
        print(f"https://www.{website.host}.{website.domain}/query?=", end='')
        for query in website.querries_list:
            if query == website.querries_list[-1]:
                print(f"[{query}]")
            else:
                print(f"[{query}]&", end='')
    else:
        print(f"https://www.{website.host}.{domain}")
