grondgetallen = [4, 5, 3]

def kwadraten_som(grondgetallen):
    return sum(i*i for i in grondgetallen if i > 0)

print(kwadraten_som(grondgetallen))



