stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert",
            "Roermond", "Sittard", "Maastricht"]

Beginstation = str(input("Wat is je beginstation? : "))

if Beginstation in stations:
    print("Beginstation is: " + Beginstation)
else:
    Beginstation = "Schagen"
    print("Dit station is niet geldig in dit traject, beginstation is: " + Beginstation)

Eindstation = str(input("Wat is je eindstation? : "))

if Eindstation in stations and stations.index(Beginstation) < stations.index(Eindstation):
    print("Eindstation is: " + Eindstation)
else:
    Eindstation = "Maastricht"
    print("Dit station is niet geldig in dit traject, Eindstation is: " + Eindstation)

trajectnrbegin = stations.index(Beginstation) + 1
trajectnreind = stations.index(Eindstation) + 1
trajectafstand = trajectnreind - trajectnrbegin
trajectprijs = trajectafstand * 5

print("\nReisGegevens:")
print("\nHet beginstation " + Beginstation + " is het " + str(trajectnrbegin) + "e station in het traject")
print("Het eindstation " + Eindstation + " is het " + str(trajectnreind) + "e station in het traject")
print("De afstand bedraagt " + str(trajectafstand) + " stations")
print("De prijs van het kaartje is " + str(trajectprijs) + " euro")

tussenstopsA = stations.index(Beginstation) + 1
tussenstopsB = stations.index(Eindstation) - 1

print("Jij stapt in de trein in: " + str(Beginstation))
for tussenstops in stations[tussenstopsA:tussenstopsB]:
    print("- " + tussenstops)
print("Jij stapt uit de trein in: " + str(Eindstation))

