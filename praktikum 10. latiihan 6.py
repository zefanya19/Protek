try:
    file = input('Nama file yang dienkripsi : ')
    key = int(input('Input key\t\t\t: '))
    dataFile = open(file + '.txt', 'r')
    isi = dataFile.read()
    hasil = ' '

    for x in isi:
        if x == ' ':
            hasil += x
        elif x.islower():
            hasil += chr((ord(x) + key - 97) % 26 + 97)
        else:
            hasil += chr((ord(x) + key - 65) % 26 + 65)

    dataFile.close()
    enkripsi = open(file + '.encrypt', 'w')
    enkripsi.write(hasil)
    enkripsi.close()
    print('File enkripsi : {}.encrypt'.format(file))

except FileNotFoundError:
    print('File tidak ditemui')








