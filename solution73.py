# Дан алфавит (1,2,3,4,5,6,7,8). Построить все возможные слова длины 6, в которых три символа 2

def permutations(alphabet, kolvo):
    if kolvo == 1:
        return [[x] for x in alphabet]

    result = []
    for i in range(len(alphabet)):
        currentNumber = alphabet[i]
        otherAlphabet = alphabet[:i] + alphabet[i + 1:]
        for permutation in permutations(otherAlphabet, kolvo - 1):
            result.append([currentNumber] + permutation)

    return result

def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)

    if r == 0:
        yield ()
    else:
        for i in range(n):
            for tail in combinations_with_replacement(pool[i:], r-1):
                yield (pool[i],) + tail

n = ["1", "3", "4", "5", "6", "7", "8"]               

result = []

for ch in list(combinations_with_replacement(n, 3)):
    for el in list(permutations(list(["2", "2", "2", ch[0], ch[1], ch[2]]), 6)):
        result.append(" ".join(str(x) for x in el))

result = set(result)

with open("solution73.txt", "w") as file:
    for res in result:
        file.write(res + "\n")
    file.write(f"Amount: {len(result)}")
