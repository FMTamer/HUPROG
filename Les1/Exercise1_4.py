cijferICOR = 8
cijferPROG = 7
cijferCSN = 4.5

gemiddeld = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = gemiddeld * 30
overzicht = 'Mijn cijfers(gemiddeld een ' + str(gemiddeld) + ') leveren een beloning op van € ' + str(beloning) + ' op!'
print(overzicht)
