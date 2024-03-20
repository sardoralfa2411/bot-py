class TurizmAylanma:
    def __init__(self, joy, tavsif):
        self.joy = joy
        self.tavsif = tavsif


class QashqadaryoTurizmDasturi:
    def __init__(self):
        self.aylanmalar = []

    def aylanma_qo'shish(self, joy, tavsif):

    self.aylanmalar.append(TurizmAylanma(joy, tavsif))


def joylarni_ko'rsatish(self):


for index, aylanma in enumerate(self.aylanmalar):
    print(f"{index + 1}. {aylanma.joy}")


def joy_tafsiloti(self, indeks):
    aylanma = self.aylanmalar[indeks]
    print(f"{aylanma.joy}: {aylanma.tavsif}")


def main():
    dastur = QashqadaryoTurizmDasturi()
    dastur.aylanma_qo
    'shish("Obi Hayvonot bog'
    i
    ", "
    Shoh
    ko
    'z soch o'
    sishi
    ")
    dastur.aylanma_qo
    'shish("G'
    allaorol
    ", "
    Tabiiy
    qoral
    quti
    ")
    dastur.aylanma_qo
    'shish("Nurata ta'
    mi
    ", "
    Uchuvchi
    ta
    'm osh")

    print("Turizm joylari:")
    dastur.joylarni_ko
    'rsatish()

    indeks = int(input("Batafsil ma'lumotlarni ko'rish uchun raqam kiriting: "))
    dastur.joy_tafsiloti(indeks - 1)


if __name__ == "__main__":
    main()
