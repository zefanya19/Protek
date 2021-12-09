try :
    from datetime import *

    def differentDate(x):
        tanggalsekarang = datetime.now()
        selisih = str(x - tanggalsekarang)
        print('Selisih jumlah hari antara tanggal ', tanggalsekarang, ' dan ', x, ' adalah ', selisih.days, ' hari.')

    x = date(2003, 7, 23)
    differentDate(x)
except ValueError:
    print('waduh inputnya tidak valid nich')