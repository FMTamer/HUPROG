def convert(Celcius):
    tempF = Celcius * 1.8 + 32
    return tempF

def table(celciusmin, celciusmax):
    titel ='{:5}    {:5}'.format('F', 'C')
    print(titel)
    for x in range(celciusmin, celciusmax+1 , +10):
        temp='{:5}  {:5}'.format(convert(x), x)
        print(temp)


print(table(-30 , 40))

