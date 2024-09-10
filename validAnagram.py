def valid_anagram(first, second):
    if len(first) != len(second):
        return False

    lookup = {}

    for letter in first:
        if letter in lookup:
            lookup[letter] += 1
        else:
            lookup[letter] = 1
    print(lookup)

    for letter in second:
        if letter not in lookup or lookup[letter] == 0:
            return False
        lookup[letter] -= 1

    return True


print(valid_anagram("anagrams", "nagaramm"))
