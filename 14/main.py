def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    print("Strs with [1:] is: " , strs[1:])
    for s in strs[1:]:
        print("s is: ", s)
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            print("prefix is: ", prefix)
            if not prefix:
                return ""
            print("________________")
    return prefix


longestCommonPrefix(["flower", "float", "flight"])
