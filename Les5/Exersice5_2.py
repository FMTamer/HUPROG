strings = eval(input("Geef een lijst met minimaal 10 strings: "))
vierletterstrings = []
for woord in strings:
    if len(woord) == 4:
        vierletterstrings.append(woord)

print('Dit is een lijst met alle vier-letter strings erin: \n', vierletterstrings)
