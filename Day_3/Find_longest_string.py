def get_longest(*words):
    if len(words) == 0:
        return None
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

print(get_longest('ARUSH', 'PAYAL', 'zarina', 'yogesh'))