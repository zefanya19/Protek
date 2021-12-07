
File = open('bilangan.txt', 'r')
genap = 0
ganjil = 0
for x in File:
    if int(x) % 2 == 0:
        genap += 1
    else:
        ganjil += 1

File.close()
hasil = {'genap' : genap, 'ganjil' : ganjil}
print('Banyaknya bilangan genap  : ', hasil.get('genap'))
print('Banyaknya bilangan ganjil : ', hasil.get('ganjil'))




