# Modify the data to give only the usernames

search_text = "'s profile picture"
replace_text = ""

def modFollowers():
    with open('followers.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.replace(search_text,replace_text)
    with open('followers.txt', 'w', encoding='utf-8') as file:
        file.write(content)
    print("Followers List modified...")

def modFollowing():
    with open('following.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.replace(search_text,replace_text)
    with open('following.txt', 'w', encoding='utf-8') as file:
        file.write(content)
    print("Following List modified...")