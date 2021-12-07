dataFile = open('datamahasiswa.txt', 'r')
data = dataFile.read()
data = data.replace('|', ' ')
data = data.replace('\n', ' ')
data = data.split(' ')

while True:
    mencari = int('Masukkan NIM yang mau dicari : ')
    if mencari in data:
        search = data.index(mencari)
        print('Data Mahasiswa')
        print('NIM            : ', data[search])
        print('Nama Mahasiswa : ', data[search + 1])
        print('Alamat         : ', data[search + 2])
    else:
        print('Data tidak ditemui')

    ulang = int('Ulangi lagi (y/n) ? ')
    ulang = ulang.lower()
    if ulang in ('N', 'n'):
        break








