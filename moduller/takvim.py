import calendar
import datetime

def takvim_menu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║      TAKVİM VE YAŞ HESAPLAMA        ║")
    print("║                                     ║")
    print("║  1- Aylık Takvim Göster             ║")
    print("║  2- Yıllık Takvim Göster            ║")
    print("║  3- Yaş Hesapla                     ║")
    print("║  4- Şu Anki Tarih ve Saati Göster   ║")
    print("║  5- Ana Menüye Dön                  ║")
    print("╚═════════════════════════════════════╝")
    secim = input("Seçiminiz nedir?: ")

    if secim == "1":
        yil = int(input("Yılı giriniz: "))
        ay = int(input("Ayı giriniz: "))
        if ay >= 1 and ay <= 12:
            print("\n", calendar.month(yil, ay))
        else:
            print("[!] Hatalı Ay girişi! Ay bilgisi 1 ile 12 arasında olmalıdır!")
        takvim_menu()

    elif secim == "2":
        yil = int(input("Yılı giriniz: "))
        print("\n", calendar.calendar(yil))
        takvim_menu()

    elif secim == "3":
        bu_yil = datetime.date.today().year
        dogum_yili = int(input("Doğum yılını giriniz: "))
        if dogum_yili > bu_yil:
            print("[!] Hatalı yıl girişi! Lütfen geçerli bir yıl giriniz.")
        else:
            yas = bu_yil - dogum_yili
            print(f"{yas} yaşındasınız!")
        takvim_menu()
        
    elif secim == "4":
        simdi = datetime.datetime.now()
        print("Şu anki tarih ve saat:", simdi)
        takvim_menu()

    elif secim == "5":
        print("\n>>> Ana menüye dönülüyor...")

    else:
        print("\n[!] Hatalı seçim yaptınız! Lütfen 1-5 arasında bir seçim yapınız.")
        takvim_menu()