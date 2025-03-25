from abc import ABC, abstractmethod

# Kelas Abstrak
class Animal(ABC):
    def _init_(self, nama, usia):
        self.__nama = nama
        self.__usia = usia

    @abstractmethod
    def make_sound(self):
        pass

    def get_nama(self):
        return self.__nama

    def get_usia(self):
        return self.__usia

    def set_nama(self, nama):
        self.__nama = nama

    def set_usia(self, usia):
        if usia < 0:
            raise ValueError("Usia tidak boleh negatif.")
        self.__usia = usia

# Kelas Turunan
class Anjing(Animal):
    def make_sound(self):
        return "Guk! Guk!"

class Kucing(Animal):
    def make_sound(self):
        return "Meow!"

class Burung(Animal):
    def make_sound(self):
        return "Cuit! Cuit!"

# Sistem Manajemen Hewan
class ZooManagementSystem:
    def _init_(self):
        self.__hewan_list = []

    def tambah_hewan(self, hewan):
        if not isinstance(hewan, Animal):
            raise TypeError("Objek yang ditambahkan harus merupakan instansi dari kelas Animal.")
        self.__hewan_list.append(hewan)

    def tampilkan_hewan(self):
        for hewan in self.__hewan_list:
            print(f"Nama: {hewan.get_nama()}, Usia: {hewan.get_usia()}, Suara: {hewan.make_sound()}")

# Fungsi utama
def main():
    zoo = ZooManagementSystem()

    while True:
        try:
            print("\n=== Sistem Manajemen Kebun Binatang ===")
            print("1. Tambah Hewan")
            print("2. Tampilkan Hewan")
            print("3. Keluar")
            pilihan = int(input("Pilih menu: "))

            if pilihan == 1:
                nama = input("Masukkan nama hewan: ")
                usia = int(input("Masukkan usia hewan: "))
                jenis = input("Masukkan jenis hewan (anjing/kucing/burung): ").lower()

                if jenis == "anjing":
                    hewan = Anjing(nama, usia)
                elif jenis == "kucing":
                    hewan = Kucing(nama, usia)
                elif jenis == "burung":
                    hewan = Burung(nama, usia)
                else:
                    print("Jenis hewan tidak valid.")
                    continue

                zoo.tambah_hewan(hewan)
                print(f"Hewan {nama} berhasil ditambahkan.")

            elif pilihan == 2:
                zoo.tampilkan_hewan()

            elif pilihan == 3:
                print("Keluar dari sistem.")
                break

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        except ValueError as e:
            print(f"Kesalahan: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()