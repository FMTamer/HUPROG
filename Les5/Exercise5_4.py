nummers = []
invoer = eval(input('Geef een getal: '))
while invoer != 0:
    nummers.append(invoer)
    invoer = eval(input('Geef een getal: '))
if invoer == 0:
    print('Er zijn {} getallen ingevoerd, de som is {}'.format(len(nummers), sum(nummers)))
