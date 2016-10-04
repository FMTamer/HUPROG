import requests
import xmltodict

auth_details = ('Frank.mohammed.tamer@gmail.com', 'f4J4sVsW5QcombdwV1zP7hej_3unwSweNKkkNyVUIsQiT5_LG3PNgw')

api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(api_url, auth=auth_details)
vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']
    vertrektijd = vertrek['VertrekTijd']
    vertrektijd = vertrektijd[11:16]
    print('Om {} vertrekt er een trein naar {}'.format(vertrektijd,eindbestemming))

##
