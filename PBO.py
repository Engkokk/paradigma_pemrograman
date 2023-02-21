class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga1 = segitiga(5,10)
segitiga2 = segitiga(6,10)
segitiga3 = segitiga(7,10)
print('luas segitiga', segitiga1.get_luas())
print('luas segitiga', segitiga2.get_luas())
print('luas segitiga', segitiga3.get_luas())
