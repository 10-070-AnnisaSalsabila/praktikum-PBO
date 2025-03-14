import math

class Kalkulator:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)

    def __sub__(self, other):
        return Kalkulator(self.nilai - other.nilai)

    def __mul__(self, other):
        return Kalkulator(self.nilai * other.nilai)

    def __truediv__(self, other):
        if other.nilai == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        return Kalkulator(self.nilai / other.nilai)

    def __pow__(self, exponent):
        return Kalkulator(self.nilai ** exponent.nilai)

    def log(self):
        if self.nilai <= 0:
            raise ValueError("Logaritma tidak terdefinisi untuk nilai <= 0")
        return math.log(self.nilai)

    def __repr__(self):
        return f"Kalkulator({self.nilai})"

if __name__ == "__main__":
    a = Kalkulator(10)
    b = Kalkulator(5)

    print("Penjumlahan:", (a + b))  # 10 + 5
    print("Pengurangan:", (a - b))  # 10 - 5
    print("Perkalian:", (a * b))    # 10 * 5
    print("Pembagian:", (a / b))    # 10 / 5
    print("Eksponen:", (a ** b))     # 10 ^ 5
    print("Logaritma dari a:", a.log())  # log(10)