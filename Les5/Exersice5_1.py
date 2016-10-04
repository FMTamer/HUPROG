def seizoen(maand):
    if 3 <= maand <= 5:
        return 'lente'
    elif 6 <= maand <= 8:
        return 'zomer'
    elif 9 <= maand <= 11:
        return 'herfst'
    elif maand == 12 or maand <= 2:
        return 'winter'

print(seizoen(10))
