import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %y %H:%M:%S")

outfile = open('hardlopers.txt', 'a')

outfile.write('{0} {1}\n'.format(s, ', Kemal'))


outfile.close()
