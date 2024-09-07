following_set = set()
followers_set = set()

def bandit():
    # Read following.txt and followers.txt into sets
    with open('following.txt', 'r', encoding='utf-8') as following_file:
        for line in following_file:
            following_set.add(line.strip())

    with open('followers.txt', 'r', encoding='utf-8') as followers_file:
        for line in followers_file:
            followers_set.add(line.strip())

    # Find the users in following but not in followers
    bandits = following_set - followers_set

    # Write the information of non-followers and find their instagram id, along with link
    with open('Bandits.txt', 'w', encoding='utf-8') as result_file:
        for bandit in bandits:
            result_file.write(f"{bandit} - www.instagram.com/{bandit}\n")
            print(f"{bandit} Found")