def isAnagram(s: str, t: str) -> bool:
    # empty case
    if len(s) is not len(t):
        return False

    
    chars_one = {}
    for i in range(len(s)):
        if s[i] in chars_one:
            chars_one[s[i]] += 1
        else:
            chars_one[s[i]] = 1
    chars_two = {}
    for j in range(len(t)):
        if t[j] in chars_two: 
            chars_two[t[j]] += 1
        else:
            chars_two[t[j]] = 1
    
    return chars_one == chars_two


print(isAnagram(s, "racecar"))
