# Дан алфавит (1,2,3,4,5,6,7,8). Построить все возможные слова длины 7, в которых ровно один символ повторяется 3 раза и ровно 1 символ повторяется два раза

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

n = ["1", "2", "3", "4", "5", "6", "7", "8"]

result = []

for ch in list(permutations(n, 4)):
    s = [ch[0], ch[0], ch[0], ch[1], ch[1], ch[2], ch[3]]
    for el in list(permutations(s, 7)):
        result.append(" ".join(str(x) for x in el))

result = set(result)

with open("solution72.txt", "w") as file:
    for res in result:
        file.write(res + "\n")
    file.write(f"Amount: {len(result)}")