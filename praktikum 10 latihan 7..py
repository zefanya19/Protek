try:
    file = input('Nama file yang dienkripsi : ')
    key = int(input('Input key                       : '))
    dataFile = open(file + '.encrypt', 'r')
    isi = dataFile.read()
    hasil = ' '

    for x in isi:
        if x == ' ':
            hasil += x
        elif x.islower():
            hasil += chr((ord(x) - key - 97) % 26 + 97)
        else:
            hasil += chr((ord(x) - key - 65) % 26 + 65)

    dataFile.close()
    enkripsi = open(file + '.encrypt.decrypt', 'w')
    enkripsi.write(hasil)
    enkripsi.close()
    print('File enkripsi : {}.encrypt.decrypt'.format(file))

except FileNotFoundError:
    print('File tidak ditemui')







