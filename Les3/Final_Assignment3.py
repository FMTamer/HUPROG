def standaardprijs(afstandKM):
    if afstandKM >= 50:
        return afstandKM * 0.60 + 15
    elif afstandKM <= 0:
        return 0
    else:
        return afstandKM * 0.80

dagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == False:
            return prijs * .70
        if weekendrit == True:
            return prijs * .65
    else:
        if weekendrit == True:
            return prijs * .6
        else:
            return prijs

print(ritprijs(55, True, 20))


# TEST RESULTATEN
# Negatieve afstand

print ("Afstanden bij -1")
standaardprijs(-1)
print (ritprijs(11,False,-1))
standaardprijs(-1)
print (ritprijs(12,False,-1))
standaardprijs(-1)
print (ritprijs(64,False,-1))
standaardprijs(-1)
print (ritprijs(65,False,-1))
print ("")
#-------------------------------------
standaardprijs(-1)
print (ritprijs(11,True,-1))
standaardprijs(-1)
print (ritprijs(12,True,-1))
standaardprijs(-1)
print (ritprijs(64,True,-1))
standaardprijs(-1)
print (ritprijs(65,True,-1))
print ("")
#//////////////////////////////////////////
# Afstand gelijk aan 0
#/////////////////////////////////////////
print ("Bij 0")
standaardprijs(0)
print (ritprijs(11,False,0))
standaardprijs(0)
print (ritprijs(12,False,0))
standaardprijs(0)
print (ritprijs(64,False,0))
standaardprijs(0)
print (ritprijs(65,False,0))
print ("")
#-------------------------------------
standaardprijs(0)
print (ritprijs(11,True,0))
standaardprijs(0)
print (ritprijs(12,True,0))
standaardprijs(0)
print (ritprijs(64,True,0))
standaardprijs(0)
print (ritprijs(65,True,0))
print ("")
#//////////////////////////////////////////
# Afstand hoger dan 0
#/////////////////////////////////////////
print ("Bij 1")
standaardprijs(1)
print (ritprijs(11,False,1))
standaardprijs(1)
print (ritprijs(12,False,1))
standaardprijs(1)
print (ritprijs(64,False,1))
standaardprijs(1)
print (ritprijs(65,False,1))
print ("")
#-------------------------------------
standaardprijs(1)
print (ritprijs(11,True,1))
standaardprijs(1)
print (ritprijs(12,True,1))
standaardprijs(1)
print (ritprijs(64,True,1))
standaardprijs(1)
print (ritprijs(65,True,1))
print ("")
#//////////////////////////////////////////
# Afstand hoger dan 50
#/////////////////////////////////////////
print ("Bij 51")
standaardprijs(51)
print (ritprijs(11,False,51))
standaardprijs(51)
print (ritprijs(12,False,51))
standaardprijs(51)
print (ritprijs(64,False,51))
standaardprijs(51)
print (ritprijs(65,False,51))
print ("")
#-------------------------------------
standaardprijs(51)
print (ritprijs(11,True,51))
standaardprijs(51)
print (ritprijs(12,True,51))
standaardprijs(51)
print (ritprijs(64,True,51))
standaardprijs(51)
print (ritprijs(65,True,51))
print ("")
#//////////////////////////////////////////
