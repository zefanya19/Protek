from datetime import *

myFile = open('data_perpus.txt', 'r')
datalist = []
data = myFile.readlines()


def diffDate(x):
    skrg = datetime.now()
    i= str(skrg.year) + '-' + str(skrg.month) + '-' + str(skrg.day)
    tgl = datetime.strptime(i, '%Y-%m-%d')
    date = datetime.strptime(x, '%Y-%m-%d')
    y = date - tgl
    return y.days


telat = diffDate('2021-12-15') * 2000
pinjam = date(2021, 12, 1)
tglmax = '2021-12-15'

for x in range(len(data)):
    pecahData = data[x].split("|")
    dataDict = {'kode member': pecahData[0], 'nama': pecahData[1], 'judul buku': pecahData[2],
                'mulai pinjam': pecahData[3], 'pengembalian': pecahData[4]}
    datalist.append(dataDict)

kunci = input('masukkan kode member yang ingin dicari :')

for i in range(len(datalist)):
    if kunci in datalist[i]['kode member']:
        print('kode                :' + str(datalist[i]['kode member']))
        print('nama                :' + str(datalist[i]['nama']))
        print('judul               :' + str(datalist[i]['judul buku']))
        print('pinjam              :', pinjam)
        print('maks pengembalian   :', tglmax)
        print('tanggal kembali     :', datetime.date(datetime.now()))
        print('terlambat           :', diffDate('2021-12-15'))
        print('denda               :', telat)

if kunci not in datalist[0]['kode member']:
    if kunci not in datalist[1]['kode member']:
        if kunci not in datalist[2]['kode member']:
            print("\"Data  tidak ditemui\"")

myFile.close()