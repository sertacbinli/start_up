import random
import time

print("""
*****************************************
Sayı Tahmin Oyununa Hoş Geldiniz.
Toplam 7 tahminde 1 ile 50 arasında
tuttuğum sayıyı tahmin edin.
*****************************************
""")

random_number = random.randint(1,50)
forecast_number = 7

while True:
    forecast = input("0 ile 51 arasında bir sayı girin: ")

    if forecast == "q":
        print("Oyun sonlandırılıyor.")
        time.sleep(2)
        break
    else:
        forecast = int(forecast)

    if forecast > 50 or forecast < 0:
        print("Lütfen 0 ile 50 arasında geçerli bir sayı girin.")

    elif forecast > random_number:
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Hatalı tahmin, daha düşük bir sayı girin.")
        forecast_number -= 1
        print("Kalan tahmin hakkı {}".format(forecast_number))

    elif forecast < random_number:
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Hatalı tahmin, daha yüksek bir sayı girin.")
        forecast_number -=1
        print("Kalan tahmin hakkı {}".format(forecast_number))

    else:
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Bravo! Sayıyı doğru bildiniz.")
        break

    if forecast_number == 0:
        print("Tahmin hakkınız kalmadı. Tuttuğum sayı: {} idi.".format(random_number))
        break