from itertools import permutations

nama = "naiplovyu"  
panjang_maks = 6
kombinasi = set()  

for i in range(1, panjang_maks + 1):
    for p in permutations(nama, i):
        kombinasi.add("".join(p))  

print(len(kombinasi))  