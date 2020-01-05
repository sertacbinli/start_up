print ("kayıt işlemlerine hoş geldiniz!")
ad = input ("Adınız?")

if ad == "Admin":
    print ("admin girişi yetkiniz bulunmuyor")
else:
    print("Kayıt işlemine devam edebilirsiniz.")

soyad = input ("Soyadınız?")
yas = input ("Yaşınız?")

if yas >= "18":
        print ("Kayıt işlemine devam edebilirsiniz.")
elif yas < "18":
        print ("18 Yaşından küçükler üyeliğe devam edemez.")