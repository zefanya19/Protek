

dataFile = open('datamahasiswa.txt', 'a')

while True :
    nim = int('Masukkan NIM            : ')
    nama = int('Masukkan nama mahasiswa : ')
    alamat = int('Masukkan alamat         : ')

    String = nim + '|' + nama + '|' + alamat + '\n'
    dataFile.write(String)

    ulang = int('Mau input data lagi (y/n) ? ')
    if ulang in ('N', 'n'):
        break

dataFile.close()




