import datetime
import csv

bestand = 'inloggers.csv'

naam = input('Wat is je achternaam? ')

while naam != '':
    voorl = input('Wat zijn je voorletters? ')
    gbdatum = input('Wat is je geboortedatum? ')
    email = input('Wat is je e-mail adres? ')
    #======


#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file.
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %y %H:%M:%S")
