print("""
**************************
Hesap Makinesi

İşlem Tipini Seçin
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
Çıkmak için 'q' ya basın.
**************************
""")

while True:
    operation_type = input("İşlem Tipi: ")

    if operation_type == "q":
        print("Program kullanıcı isteğiyle sonlandırıldı.")
        break
    elif operation_type == "1" or operation_type == "2" or operation_type == "3" or operation_type == "4":
        print("İşleme devam ediliyor.")
    else:
        print("Geçersiz işlem tipi")
        break

    first_number = int(input("Birinci Sayı: "))
    second_number = int(input("İkinci Sayı: "))

    if operation_type != "q":
        operation_type = int(operation_type)

    if operation_type == 1:
        print("İşlem Sonucu: ", first_number + second_number)
    elif operation_type == 2:
        print("İşlem Sonucu: ", first_number - second_number)
    elif operation_type == 3:
        print("İşlem Sonucu: ", first_number * second_number)
    elif operation_type == 4:
        print("İşlem Sonucu: ", first_number / second_number)

    elif operation_type > 4:
        print("Geçersiz bir işlem tipi seçtiniz.")



