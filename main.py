"""
Dil : Python
Konu: String Veri Tipi
"""

# --------------------------------------------------------------------------------------

"""
ad="Mehmet Ali"
soyad="Durusoy"
print(ad," ",soyad)

a="10"
b="20"
print(a+b)

ad=input("Adini gir : ")

if int(ad):
 print("Ad Sayi Olamaz")
else:
 soyad=input("Soyadini gir : ")
 print(ad," ",soyad)


--- 
 Hesapla
---

# Ogrenci 1
ad=input("Adini gir : ")
soyad=input("Soyadini gir : ")
not1=float(input("1.Notu gir : "))
not2=float(input("2.Notu gir : "))
sozlu=float(input("Sozluyu gir : "))
hesapla=(not1+not2+sozlu)/3
if hesapla<50:
  durum="Kaldi"
else:
  durum="Gecti"

print("------------")

# Ogrenci 2
og2_ad=input("Adini gir : ")
og2_soyad=input("Soyadini gir : ")
og2_not1=float(input("1.Notu gir : "))
og2_not2=float(input("2.Notu gir : "))
og2_sozlu=float(input("Sozluyu gir : "))
og2_hesapla=(og2_not1+og2_not2+og2_sozlu)/3
if og2_hesapla<50:
  og2_durum="Kaldi"
else:
  og2_durum="Gecti"
print("Ogrenci 1 ",ad,soyad,"\nOrtalamasi : ",hesapla," | Durum : ",durum)
print("-----------------------------------------------------------------------------------")
print("Ogrenci 2 ",og2_ad,og2_soyad,"\nOrtalamasi : ",og2_hesapla," | Durum : ",og2_durum)
exit

"""

def ogrenci_not_hesapla(ad,soyad,not1,not2,sozlu,inci):
  print("****************")
  hesapla=(not1+not2+sozlu)/3
  if hesapla<50:
    durum="Kaldi"
  else:
    durum="Gecti" 
  print(inci,".Ogrenci  Adi ve Soyadi : ",ad,soyad,"\nOrtalamasi : ",hesapla," | Durum : ",durum
    ,"\n*********************")

"""
 ogrenci_not_hesapla(input("Adini gir : "),input("Soyadini gir : "),
    float(input("1.Notu gir : ")),float(input("2.Notu gir : ")),
    float(input("Sozlugu gir : ")))

ogrenci_not_hesapla(input("Adini gir : "),input("Soyadini gir : "),
    float(input("1.Notu gir : ")),float(input("2.Notu gir : ")),
    float(input("Sozlugu gir : ")))
"""
donguSayisi=2
for x in range(donguSayisi):
  ogrenci_not_hesapla(input("Adini gir : "),input("Soyadini gir : "),
   float(input("1.Notu gir : ")),float(input("2.Notu gir : ")),
   float(input("Sozlugu gir : ")),x)
