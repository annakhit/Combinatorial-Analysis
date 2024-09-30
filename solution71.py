# Дан алфавит (1,2,3,4,5,6,7,8). Составить все возможные размещения по 5 элементов данного | алфавита и вывести их в файл. Последней строкой в файле указать количество элементов.

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

alphabet = [1, 2, 3, 4, 5, 6, 7, 8]
kolvo = 5
result = permutations(alphabet, kolvo)

with open("solution71.txt", "w") as file:
    for res in result:
        file.write(" ".join(str(x) for x in res) + "\n")
    file.write(f"Amount: {len(result)}")