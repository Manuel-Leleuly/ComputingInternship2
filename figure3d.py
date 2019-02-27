class kubus:
    jumlah_sisi = 6
    def __init__(self,sisi):
        self.sisi = sisi
    def hitung_luaskubus(self):
        hasil = 6*self.sisi*self.sisi
        return hasil
    def hitung_volumekubus(self):
        hasil =  self.sisi*self.sisi*self.sisi
        return hasil

class balok:
    jumlah_sisi = 6
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    def hitung_luasbalok(self):
        hasil = (2*self.panjang*self.lebar) +(2*self.tinggi*self.panjang ) + (2*self.lebar*self.tinggi )
        return hasil
    def hitung_volumebalok(self):
        hasil =  self.panjang*self.lebar*self.tinggi
        return hasil

class tabung:
    jumlah_sisi = 3
    def __init__(self,jari,tinggi):
        self.jari = jari
        self.tinggi = tinggi
    def hitung_luastabung(self):
        hasil = 2 * 3.14 * self.jari * (self.jari + self.tinggi)
        return hasil
    def hitung_volumetabung(self):
        hasil =  3.14*self.jari*self.jari*self.tinggi
        return hasil

class kerucut:
    jumlah_sisi = 2
    def __init__(self,jari,tinggi):
        self.jari = jari
        self.tinggi = tinggi
    def hitung_luaskerucut(self):
        hasil = 3.14 * self.jari * (self.jari + self.tinggi)
        return hasil
    def hitung_volumekerucut(self):
        hasil =  1/3 * 3.14*self.jari*self.jari*self.tinggi
        return hasil