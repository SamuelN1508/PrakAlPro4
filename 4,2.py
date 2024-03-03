# Fungsi
def cek_digit_belakang(a, b, c):
    # Digunakan operator % untuk mencari digit paling kanan
    # Operator % untuk mencari sisa pembagian 10
    a = a % 10
    b = b % 10
    c = c % 10
    # Mencari apakah ada yang sama
    if a == b or a == c or b == c:
        # Jika kondisi diatas terpenuhi maka akan return True
        return True
    else:
        # Jika kondisi diatas tidak terpenuhi maka akan return False
        return False

# Memanggil fungsi
print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))

