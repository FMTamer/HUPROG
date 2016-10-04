cursus_cijfer = {
    'Kees': 2.1,
    'Piet': 6.8,
    'Timmy': 3.6,
    'Johan': 9.5,
    'Frank': 10,
    'Timmy2': 8.2,
    'Tom': 5.2,
    'Henk': 1,
}
print('Deze personen hebben een cijfer die hoger is dan een 9.0!')
for naam in cursus_cijfer.keys():
    if cursus_cijfer[naam] >= 9:
        print('ez')
