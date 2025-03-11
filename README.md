import random
import time    

class Robot:
    def __init__(self, nama, hp, serangan, pertahanan, akurasi):
        self.nama = nama
        self.max_hp = hp  
        self.hp = hp
        self.serangan = serangan
        self.pertahanan = pertahanan
        self.akurasi = akurasi
        self.stunned = False  
        self.silenced = False  
        self.pertahanan_boost = 0  

    def serang_lawan(self, lawan):
        if self.stunned:  
            print(f"{self.nama} terkena stun dan tidak bisa menyerang!")
            self.stunned = False  
            return False
        
        if random.random() <= self.akurasi:  
            damage = max(0, self.serangan - lawan.pertahanan)  
            lawan.hp = max(0, lawan.hp - damage)  
            print(f"{self.nama} menyerang {lawan.nama}!")
            print(f"⚔️ {self.nama} [Serangan: {self.serangan}] - {lawan.nama} [Pertahanan: {lawan.pertahanan}] ➝ Damage: {damage}")
            return True
        else:
            print(f"{self.nama} gagal menyerang.")
            return False

    def bertahan(self):
        self.pertahanan_boost = 5  
        self.pertahanan += self.pertahanan_boost  
        print(f"{self.nama} meningkatkan pertahanan sebesar {self.pertahanan_boost}!")
        print(f" Pertahanan sekarang: {self.pertahanan}")

    def gunakan_stun(self, lawan):
        if self.silenced:
            print(f"{self.nama} terkena Silence dan tidak bisa menggunakan skill!")
        else:
            print(f" {self.nama} menggunakan Stun pada {lawan.nama}!")
            lawan.stunned = True  

    def gunakan_silence(self, lawan):
        if self.silenced:
            print(f"{self.nama} terkena Silence dan tidak bisa menggunakan skill!")
        else:
            print(f" {self.nama} menggunakan Silence pada {lawan.nama}!")
            lawan.silenced = True  

    def regen_hp(self):
        if self.hp < self.max_hp:  
            regen_amount = min(20, self.max_hp - self.hp)  
            self.hp += regen_amount
            print(f" {self.nama} memulihkan {regen_amount} HP!")
        else:
            print(f"{self.nama} sudah memiliki HP penuh!")

    def reset_pertahanan(self):
        if self.pertahanan_boost > 0:
            self.pertahanan -= self.pertahanan_boost
            self.pertahanan_boost = 0

    def upgrade_serangan(self, ronde_ke):
        if ronde_ke % 3 == 0:  
            self.serangan += 5
            print(f" {self.nama} mendapatkan peningkatan serangan sebesar 5!")

    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1  

    def mulai(self):
        while self.robot1.is_alive() and self.robot2.is_alive():  
            print(f"\n============================= Ronde-{self.round} ============================================")
            print(f"{self.robot1.nama} [{self.robot1.hp} HP | Serangan: {self.robot1.serangan} | Pertahanan: {self.robot1.pertahanan}]")
            print(f"{self.robot2.nama} [{self.robot2.hp} HP | Serangan: {self.robot2.serangan} | Pertahanan: {self.robot2.pertahanan}]")
            
            for robot, lawan in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:  
                if not robot.is_alive() or not lawan.is_alive():  
                    break
                
                print("\n1. Serang  2. Bertahan  3. Stun  4. Silence  5. Menyerah  6. Regen HP")

                try:
                    pilihan = int(input(f"{robot.nama}, pilih aksi: "))  
                except ValueError:
                    print("Input tidak valid!")
                    continue
                if pilihan == 1:
                    robot.serang_lawan(lawan)
                elif pilihan == 2:
                    robot.bertahan()
                elif pilihan == 3:
                    robot.gunakan_stun(lawan)
                elif pilihan == 4:
                    robot.gunakan_silence(lawan)
                elif pilihan == 5:
                    print(f"{robot.nama} menyerah! {lawan.nama} menang!")
                    self.tampilkan_hasil(lawan)
                    return
                elif pilihan == 6:
                    robot.regen_hp()
                else:
                    print("Pilihan tidak valid!")
                    continue  

                if not lawan.is_alive():  
                    print(f"{lawan.nama} kalah! {robot.nama} menang!")
                    self.tampilkan_hasil(robot)
                    return
                
                time.sleep(1) 

            self.robot1.reset_pertahanan()
            self.robot2.reset_pertahanan()
            self.robot1.upgrade_serangan(self.round)
            self.robot2.upgrade_serangan(self.round)
            self.robot1.silenced = False  
            self.robot2.silenced = False  

            print(f"\n------------ Akhir Ronde-{self.round} ----------------")
            self.round += 1  

    def tampilkan_hasil(self, pemenang):
        pecundang = self.robot1 if pemenang == self.robot2 else self.robot2
        print("\n============================= Hasil Akhir ===========================================")
        print(f" Pemenang: {pemenang.nama} dengan {pemenang.hp} HP!")
        print(f" {pecundang.nama} kalah!")
        print(" Pertarungan selesai! 🎉\n")
robot1 = Robot("Tiger", 150, 60, 5, 0.75)
robot2 = Robot("Piko", 150, 50, 8, 0.75)

game = Game(robot1, robot2)
game.mulai()
