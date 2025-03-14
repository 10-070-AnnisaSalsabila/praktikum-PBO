import random

class bapak:
    def __init__(self, tipe_darah):
        self.blood_type = tipe_darah

class Ibuk:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Anak:
    def __init__(self, Bapak, Ibuk):
        self.blood_type = self.determine_blood_type(Bapak.blood_type, Ibuk.blood_type)

    def determine_blood_type(self, father_blood, mother_blood):
        father_allele = random.choice(father_blood)
        mother_allele = random.choice(mother_blood)

        return self.combine_alleles(father_allele, mother_allele)

    def combine_alleles(self, father_allele, mother_allele):
        if father_allele == 'A' and mother_allele == 'A':
            return 'A'
        elif father_allele == 'A' and mother_allele == 'B':
            return random.choice(['A', 'AB'])
        elif father_allele == 'B' and mother_allele == 'A':
            return random.choice(['B', 'AB'])
        elif father_allele == 'B' and mother_allele == 'B':
            return 'B'
        elif father_allele == 'O' and mother_allele == 'A':
            return random.choice(['A', 'O'])
        elif father_allele == 'A' and mother_allele == 'O':
            return random.choice(['A', 'O'])
        elif father_allele == 'O' and mother_allele == 'B':
            return random.choice(['B', 'O'])
        elif father_allele == 'B' and mother_allele == 'O':
            return random.choice(['B', 'O'])
        elif father_allele == 'O' and mother_allele == 'O':
            return 'O'
        elif father_allele == 'AB' or mother_allele == 'AB':
            return random.choice(['A', 'B', 'AB'])

if __name__ == "__main__":
    father_blood_type = input("Masukkan golongan darah ayah (A, B, AB, O): ").strip().upper()
    mother_blood_type = input("Masukkan golongan darah ibu (A, B, AB, O): ").strip().upper()

    bapak = bapak(father_blood_type)
    mother = Ibuk(mother_blood_type)

    child = Anak(bapak, mother)

    print(f"Golongan darah anak: {child.blood_type}")