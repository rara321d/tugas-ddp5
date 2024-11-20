def celcius_ke_fahrenheit(celcius):
    # Mengkonversi suhu dari Celsius ke Fahrenheit
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
# Contoh penggunaan
print(celcius_ke_fahrenheit(0)) 
print(celcius_ke_fahrenheit(100))

print('===============================================================')

def is_genap(bilangan):
    return bilangan % 2 == 0
print(is_genap(4))  
print(is_genap(7))  

print('===================================================================')

def nilai(n):
    # Mengembalikan keterangan lulus atau tidak lulus
    if n >= 80:
        return "lulus"
    else:
        return "gagal"
print(nilai(80)) 
print(nilai(60))  

print('========================================================================')

def bil_ganjil(angka):
    for i in range(1, angka, 2):
         print(i, end=" ")
#untuk memasukkan valueu        
print(bil_ganjil(20))  