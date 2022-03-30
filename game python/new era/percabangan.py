# implementasi percabangan pada python
# NAMA = ???
# KELAS = ???
#penghitungan sederhana
print(20*"=")
print("penghitungan sederhana")
print(20*"=" + "\n")

angka1 = float(input("masukan angka ke 1 ="))
operasi = input("+,-,x,/ = ")
angka2 = float(input("masukan angka ke 2 ="))

#percabangannya

if operasi == "+":
	hasil = angka1 + angka2
	print(f"hasilnya adalah {hasil}")
elif operasi == "-":
	hasil = angka1 - angka2
	print(f"hasilnya adalah {hasil}")
elif operasi == "x" or operasi == "*":
	hasil = angka1 * angka2
	print(f"hasilnya adalah {hasil}")
elif operasi == "/":
	hasil = angka1 / angka2
	print(f"hasilnya adalah {hasil}")
else:
	print("masukan yang bener dong la brooo")

print("Akhir dari program, penghitunngan sederhana!")