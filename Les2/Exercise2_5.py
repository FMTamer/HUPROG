s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = ["a", "o", "i", "u", "e"]

for LetterCheck in s:
    if LetterCheck in klinkers:
        print(LetterCheck)
