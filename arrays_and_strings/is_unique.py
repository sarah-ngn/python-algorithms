def is_unique(string):
    characters = [False] * 123
    for i in string:
        if not characters[ord(i)]:
            characters[ord(i)] = True
        else:
            return False
    return True
