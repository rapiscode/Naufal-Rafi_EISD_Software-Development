def hitung_kembalian(total_bayar, total_belanja):
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = total_bayar - total_belanja

    for uang in pecahan:
        jumlah = kembalian // uang
        if jumlah > 0:
            print(f'"{uang}" : {jumlah}')
            kembalian -= uang * jumlah

hitung_kembalian(10000, 7500)
print("---")
hitung_kembalian(5000, 1100)
print("---")
hitung_kembalian(178000, 90500)