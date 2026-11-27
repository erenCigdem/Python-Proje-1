def hm_menu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║           HESAP MAKİNESİ            ║")
    print("║                                     ║")
    print("║  1- Toplama (+)                     ║")
    print("║  2- Çıkarma (-)                     ║")
    print("║  3- Çarpma (*)                      ║")
    print("║  4- Bölme (/)                       ║")
    print("║  5- Üs Alma (**)                    ║")
    print("║  6- Kare Alanı Hesaplama            ║")
    print("║  7- Karenin Çevresini Hesaplama     ║")
    print("║  8- Ana Menüye Dön                  ║")
    print("╚═════════════════════════════════════╝")

    secim = input("Seçiminiz nedir?: ")

    if secim == "1":
        sayi1 = float(input("1. sayıyı giriniz: "))
        sayi2 = float(input("2. sayıyı giriniz: "))
        print("Sonuç (Toplam):", sayi1 + sayi2)
        hm_menu()

    elif secim == "2":
        sayi1 = float(input("1. sayıyı giriniz: "))
        sayi2 = float(input("2. sayıyı giriniz: "))
        print("Sonuç (Fark):", sayi1 - sayi2)
        hm_menu()

    elif secim == "3":
        sayi1 = float(input("1. sayıyı giriniz: "))
        sayi2 = float(input("2. sayıyı giriniz: "))
        print("Sonuç (Çarpım):", sayi1 * sayi2)
        hm_menu()

    elif secim == "4":
        sayi1 = float(input("1. sayıyı giriniz: "))
        sayi2 = float(input("2. sayıyı giriniz: "))
        if sayi2 == 0:
            print("[!] Hata: Bir sayı 0'a bölünemez!")
        else:
            print("Sonuç (Bölüm):", sayi1 / sayi2)
        hm_menu()

    elif secim == "5":
        taban = float(input("Taban sayıyı giriniz: "))
        us = float(input("Üs (kuvvet) sayısını giriniz: "))
        print("Sonuç:", taban ** us)
        hm_menu()

    elif secim == "6":
        kenar = float(input("Karenin bir kenar uzunluğunu giriniz: "))
        print("Karenin Alanı:", kenar * kenar)
        hm_menu()

    elif secim == "7":
        kenar = float(input("Karenin bir kenar uzunluğunu giriniz: "))
        print("Karenin Çevresi:", kenar * 4)
        hm_menu()

    elif secim == "8":
        print("\n>>> Ana menüye dönülüyor...")

    else:
        print("\n[!] Hatalı seçim yaptınız! Lütfen 1-8 arasında bir seçim yapınız.")
        hm_menu()