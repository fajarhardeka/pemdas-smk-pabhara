print("Fajar Hardeka / Guru Produktif") #DIGANTI DENGAN NAMA DAN KELAS KALIAN
print("Kalkulator sederhana mbanget\n")
print("1. Perkalian")
print("2. Pertambahan")
print("3. Pemgurangan")
print("4. modulo")
# TAMBAHKAN MINIMAL 1 OPERASI SELAIN YANG DI ATAS
pilihan = int(input("\nMasukan Pilihan Operasi : "))

a= int(input("Bilangan Pertama : "))
b= int(input("Bilangan Kedua : "))

if pilihan   == 1:
    hasilnya = a*b

elif pilihan == 2:
    hasilnya = a+b

elif pilihan == 3:
    hasilnya = a-b

elif pilihan == 4:
    hasilnya = a%b
#SESUAIKAN PERINTAH DENGAN OPERASI YANG KALIAN TAMBAHKAN JANGAN SAMPAI TERBALIK
print("\nHasil : %d" %hasilnya)     