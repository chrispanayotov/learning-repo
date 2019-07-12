# You have been tasked to create a Console Social Media Database.
# If you receive the post command, you must create a post with the given name.
# If you receive the like command you must add a like to the given post.
# If you receive the dislike command you must add a dislike to the given post.

data = input().split()

posts_dict = {}

while data[0] != 'drop':
    command = data[0]
    post = data[1]

    if command == 'post':
        posts_dict[post] = {'likes': 0, 'dislikes': 0, 'comments': None}
    elif command == 'like':
        if post in posts_dict.keys():
            posts_dict[post]['likes'] += 1
    elif command == 'dislike':
        if post in posts_dict.keys():
            posts_dict[post]['dislikes'] += 1
    elif command == 'comment':
        commentator = data[2]
        content = ' '.join(data[3:])
        if post in posts_dict.keys():
            if not posts_dict[post]['comments']:
                posts_dict[post]['comments'] = []
            posts_dict[post]['comments'].append({commentator: content})

    data = input().split(' ')

for post, values in posts_dict.items():
    print(f"Post: {post} | Likes: {values['likes']} | Dislikes: {values['dislikes']}")
    print("Comments:")
    if values['comments']:
        for comment in values['comments']:
            for item in comment.items():
                commentator = item[0]
                content = item[1]
                print(f"*  {commentator}: {content}")
    else:
        print(None)