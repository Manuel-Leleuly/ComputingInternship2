import math

class Segitiga :
    jumlah_sisi = 3

class Segiempat :
    jumlah_sisi = 4

class Samasisi(Segitiga):
    def __init__(self,sisi,tinggi):
        self.sisi=sisi
        self.tinggi=tinggi

    def hitung_luas(self):
        hasil = (0.5*self.tinggi*self.sisi)
        return hasil

    def hitung_keliling(self):
        hasil=self.sisi*3
        return hasil


class Samakaki(Segitiga):
    def __init__(self,alas,tinggi):
        self.alas=alas
        self.tinggi=tinggi

    def hitung_luas(self):
        hasil=0.5*self.alas*self.tinggi
        return hasil

    def hitung_keliling(self):
        sisi_miring=pow((self.tinggi*self.tinggi+(self.alas*self.alas)/4),0.5)
        hasil=sisi_miring*2+self.alas
        return hasil

class Persegi(Segiempat):
    def __init__(self,panjang,lebar):
        self.panjang=panjang
        self.lebar=lebar
    
    def hitung_luas(self):
        hasil=self.panjang*self.lebar
        return hasil
    
    def hitung_keliling(self):
        hasil=2*(self.panjang+self.lebar)
        return hasil
    
class Trapesium(Segiempat):
    def __init__(self,alas,tutup,tinggi):
        self.alas=alas
        self.tutup=tutup
        self.tinggi=tinggi
    
    def hitung_luas(self):
        hasil=(self.alas+self.tutup)*self.tinggi/2
        return hasil
    
    def hitung_keliling(self):
        tmp=(self.alas-self.tutup)/2
        sisi_miring=pow(tmp*tmp+self.tinggi*self.tinggi,0.5)
        return sisi_miring
    
class Jajargenjang(Segiempat):
    def __init__(self,alas,tinggi):
        self.alas=alas
        self.tinggi=tinggi
    
    def hitung_luas(self):
        hasil=self.alas*self.tinggi
        return hasil
    
    def hitung_keliling(self):
        hasil=2*(self.alas+self.tinggi)
        return hasil