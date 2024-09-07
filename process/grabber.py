# Purpose: Grab the necessary data from another set of data based on a criteria

def grabFollowers():
    # Open the existing file 'test.txt' for reading with UTF-8 encoding
    with open('test.txt', 'r', encoding='utf-8') as source_file:
        # Open the new file 'followers' for writing with UTF-8 encoding
        with open('followers.txt', 'w', encoding='utf-8') as destination_file:
            # Iterate through each line in the source file
            for line in source_file:
                # Check if the line contains the specific string
                if "'s profile picture" in line:
                    # Write the line to the destination file
                    destination_file.write(line)
    print("Followers grabbed...")

def grabFollowing():
    # Open the existing file 'test.txt' for reading with UTF-8 encoding
    with open('test.txt', 'r', encoding='utf-8') as source_file:
        # Open the new file 'followers' for writing with UTF-8 encoding
        with open('following.txt', 'w', encoding='utf-8') as destination_file:
            # Iterate through each line in the source file
            for line in source_file:
                # Check if the line contains the specific string
                if "'s profile picture" in line:
                    # Write the line to the destination file
                    destination_file.write(line)
    print("Following grabbed...")