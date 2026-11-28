import random

def carpim_menu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║           ÇARPIM TABLOSU            ║")
    print("║                                     ║")
    print("║  1- Seçtiğin Sayının Tablosu        ║")
    print("║  2- Tüm Çarpım Tablosu (1 - 10)     ║")
    print("║  3- Çarpım Tablosu Testi (5 Soru)   ║")
    print("║  4- Ana Menüye Dön                  ║")
    print("╚═════════════════════════════════════╝")

    secim = input("Seçiminiz nedir?: ")

    if secim == "1":
        sayi = int(input("Hangi sayının çarpım tablosunu görmek istersiniz?: "))
        print(f"\n--- {sayi} Sayısının Çarpım Tablosu ---")
        for i in range(1, 11):
            print(f"{sayi} x {i} = {sayi * i}")
        carpim_menu()

    elif secim == "2":
        print("\n--- Tüm Çarpım Tablosu (1 - 10) ---")
        for i in range(1, 11):
            for j in range(1, 11):
                print(f"{i} x {j} = {i * j}")
            print()  # Her sayının tablosundan sonra boş satır
        carpim_menu()

    elif secim == "3":
        print("\n--- Çarpım Tablosu Testi (5 Soru) ---")
        dogru_sayisi = 0
        for _ in range(5):
            sayi1 = random.randint(1, 10)
            sayi2 = random.randint(1, 10)
            cevap = int(input(f"{sayi1} x {sayi2} = ? "))
            if cevap == sayi1 * sayi2:
                print("Doğru!")
                dogru_sayisi += 1
            else:
                print(f"Yanlış! Doğru cevap: {sayi1 * sayi2}")
        print(f"\nTest tamamlandı! Doğru cevap sayınız: {dogru_sayisi}/5")
        carpim_menu()

    elif secim == "4":
        print("\n>>> Ana menüye dönülüyor...")

    else:
        print("\n[!] Hatalı seçim yaptınız! Lütfen 1-4 arasında bir seçim yapınız.")
        carpim_menu()