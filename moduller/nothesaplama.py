def not_menu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║           NOT HESAPLAYICI           ║")
    print("║                                     ║")
    print("║  1- Vize - Final Ortalama Hesapla   ║")
    print("║  2- Harf Notu ve Geçme Durumu       ║")
    print("║  3- 3 Sınavın Not Analizi           ║")
    print("║  4- Ana Menüye Dön                  ║")
    print("╚═════════════════════════════════════╝")

    secim = input("Seçiminiz nedir?: ")

    if secim == "1":
        vize = float(input("Vize notunuzu giriniz: "))
        final = float(input("Final notunuzu giriniz: "))
        ortalama = (vize * 0.4) + (final * 0.6)
        print("Dönem Ortalamanız:", ortalama)
        if ortalama >= 50:
            print("Durum: GEÇTİNİZ! Tebrikler.")
        else:
            print("Durum: KALDINIZ.")
        not_menu()

    elif secim == "2":
        notu = float(input("Ortalamanızı giriniz (0-100): "))
        if notu >= 90 and notu <= 100: 
            print("Harf Notunuz: AA (Çok İyi - Geçti)")
        elif notu >= 80 and notu < 90:
            print("Harf Notunuz: BA (İyi - Geçti)")
        elif notu >= 70 and notu < 80:
            print("Harf Notunuz: BB (Orta-İyi - Geçti)")
        elif notu >= 60 and notu < 70:
            print("Harf Notunuz: CC (Orta - Geçti)")
        elif notu >= 50 and notu < 60:
            print("Harf Notunuz: DD (Koşullu Geçti)")
        elif notu >=0 and notu < 50:
            print("Harf Notunuz: FF (Kaldı)")
        else:
            print("[!] Hatalı giriş! Lütfen geçerli bir not giriniz.")
        not_menu()

    elif secim == "3":
        n1 = float(input("İlk notunuzu giriniz: "))
        n2 = float(input("İkinci notunuzu giriniz: "))
        n3 = float(input("Üçüncü notunuzu giriniz: "))
        notlar = [n1, n2, n3]
        ortalama = (n1 + n2 + n3) / 3
        print(f"En yüksek not: {max(notlar)}")
        print(f"En düşük not: {min(notlar)}")
        print(f"Ortalamanız: {ortalama}")
        not_menu()

    elif secim == "4":
        print("\n>>> Ana menüye dönülüyor...")

    else: 
        print("\n[!] Hatalı seçim yaptınız! Lütfen 1-4 arasında bir seçim yapınız.")
        not_menu()
        
