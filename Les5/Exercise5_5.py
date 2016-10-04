invoer = input('Geef een string van vier letters: ')
print(invoer + ' heeft ' + str(len(invoer)) + ' letters')

while (len(invoer) != 4):
    invoer = input('Geef een string van vier letters: ')
    print(invoer + ' heeft ' + str(len(invoer)) + ' letters')
    if len(invoer) == 4:
        print('inlezen van correcte string: {} is geslaagd'.format(invoer))
        break
