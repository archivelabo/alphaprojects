# .replace()

def monkeyWord(s): # Is it a monkey word
    if aWord(s):
        return True
    for i, c in enumerate(s): # i is the iterating variable, while c will be s[i]
        if c == "N":
            if aWord(s[:i]) and monkeyWord(s[i + 1:]):
                return True
    return False

def aWord(s):
    if s == "A":
        return True
    if len(s) >= 1 and s[0] == "B" and s[-1] == "S" and monkeyWord(s[1:-1]):
        return True
    return False

s = input()
while s != "X":
    print("YES" if monkeyWord(s) else "NO")
    s = input()