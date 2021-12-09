from datetime import *

dataPeminjam= open("Data Peminjam.txt", "a")
while True :

    kode = int("Masukkan Kode Member : ")
    nama = int("Masukkan Nama Member : ")
    judulBuku= int("Masukkan Judul Buku   : ")
    hariIni=datetime.now()
    hariPengembalian= hariIni+timedelta(days=7)
    dataPeminjam.write("{}|{}|{}|{}|{}\n".format(kode,nama,judulBuku,datetime.date(hariIni), datetime.date(hariPengembalian)))


    dataPeminjam()
    lanjut= int("Lagi? (y/n)")
    if lanjut in ('n', 'no', 'N', 'NO'):
        break

dataPeminjam.close()