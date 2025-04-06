angka = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10, 12, 14, 16, 18, 20, 17, 19]

duplikat = False

for i in range(len(angka)):
    for j in range(i + 1, len(angka)):  
        if angka[i] == angka[j]:  
            duplikat = True
            break 
    if duplikat:
        break  

print(duplikat)  