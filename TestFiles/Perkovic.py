# hoofdstuk 3

def pay(aantalUren, uurloon):
    if aantalUren > 40:
        return 40 * uurloon + (aantalUren - 40) * uurloon * 1.5
    else:
        return aantalUren * uurloon

print(pay(65, 10))

grades = [[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]

def avg(lst):
    for avggrades in lst:
        print(sum(avggrades) / len(avggrades))

avg(grades)

# hoofdstuk 4

lst = ["aap", "noot", "mies", "blaa", "fooo", "bar", "bnb"]

beginIndex = 3
endIndex = 6

for index_woord in range(beginIndex, endIndex):
    woord = lst[index_woord]
    print(woord)

# perkovic 4.18

table = str.maketrans(',.;\n', 4*' ')
newS = s.translate(table)
print(newS)
newS = newS.strip()
newS = newS.lower()
aantal = newS.count('it was')

print(aantal)
newS = newS.replace('was,', 'is')
print(newS
      listS = newS.split()
      print(listS)









