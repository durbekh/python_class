# # 1
# class Transport:
#     def __init__(self, model: str, yil: int) -> None:
#         self.model = model
#         self.yil = yil
#
#     def malumot(self) -> str:
#         return f"Model: {self.model}, Yil: {self.yil}"
#
#
# class Avtomobil(Transport):
#     def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, Yonilg'i: {self.yonilgi_turi}"
#
#
# class Avtobus(Transport):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"
#
#
# a = Avtomobil("Cobalt", 2022, "benzin")
# print(a.malumot())
#
# b = Avtobus("Isuzu", 2018, 40)
# print(b.malumot())

# # 2
# class Kitob:
#     def __init__(self, nom, muallif, yil):
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = yil
#
#     def taqdimot(self):
#         return f'"{self.nom}" - {self.muallif} ({self.yil})'
#
#
# class ElektronKitob(Kitob):
#     def __init__(self, nom, muallif, yil, fayl_hajmi_mb):
#         super().__init__(nom, muallif, yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def taqdimot(self):
#         return super().taqdimot() + f" [Elektron, {self.fayl_hajmi_mb}MB]"
#
#
# class AudioKitob(Kitob):
#     def __init__(self, nom, muallif, yil, davomiylik_soat):
#         super().__init__(nom, muallif, yil)
#         self.davomiylik_soat = davomiylik_soat
#
#     def taqdimot(self):
#         return super().taqdimot() + f" [Audio, {self.davomiylik_soat} soat]"
#
#
#
# e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
# a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
#
# print(e.taqdimot())
# print(a.taqdimot())
# # 3
# class Xodim:
#     def __init__(self, ism, asosiy_maosh):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
#
#     def oylik(self):
#         return self.asosiy_maosh
#
#     def malumot(self):
#         return f"Ism: {self.ism}, Oylik: {self.oylik()}"
#
#
# class Oqsoch(Xodim):
#     def __init__(self, ism, asosiy_maosh, bonus_foiz):
#         super().__init__(ism, asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
#
#     def oylik(self):
#         bonus = self.asosiy_maosh * self.bonus_foiz / 100
#         return self.asosiy_maosh + bonus
#
#
# class SoatbayXodim(Xodim):
#     def __init__(self, ism, soat, soatlik_stavka):
#         asosiy_maosh = soat * soatlik_stavka
#         super().__init__(ism, asosiy_maosh)
#         self.soat = soat
#         self.soatlik_stavka = soatlik_stavka
#
#
#
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)
#
# print(o.malumot())
# print(s.malumot())
# # 4
# class Mahsulot:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def chegirmali_narx(self, foiz):
#         chegirma = self.narx * foiz / 100
#         return self.narx - chegirma
#
#
# class Elektronika(Mahsulot):
#     def __init__(self, nom, narx, kafolat_oy):
#         super().__init__(nom, narx)
#         self.kafolat_oy = kafolat_oy
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Kafolat: {self.kafolat_oy} oy"
#
#
# class OziqOvqat(Mahsulot):
#     def __init__(self, nom, narx, yaroqlilik_kuni):
#         super().__init__(nom, narx)
#         self.yaroqlilik_kuni = yaroqlilik_kuni
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Yaroqlilik: {self.yaroqlilik_kuni}"
#
#
# telefon = Elektronika("iPhone 15", 12_000_000, 12)
# sut = OziqOvqat("Sut", 15_000, "2026-12-31")

