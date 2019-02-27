from figure3d import *


print("Program 4")
print("1. Kubus")
print("a) luas permukaan")
kubusA = kubus(int(input("Masukkan panjang sisi : ")))
print("Luas Kubus: ",kubusA.hitung_luaskubus())
print("b) volume")
print("Volume Kubus: ",kubusA.hitung_volumekubus())

print(" ")

print("2. balok")
print("a) luas permukaan")
balokA = balok(int(input("Masukkan panjang : ")),int(input("Masukkan lebar : ")),int(input("Masukkan tinggi : ")))
print("Luas Balok: ",balokA.hitung_luasbalok())
print("b) volume")
print("Volume Balok: ",balokA.hitung_volumebalok())

print(" ")

print("3. Tabung")
print("a) luas permukaan")
tabungA = tabung(int(input("Masukkan jari jari : ")),int(input("Masukkan tinggi : ")))
print("Luas Tabung: ",tabungA.hitung_luastabung())
print("b) volume")
print("Volume Tabung : ",tabungA.hitung_volumetabung())

print(" ")

print("4. Kerucut")
print("a) luas permukaan")
kerucutA = kerucut(int(input("Masukkan jari jari : ")),int(input("Masukkan tinggi : ")))
print("Luas Kerucut: ",kerucutA.hitung_luaskerucut())
print("b) volume")
print("Volume Kerucut : ",kerucutA.hitung_volumekerucut())


