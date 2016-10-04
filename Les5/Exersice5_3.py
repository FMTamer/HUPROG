invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

getallenlijst = []
getallenlos = invoer.split("-")
for nummers in getallenlos:
    getallenlijst.append(int(nummers))

print('Gesorteerde list van ints: {}'.format(sorted(getallenlijst)))
print('Grootste getal: {} en Kleinste getal: {}'.format(max(getallenlijst), min(getallenlijst)))
print('Aantal getallen: {} en Som van de getallen: {}'.format(len(getallenlijst), sum(getallenlijst)))
print('Gemiddelde: {}'.format(sum(getallenlijst) / len(getallenlijst)))

