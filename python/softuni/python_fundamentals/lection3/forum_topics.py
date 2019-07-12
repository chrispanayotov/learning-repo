# You have been tasked to store a few forum topics, and filter them by several given tags.
# Example - I: HelloWorld -> hello, forum, topic; HelpWithHomework -> homework, forum, topic
# O: HelloWorld | #hello, #forum, #topic; HelpWithHomework | #homework, #forum, #topic;
# I: filter - forum, topic

data = input()

forum_dict = {}

while data != 'filter':
    topic, tags = data.split(' -> ')
    tags = tags.split(', ')

    if topic not in forum_dict.keys():
        forum_dict[topic] = []
        forum_dict[topic].extend(tags)
    else:
        for tag in tags:
            if tag not in forum_dict[topic]:
                forum_dict[topic].append(tag)

    data = input()

# Create the filter
filter_tags = input().split(', ')

for key in forum_dict.keys():
    count = 0
    for i in range(len(filter_tags)):
        if filter_tags[i] in forum_dict[key]:
            count += 1

    if count == len(filter_tags):
        print(f"{key} | ", end='')
        for tag in forum_dict[key]:
            if tag != forum_dict[key][-1]:
                print(f"#{tag}", end=', ')
            else:
                print(f"#{tag}")