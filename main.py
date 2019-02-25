from vehicle import *

print("ini program vehicle")
a = Bicycle(int(input("input hour: ")), int(input("input year: ")), int(input("input price: ")))
print('pajak = ',a.pay_tax())
print('harga tiket = ',a.park())
#motorbikeA = Motorbike (int(input("input: tax")), int(input("input: wheel")), int(input("input: hour")))
