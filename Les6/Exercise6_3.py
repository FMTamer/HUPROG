klas = {}

invoer = input('Voer een naam in: ')

while invoer is not '':

    if invoer not in klas:
        klas[invoer] = 1
    else:
        klas[invoer] += 1
    invoer = input('Voer een naam in: ')

print(klas)