# print(telefon.malumot())
# print(f"Chegirmali narx (10%): {telefon.chegirmali_narx(10)}")
# print()
# print(sut.malumot())
# print(f"Chegirmali narx (5%): {sut.chegirmali_narx(5)}")
# # 5
# class Shaxs:
#     def __init__(self, ism):
#         self.ism = ism
#
#
# class Talaba(Shaxs):
#     def __init__(self, ism, id_raqam):
#         super().__init__(ism)
#         self.id_raqam = id_raqam
#
#
# class ImtihonNatijasi(Talaba):
#     def __init__(self, ism, id_raqam, baholar):
#         super().__init__(ism, id_raqam)
#         self.baholar = baholar
#
#     def ortalama(self):
#         return sum(self.baholar) / len(self.baholar)
#
#     def status(self):
#         o = self.ortalama()
#         if o >= 86:
#             return "A'lo"
#         elif o >= 71:
#             return "Yaxshi"
#         elif o >= 56:
#             return "Qoniqarli"
#         else:
#             return "Qoniqarsiz"
#
#
# natija = ImtihonNatijasi("Ali", "T001", [90, 80, 100])
# print(natija.ism)
# print(natija.id_raqam)
# print(natija.ortalama())
# print(natija.status())
# # 6
# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.egasi = egasi
#         self.balans = balans
#
#     def kirim(self, summa):
#         if summa < 0:
#             raise ValueError("Qiymatda xatolik!")
#         self.balans += summa
#
#     def chiqim(self, summa):
#         if summa < 0:
#             return "Manfiy summa chiqarib bo'lmaydi"
#         if self.balans < summa:
#             return "Balans yetarli emas"
#         self.balans -= summa
#         return "Muvaffaqiyatli!"
#
#
# class JamgArmaMixin:
#     def __init__(self, foiz_stavkasi, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.foiz_stavkasi = foiz_stavkasi
#
#     def foiz_qosh(self):
#         qoshimcha = self.balans * self.foiz_stavkasi / 100
#         self.balans += qoshimcha
#
#
# class KreditMixin:
#     def __init__(self, limit, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.limit = limit
#
#     def chiqim(self, summa):
#         if summa < 0:
#             return "Manfiy summa chiqarib bo'lmaydi"
#         if self.balans + self.limit < summa:
#             return "Limit yetarli emas"
#         self.balans -= summa
#         return "Muvaffaqiyatli!"
#
#
# class VIPHisob(JamgArmaMixin, KreditMixin, Hisob):
#     def __init__(self, raqam, egasi, balans, foiz_stavkasi, limit):
#         super().__init__(foiz_stavkasi=foiz_stavkasi, limit=limit,
#                          raqam=raqam, egasi=egasi, balans=balans)
#
#
# vip = VIPHisob("001", "Karim", 2_000_000, 12, 500_000)
#
# vip.foiz_qosh()
# print(vip.balans)
# vip.chiqim(2_400_000)
# print(vip.balans)

# # 7
# class Kurs:
#     def __init__(self, nom, davomiylik_hafta, narx):
#         self.nom = nom
#         self.davomiylik_hafta = davomiylik_hafta
#         self.narx = narx
#
#     def malumot(self):
#         return f"Kurs: {self.nom}, Davomiylik: {self.davomiylik_hafta} hafta, Narx: {self.narx}"
#
#
# class OnlaynKurs(Kurs):
#     def __init__(self, nom, davomiylik_hafta, narx, platforma):
#         super().__init__(nom, davomiylik_hafta, narx)
#         self.platforma = platforma
#
#     def malumot(self):
#         m = super().malumot()
#         return f"{m}, Platforma: {self.platforma}"
#
#
# class OfflineKurs(Kurs):
#     def __init__(self, nom, davomiylik_hafta, narx, manzil):
#         super().__init__(nom, davomiylik_hafta, narx)
#         self.manzil = manzil
#
#     def malumot(self):
#         x = super().malumot()
#         return f"{x}, Manzil: {self.manzil}"
#
#
# kurslar = [
#     OnlaynKurs("Python", 12, 1_800_000, "Coursera"),
#     OfflineKurs("Kiberxavfsizlik", 40, 25_000_000, "Toshkent")
# ]
#
# for kurs in kurslar:
#     print(kurs.malumot())

# # 8

# class Taom:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def tavsif(self):
#         return f"Taom: {self.nom}, Narx: {self.narx}"
#
#
# class IssiqTaom(Taom):
#     def __init__(self, nom, narx, kaloriya):
#         super().__init__(nom, narx)
#         self.kaloriya = kaloriya
#
#     def tavsif(self):
#         return super().tavsif() + f", Kaloriya: {self.kaloriya} kkal"
#
#
# class Ichimlik(Taom):
#     def __init__(self, nom, narx, hajm_ml):
#         super().__init__(nom, narx)
#         self.hajm_ml = hajm_ml
#
#     def tavsif(self):
#         return super().tavsif() + f", Hajm: {self.hajm_ml} ml"
#
#
# def chegirma_qollash(taomlar, foiz):
#     for taom in taomlar:
#         taom.narx *= (1 - foiz / 100)
#
# taomlar = [
#     IssiqTaom("Lagman", 30000, 450),
#     Ichimlik("Coca-Cola", 10000, 500),
#     IssiqTaom("Shashlik", 40000, 550)
# ]
#
# for taom in taomlar:
#     print(taom.tavsif())
#
# chegirma_qollash(taomlar, 10)
#
# print("\nChegirma qollashdan keyin:")
# for taom in taomlar:
#     print(taom.tavsif())

# # 9












































