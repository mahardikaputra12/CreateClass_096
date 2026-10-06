class PersegiPanjang:
    def __init__(self, panjang, lebar):
            self.panjang = panjang
            self.lebar = lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
            return self.panjang * self.lebar
    
    def __str__(self):
            return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

input_panjang = int(input("Masukan panjang (cm): "))
input_lebar = int(input("Masukan lebar (cm): "))
        
pp = PersegiPanjang(input_panjang, input_lebar)

print(pp)
print("Keliling:", pp.keliling(), "cm")
print("Luas:", pp.luas(), "cm²")