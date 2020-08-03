def open_or_senior(data):
    final = []
    for duplo in data:
        final.append(
            'Senior') if duplo[0] >= 55 and duplo[1] >= 7 else final.append('Open')
    return final


open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)])
open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)])
