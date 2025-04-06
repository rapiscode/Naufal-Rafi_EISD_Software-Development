produk = {
    "TV": "elektronik",
    "headphone": "elektronik",
    "baju": "fashion",
    "gitar": "musik",
    "sepatu": "olahraga",
    "kamera": "elektronik"
}

pelanggan = {
    "Rina": ["elektronik", "musik"],
    "Budi": ["fashion", "musik"],
    "Hartono": ["olahraga", "elektronik"]
}

def rekomendasi(nama):
    minat = pelanggan[nama]
    hasil = []

    for nama_produk, kategori in produk.items():
        if kategori in minat:
            hasil.append(nama_produk)

    return hasil


print("Rekomendasi untuk Rina:", rekomendasi("Rina"))
print("Rekomendasi untuk Budi:", rekomendasi("Budi"))
print("Rekomendasi untuk Hartono:", rekomendasi("Hartono"))