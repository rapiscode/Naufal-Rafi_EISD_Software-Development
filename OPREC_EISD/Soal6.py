menu = {
    "Ayam Goreng Krispi": ["makanan", 15000],
    "Ayam Puk Puk": ["makanan", 13000],
    "Ayam Bakar": ["makanan", 20000],
    "Es Teh": ["minuman", 5000],
    "Es Jeruk": ["minuman", 7000],
}

pajak_makanan = 0.05   
pajak_minuman = 0.03   
pajak_transaksi = 0.15 

def hitung_harga_item(nama_item, jumlah):
    tipe, harga = menu[nama_item]
    
    total = harga * jumlah
    
    if tipe == "makanan":
        total += total * pajak_makanan
    elif tipe == "minuman":
        total += total * pajak_minuman
    
    return total

pesanan = {
    "Rehan": [("Ayam Bakar", 2), ("Es Teh", 1)],
    "Amba": [("Ayam Puk Puk", 1), ("Es Teh", 3)],
    "Faiz": [("Ayam Goreng Krispi", 1), ("Ayam Puk Puk", 1), ("Ayam Bakar", 1), ("Es Teh", 1), ("Es Jeruk", 1)],
}

for nama, daftar_pesanan in pesanan.items():
    subtotal = 0
    
    for item, jumlah in daftar_pesanan:
        subtotal += hitung_harga_item(item, jumlah)
    
    total_bayar = subtotal + (subtotal * pajak_transaksi)
    
    print(f"{nama} harus membayar: Rp{round(total_bayar)}")