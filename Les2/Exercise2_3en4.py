Leeftijd = int(input("Geef je leeftijd: "))
NL_Pasport = input("Heeft u een Nederlandse paspoort ja/nee : ")

if int(Leeftijd) >= 18 and NL_Pasport == "ja":
    print("Gefiliciteerd, je mag stemmen!")
else:
    print("Helaas, je mag niet stemmen")
