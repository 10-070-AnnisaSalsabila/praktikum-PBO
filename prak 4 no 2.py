class TugasError(Exception):
    """Kelas exception khusus untuk kesalahan tugas."""
    pass

class DaftarTugas:
    def _init_(self):
        self.tugas = []

    def tambah_tugas(self, tugas):
        if not tugas:
            raise TugasError("Tugas tidak boleh kosong.")
        self.tugas.append(tugas)
        print(f"Tugas '{tugas}' berhasil ditambahkan.")

    def hapus_tugas(self, tugas):
        if tugas not in self.tugas:
            raise TugasError(f"Tugas '{tugas}' tidak ditemukan dalam daftar.")
        self.tugas.remove(tugas)
        print(f"Tugas '{tugas}' berhasil dihapus.")

    def tampilkan_tugas(self):
        if not self.tugas:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.tugas, start=1):
                print(f"{i}. {tugas}")

def main():
    daftar_tugas = DaftarTugas()

    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tampilkan Tugas")
        print("4. Keluar")

        try:
            pilihan = int(input("Pilih menu (1-4): "))
            if pilihan == 1:
                tugas = input("Masukkan tugas yang ingin ditambahkan: ")
                daftar_tugas.tambah_tugas(tugas)
            elif pilihan == 2:
                tugas = input("Masukkan tugas yang ingin dihapus: ")
                daftar_tugas.hapus_tugas(tugas)
            elif pilihan == 3:
                daftar_tugas.tampilkan_tugas()
            elif pilihan == 4:
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1-4.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
        except TugasError as e:
            print(e)

if __name__ == "_main_":
    main()