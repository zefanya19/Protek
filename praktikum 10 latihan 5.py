dataFile = open('databil.txt', 'r')
for x in dataFile:
    mengambil = x.split('|')
    menghasilkan = int(mengambil[0]) + int(mengambil[1])
    print(menghasilkan)

dataFile.close()








