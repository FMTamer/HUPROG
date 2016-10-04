with open('kaartnummers', 'r') as kaartnr:

    infile = kaartnr.readlines()
    for line in infile:
        infilelijst = line.split(",")
        nummers = infilelijst[0]
        namen = infilelijst[1]
        namen = namen.replace('\n' , '')
        print(namen, 'heeft kaartnummer : ', nummers)

kaartnr.close()

