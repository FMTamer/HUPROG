stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert",
            "Roermond", "Sittard", "Maastricht"]

def inlezen_beginpunt():
    status = False
    while status == False:
        beginstation = input('Wat is je beginstation? : ')
        if beginstation not in stations:
            print('Deze trein komt niet in' + str(beginstation))
        else:
            return beginstation

def inlezen_eindpunt(begin):
    status = False
    while status == False:
        eindstation = input('Wat is je eindstation? : ')
        if eindstation not in stations or stations.index(begin) < stations.index(eindstation):
            print('Deze trein komt niet in' + str(eindstation))
        else:
            return eindstation
def omroepen_reis(beginomroep,eindomroep):
    trajectnrbegin = stations.index(beginomroep) + 1
    trajectnreind = stations.index(eindomroep) + 1
    trajectafstand = trajectnreind - trajectnrbegin
    trajectprijs = trajectafstand * 5
    print('\nReisGegevens:')
    print("\nHet beginstation " + beginomroep + " is het " + str(trajectnrbegin) + "e station in het traject")
    print("Het eindstation " + eindomroep + " is het " + str(trajectnreind) + "e station in het traject")
    print("De afstand bedraagt " + str(trajectafstand) + " stations")
    print("De prijs van het kaartje is " + str(trajectprijs) + " euro")

    tussenstopsA = stations.index(beginomroep) + 1
    tussenstopsB = stations.index(eindomroep) - 1

    print("Jij stapt in de trein in: " + str(beginomroep))
    for tussenstops in stations[tussenstopsA:tussenstopsB]:
        print("- " + tussenstops)
    print("Jij stapt uit de trein in: " + str(eindomroep))

begin = inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
omroepen_reis(begin, eind)
