bedrag = 4356.0

try:
    aantal = int(input('Hoeveel mensen gaan er mee op reis? : '))
    prijs = bedrag / aantal

    if prijs < 0:
        print('Negatieve getallen zijn niet toegestaan!')
    else:
        print('Het bedrag per persoon is: €{}'.format(prijs))
except ZeroDivisionError:
    print('Delen door nul is niet toegestaan!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')
