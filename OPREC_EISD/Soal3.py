tamu = ["Ningguang", "Hutao", "Xiao", "Childe"]

bukti_foto = "kue masih ada"

for i in range(len(tamu)):
    if tamu[i] == "Xiao":  
        tersangka = tamu[i + 1]  

print(f"Orang yang paling mungkin mengambil kue adalah: {tersangka}")