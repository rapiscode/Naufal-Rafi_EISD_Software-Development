def caesar_decrypt(text, shift=5):
    hasil = ""
    for char in text:
        if char.isalpha():
            huruf_baru = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            hasil += huruf_baru
        else:
            hasil += char  
    return hasil

chat = [
    "xfqfr bfmdz",
    "gjxtp lzj rfz ifkyfw jxi snm",
    "gwt, gjxtp qz rfz rfpfs in bfwlty lfp?",
    "fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz",
    "dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"
]

for i, line in enumerate(chat, 1):
    print(f"{i}. {caesar_decrypt(line)}")