def string_compression(string):
    compression = ""
    count = 1
    i = 0
    while i < len(string):
        if i < len(string) - 1 and string[i] == string[i+1]:
            count += 1
        else:
            compression += string[i] + str(count)
            count = 1
        i += 1
    if len(string) < len(compression):
        return string
    else:
        return compression