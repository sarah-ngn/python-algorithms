def one_away(str_1, str_2):
    if len(str_1) - len(str_2) > 1 | len(str_2) - len(str_1) > 1:
        return False
    else:
        characters = [0] * 123
        dif = 0
        for i in str_1:
            characters[ord(i)] += 1
        for j in str_2:
            characters[ord(j)] -= 1
            if characters[ord(j)] < 0:
                dif += 1
        if dif > 1:
            return False
        else:
            return True
