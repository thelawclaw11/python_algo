def get_words(digits, words):
    table = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    result = []

    def F(digs, accum):
        if accum in words:
            result.append(accum[:])

        if not digs:
            return

        for letter in table[digs[0]]:
            F(digs[1:], accum + letter)

    F(digits, "")
    return result

print(get_words("269", {"any", "box", "boy", "cow", "young", "chud"}))
