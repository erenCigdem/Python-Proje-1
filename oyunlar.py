import random

def oyun_menu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║               OYUNLAR               ║")
    print("║                                     ║")
    print("║  1- Sayı Tahmin Oyunu               ║")
    print("║  2- Taş - Kağıt - Makas             ║")
    print("║  3- Zar Atma Yarışı                 ║")
    print("║  4- Yazı - Tura Oyunu               ║")
    print("║  5- Matematik Bilgi Yarışması       ║")
    print("║  6- Ana Menüye Dön                  ║")
    print("╚═════════════════════════════════════╝")

    secim = input("Oynamak istediğiniz oyunu seçiniz: ")

    if secim == "1":
        print("\n--- SAYI TAHMİN OYUNU (1 ile 20 arası) ---")
        tutulan = random.randint(1, 20)
        kazandi = 0
        for hak in range(1, 6):
            tahmin = int(input(f"{hak}. tahmininiz: "))
            if tahmin == tutulan:
                print("Tebrikler! Doğru bildiniz!")
                kazandi = 1
                break
            elif tahmin < tutulan:
                print("Daha BÜYÜK bir sayı deneyiniz.")
            else:
                print("Daha KÜÇÜK bir sayı deneyiniz.")
        if kazandi == 0:
            print("Hakkınız bitti! Tutulan sayı:", tutulan)
        oyun_menu()

    elif secim == "2":
        print("\n--- TAŞ - KAĞIT - MAKAS ---")
        print("1- Taş | 2- Kağıt | 3- Makas")
        oyuncu = int(input("Seçiminiz (1/2/3): "))
        bilgisayar = random.randint(1, 3)

        if bilgisayar == 1:
            print("Bilgisayarın seçimi: Taş")
        elif bilgisayar == 2:
            print("Bilgisayarın seçimi: Kağıt")
        else:
            print("Bilgisayarın seçimi: Makas")

        if oyuncu == bilgisayar:
            print("Sonuç: BERABERE!")
        elif (oyuncu == 1 and bilgisayar == 3) or (oyuncu == 2 and bilgisayar == 1) or (oyuncu == 3 and bilgisayar == 2):
            print("Sonuç: TEBRİKLER, KAZANDINIZ!")
        elif (oyuncu == 1 and bilgisayar == 2) or (oyuncu == 2 and bilgisayar == 3) or (oyuncu == 3 and bilgisayar == 1):
            print("Sonuç: BİLGİSAYAR KAZANDI!")
        else:
            print("[!] Geçersiz seçim yaptınız (1, 2 veya 3 girmeliydiniz).")
        oyun_menu()

    elif secim == "3":
        print("\n--- ZAR ATMA YARIŞI ---")
        input("Zar atmak için Enter'a basınız...")
        senin_zar = random.randint(1, 6)
        pc_zar = random.randint(1, 6)
        print("Senin zarın:", senin_zar)
        print("Bilgisayarın zarı:", pc_zar)
        if senin_zar > pc_zar:
            print("Tebrikler, SEN KAZANDIN!")
        elif pc_zar > senin_zar:
            print("Bilgisayar kazandı!")
        else:
            print("Berabere!")
        oyun_menu()

    elif secim == "4":
        print("\n--- YAZI - TURA OYUNU ---")
        print("1- Yazı | 2- Tura")
        tahmin = int(input("Tahmininiz (1/2): "))
        para = random.randint(1, 2)
        if para == 1:
            print("Para atıldı -> YAZI geldi!")
        else:
            print("Para atıldı -> TURA geldi!")

        if tahmin == para:
            print("Tebrikler, DOĞRU BİLDİNİZ!")
        else:
            print("Maalesef bilemediniz.")
        oyun_menu()

    elif secim == "5":
        print("\n--- MATEMATİK BİLGİ YARIŞMASI (3 Soru) ---")
        puan = 0
        for soru in range(1, 4):
            s1 = random.randint(1, 20)
            s2 = random.randint(1, 20)
            cevap = int(input(f"{soru}. Soru: {s1} + {s2} kaçtır?: "))
            if cevap == s1 + s2:
                print("Doğru! (+10 puan)")
                puan = puan + 10
            else:
                print("Yanlış! Doğru cevap:", s1 + s2)
        print("Yarışma bitti! Toplam puanınız:", puan, "/ 30")
        oyun_menu()

    elif secim == "6":
        print("\n>>> Ana menüye dönülüyor...")

    else:
        print("\n[!] Hatalı seçim yaptınız! Lütfen 1-6 arasında bir seçim yapınız.")
        oyun_menu()