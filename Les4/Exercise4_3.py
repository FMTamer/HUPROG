with open('kaartnummers', 'r') as kaartnr:
    infile = kaartnr.readlines()
    lijst = []
    for line in infile:
        infilelijst = line.split(" ")
        nummers = infilelijst[0]
        nummers = nummers.replace(',' , '')
        lijst.append(nummers)

print('Deze file telt', len(infile), 'regels')
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(max(lijst),infile.index(max(infile)) + 1 ))


kaartnr.close()
