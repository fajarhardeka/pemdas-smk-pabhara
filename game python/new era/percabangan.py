# implementasi percabangan pada python
# NAMA = ???
# KELAS = ???
# penghitungan sederhana berupa kalkulator
print(15*"-")
print("PENGHITUNGAN SEDERHANA MBANGET")
print(15*"-")

angka1 = float(input("Masukan angka pertama = "))
operasi = input("pilih operasinya +, -, x, / = ")
angka2 = float(input("Masukan angka kedua = "))

# membuat percabangan untuk logika kalkulator

if operasi == "+":
	hasil = angka1 + angka2
	print(f"hasilnya adalah = {hasil}") 
elif operasi == "-":
	hasil = angka1 - angka2
	print(f"hasilnya adalah = {hasil}")
elif operasi == "x" or operasi == "*":
	hasil = angka1 * angka2
	print(f"hasilnya adalah = {hasil}")
elif operasi == "/":
	hasil = angka1 / angka2
	print(f"hasilnya adalah = {hasil}")

else:
	print("Sing mandan memper mbokan!!!")

print("Akhir dari program sederhana, terimakasih")
