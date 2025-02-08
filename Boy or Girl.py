def determine_gender(username):
    distinct_characters = set(username)
    if len(distinct_characters) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

username = input().strip()
determine_gender(username)
