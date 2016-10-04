import csv

with open('bedrijven', 'r') as tickerbestand:
    reader = csv.reader(tickerbestand, delimiter=':')
    print('Voer bedrijfs naam: ')
    bedrijf = input()
    for (key, value) in reader:
        if (key) == bedrijf:
            print('Ticker Symbool: {}'.format(value))
            break
        else:
            print('Dit is geen geldige bedrijfs naam')
    print('Voer Ticker Symbool: ')
    ticker = input()
    for (key, value) in reader:
        if (value) == bedrijf:
            print('Bedrijfs naam : {}'.format(key))
        else:
            print('Dit is geen geldige ticker symbool')
