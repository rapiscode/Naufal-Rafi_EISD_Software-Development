kalimat_list = [
    "Angsa",
    "KataK",
    "kasur empuk",
    "Aku Suka Kamu",
    "Ibu Ratna antar ubi."
]

for kalimat in kalimat_list:
    kalimat_bersih = kalimat.lower().replace(".","")
    
    if kalimat_bersih == kalimat_bersih[::-1]:  
        print("eureeka!")
    else:
        print("suka blyat")