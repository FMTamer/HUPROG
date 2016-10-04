import random
def monopolyworp():
    status = True
    worpnr = 1
    while status == True:
        worp1 = random.randrange(1,7)
        worp2 = random.randrange(1,7)
        if worp1 != worp2:
            print('{} + {} = {}'.format(worp1, worp2, worp1 + worp2))
            status = False
        else:
            worpnr += 1
            print('{} + {} = {}(dubbel)'.format(worp1, worp2, worp1 + worp2))
            if worpnr == 3:
                status = False
                print('{} + {} = {}(direct naar gevangenis)'.format(worp1, worp2, worp1 + worp2))
    return
monopolyworp()
