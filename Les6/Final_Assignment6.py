naam = input('Voer je naam in: ')
begin = input('Voer je beginstation in: ')
eind = input('Voer je eindstation in: ')

def code(invoerstring):
    lst = []
    for char in invoerstring:
        ASCIINUMMER= ord(char) + 3
        vertaalChar = chr(ASCIINUMMER)
        lst.append(vertaalChar)
    nieuwe_code = ','.join(lst)
    return 'NS kaart-CODE:: {}'.format(nieuwe_code)
invoerstring = (naam+begin+eind)
print(code(invoerstring))

#############################################################################################
##           | Georderned | Muteerbaar | Iterable | Dubbele waarde toegestaan              ##
##-----------|------------|------------|----------|--------------------------              ##
##Tuple      | Ja         | Nee        | Ja       | Ja                                     ##
##Dictionary | Nee        | Ja         | Ja       | Nee                                    ##
##Set        | Nee        | Ja         | Ja       | Nee                                    ##
##List       | Ja         | Ja         | Ja       | Ja                                     ##
#############################################################################################
