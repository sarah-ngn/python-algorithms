def palindrome_permutation(string):
    characters = [0] * 123
    odd = 0
    for i in string:
        if i.isalpha():
            characters[ord(i)] += 1
            if characters[ord(i)] % 2 != 0:
                odd += 1
            else:
                odd -= 1
    return odd <= 1

