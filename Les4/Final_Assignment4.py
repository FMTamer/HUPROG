with open('Annuleringen', 'r') as Annuleringen:
    infile = Annuleringen.readlines()
    annuleringen = []
    for line in infile:
        infilelijst = line.split(":")
        annuleringstation = infilelijst[1]
        annuleringstation = annuleringstation.replace('\n' , '')
        annuleringen.append(annuleringstation)
Annuleringen.close()

with open('Treinritten', 'r') as Treinritten:
    infile2 = Treinritten.readlines()
    treinritten = []
    tijden = []
    for line2 in infile2:
        infilelijst2 = line2.split("-")
        treintijd = infilelijst2[0]
        treinritstation = infilelijst2[1]
        treinritstation = treinritstation.replace('\n' , '')
        treinritten.append(treinritstation)
        tijden.append(treintijd)

for station_an,station in zip(annuleringen,treinritten):
   if station_an in treinritten:
        getal = treinritten.index(station_an)
        treinritten.pop(getal)
        tijden.pop(getal)
Treinritten.close()

with open('nieuwe_treinritten', 'w') as nieuwe_treinritten:
    for st,td in zip(treinritten,tijden):
        nieuwe_treinritten.write('%s-%s\n' % (td,st))
nieuwe_treinritten.close()
