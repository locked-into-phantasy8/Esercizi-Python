import csv
immagini = []
with open('giocodiscrittura.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader: 
            immagini.append(row)

print(immagini)


