import xmltodict

with open('stations') as stations:
    filecontent = stations.read()
    doc = xmltodict.parse(filecontent)
    doc = doc['Stations']
    station_elementen = doc['Station']
    print('Dit zijn de codes en types van de 4 stations:')
    for element in station_elementen:
        print('{} - {}'.format(element['Code'], element['Type']))
    print('\nDit zijn alle stations met één of meer synoniemen:')
    for i in station_elementen:
        if i['Synoniemen'] is not None:
            print('{} - {} en {}.'.format(i['Code'], i['Synoniemen']['Synoniem'][0], i['Synoniemen']['Synoniem'][1]))
    print('\nDit is de lange naam van elk station:')
    for i in station_elementen:
        print('{} - {}'.format(i['Code'], i['Namen']['Lang']))
