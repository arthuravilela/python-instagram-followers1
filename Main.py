import json

def jsonRead(filePath):
    with open(filePath, encoding='utf-8') as file:
        return json.load(file)

def getInstagramUsername(data):
    if isinstance(data, dict) and "relationships_following" in data:
        data = data["relationships_following"]

    usernames = []
    for element in data:
        username = element["string_list_data"][0]["value"]
        usernames.append(username)
    return usernames

def createNotFollowBackFile(usernames, filename='not_follow_back.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for i, username in enumerate(usernames, start=1):
                file.write(f"{i}. {username}\n")
        print("File created.")
    except Exception as e:
        print("Error: ", e)

jsonFollowers = jsonRead('followers_1.json')
jsonFollowing = jsonRead('following.json')

followers = set(getInstagramUsername(jsonFollowers))
following = set(getInstagramUsername(jsonFollowing))

notFollowBack = following - followers
notFollowBackSorted = sorted(notFollowBack)

createNotFollowBackFile(notFollowBackSorted)
