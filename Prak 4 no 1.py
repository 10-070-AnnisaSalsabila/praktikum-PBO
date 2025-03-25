import math

def hitung_akar_kuadrat():
    while True:
        try:
            
            angka_input = input("Masukkan angka: ")

            
            angka = float(angka_input)

            if angka < 0:
                print("Input tidak valid. Harap masukkan angka yang valid.")
                print("Error: Akar kuadrat dari angka negatif tidak diperbolehkan.")
            elif angka == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                akar = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {akar:.2f}")
                break  
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")
hitung_akar_kuadrat()