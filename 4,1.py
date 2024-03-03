# Fungsi
def cek_angka(a, b ,c):
    # Kondisi dalam "if" menentukan apakah ketiga argumen ada yang sama atau tidak
    # Jika berbeda semua, maka code dibawahnya akan berjalan
    if a != b and b != c and a != c:
        # Jika diambil dua parameter dan dijumlahkan hasilnya sama dengan parameter lainnya
        if a + b == c or a + c == b or b + c == a:
            # Jika kondisi tidak terpenuhi maka akan return False
            return True
        else:
            # Jika kondisi tidak terpenuhi maka akan return False
            return False
    else:
        return False
        
# Memanggil fungsi
print(cek_angka(1, 2, 3))
print(cek_angka(2, 2, 3))
print(cek_angka(3, 4, 9))
