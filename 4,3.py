# Fungsi lambda dengan memasukan rumus konversi suhu celcius ke fahrenheit
celcius_fahrenheit = lambda c: (9/5) * c + 32
# Fungsi lambda dengan memasukan rumus konversi suhu celcius ke Reamur
celcius_reamur = lambda c: 0.8 * c

# Memanggil fungsi
print("F :", celcius_fahrenheit(100))
print("R :", celcius_reamur(80))
print("F :", celcius_fahrenheit(0))
