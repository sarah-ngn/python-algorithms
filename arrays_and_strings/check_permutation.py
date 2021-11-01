def check_permutation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    characters = [0] * 123
    for i in str_1:
        characters[ord(i)] += 1
    for j in str_2:
        characters[ord(j)] -= 1
        if characters[ord(j)] < 0:
            return False
    return True
