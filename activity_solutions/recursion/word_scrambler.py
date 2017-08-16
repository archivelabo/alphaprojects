def permutations(word):
    ans = []
    if not word:
        ans.append("")
    else:
        previous = permutations(word[1:])
        for permutation in previous:
            for pos in range(len(permutation)): # pos for position
                ans.append(permutation[:pos] + word[0] + permutation[pos:])
            ans.append(permutation + word[0])
    return sorted(ans)
word = input()
for permutation in permutations(word):
    print(permutation)
