studentcijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]
studentengemiddelde = []

def gemiddelde_per_student(cijferlijst):
    for lijst in studentcijfers:
        cijferstudent = sum(lijst)/len(lijst)
        studentengemiddelde.append(cijferstudent)
    return studentengemiddelde


def gemiddelde_van_alle_studenten(cijferlijst):
    gemiddeldtotaal = sum(studentengemiddelde) / len(studentcijfers)
    return gemiddeldtotaal

print(gemiddelde_per_student(studentcijfers))
print (gemiddelde_van_alle_studenten(studentcijfers))
