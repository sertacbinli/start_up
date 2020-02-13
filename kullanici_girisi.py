print("""
**************************
Kullanıcı Giriş Ekranı
**************************
""")

admin_user = "Admin"
admin_password = "admin"
user = "SertaGE"
password = "Sertage.23"
login_count = 2

while True:
    login_user = input("Kullanıcı Adı: ")
    login_password = input("Parola: ")

    if login_user == "Admin" and login_password == "admin":
        print("Admin Girişi Başarılı")
        break

    if login_count == 0:
        print("Çok sayıda hatalı giriş nedeniyle hesap bloke edildi.")
        break

    if login_user == user and login_password == password:
        print("Kullanıcı Girişi Başarılı")
        break
    elif login_user != user and login_password == password:
        print("Kullanıcı Adı Hatalı")
        print("Kalan Hak: ", login_count)
        login_count -= 1
    elif login_user == user and login_password != password:
        print("Parola Hatalı")
        print("Kalan Hak: ", login_count)
        login_count -= 1
    elif login_user != user and login_password != password:
        print("Kullanıcı Adı ve Parola Hatalı")
        print("Kalan Hak: ", login_count)
        login_count -= 1
