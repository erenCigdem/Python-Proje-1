def ritmik_menu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║            RİTMİK SAYMA             ║")
    print("║                                     ║")
    print("║  1- İleriye Doğru Ritmik Sayma      ║")
    print("║  2- Geriye Doğru Ritmik Sayma       ║")
    print("║  3- İki Sayı Arası Çift Sayılar     ║")
    print("║  4- Ana Menüye Dön                  ║")
    print("╚═════════════════════════════════════╝")

    secim = input("Seçiminiz nedir?: ")

    if secim == "1":
        baslangic = int(input("Başlangıç sayısını giriniz: "))
        bitis = int(input("Bitiş sayısını giriniz: "))
        artis = int(input("Kaçar kaçar artsın?: "))
        for sayi in range(baslangic, bitis + 1, artis):
            print(sayi)
        ritmik_menu()

    elif secim == "2":
        baslangic = int(input("Başlangıç sayısını giriniz: "))
        bitis = int(input("Bitiş sayısını giriniz: "))
        azalis = int(input("Kaçar kaçar azalsın?: "))
        for sayi in range(baslangic, bitis - 1, -azalis):
            print(sayi)
        ritmik_menu()

    elif secim == "3":
        baslangic = int(input("Başlangıç sayısını giriniz: "))
        bitis = int(input("Bitiş sayısını giriniz: "))
        for sayi in range(baslangic, bitis + 1):
            if sayi % 2 == 0:
                print(sayi)
        ritmik_menu()

    elif secim == "4":
        print("\n>>> Ana menüye dönülüyor...")

    else: 
        print("\n[!] Hatalı seçim yaptınız! Lütfen 1-4 arasında bir seçim yapınız.")
        ritmik_menu()