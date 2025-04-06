def cari_anak_nakal(data):
    hitung = {}
    for nama in data:
        if nama in hitung:
            hitung[nama] += 1
        else:
            hitung[nama] = 1

    maks = max(hitung.values())

    nakal = []
    for nama in hitung:
        if hitung[nama] == maks:
            nakal.append(nama)

    if maks == 1:
        return "Semuanya anak baik"
    elif len(nakal) == 1:
        return f"{nakal[0]} Nackal"
    else:
        return " dan ".join(nakal) + " Nackal"

input1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
input2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
input3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]

print(cari_anak_nakal(input1))  
print(cari_anak_nakal(input2))  
print(cari_anak_nakal(input3))  