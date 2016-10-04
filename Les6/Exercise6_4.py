bruin = {
    'Boxtel', 'Best', 'Beukenlaan',
    'Eindhoven', 'Helmond\'t Hout', 'Helmond',
    'Helmond Brouwhuis', 'Deurne',
    }
groen = {'Boxtel', 'Best', 'Beukenlaan',
         'Eindhoven', 'Geldrop', 'Heeze',
         'Weert'
         }

print('Deze plaatsen komen voor in beide trajecten: ')
print(bruin & groen)
print('\n')
print('Dit is hoe het traject bruin verschilt van groen ')
print(bruin - groen)
print('\n')

print('Dit zijn alle station voor de trajecten: ')
print(bruin | groen)
print('\n')

