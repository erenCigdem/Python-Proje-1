import moduller.hesapmakinesi as hesapmakinesi
import moduller.oyunlar as oyunlar
import moduller.cizimler as cizimler
import moduller.takvim as takvim
import moduller.ritmik as ritmik
import moduller.nothesaplama as nothesaplama
def anamenu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║         PYTHON ÇALIŞMALARI          ║")
    print("║                                     ║")
    print("║  1- HESAP MAKİNESİ                  ║")
    print("║  2- OYUNLAR                         ║")
    print("║  3- ŞEKİL ÇİZDİRME                  ║")
    print("║  4- TAKVİM VE YAŞ HESAPLAMA         ║")
    print("║  5- RİTMİK SAYMA                    ║")
    print("║  6- NOT HESAPLAMA                   ║")
    print("║  7- ÇARPIM TABLOSU                  ║")
    print("║  8- BMI (İDEAL KİLO) HESAPLAMA      ║")
    print("║  9- DÖVİZ / BİRİM ÇEVİRİCİ          ║")
    print("║ 10- SICAKLIK ÇEVİRME                ║")
    print("║ 11- ÇIKIŞ                           ║")
    print("╚═════════════════════════════════════╝")
    
    secim = input("Seçiminiz: ")

    if secim == "1":
        print("\n>>> Hesap Makinesi açılıyor...")
        hesapmakinesi.hm_menu()
        anamenu()
    elif secim == "2":
        print("\n>>> Oyunlar menüsü açılıyor...")
        oyunlar.oyun_menu()
        anamenu()
    elif secim == "3":
        print("\n>>> Şekil Çizdirme menüsü açılıyor...")
        cizimler.cizim_menu()
        anamenu()
    elif secim == "4":
        print("\n>>> Takvim ve Yaş Hesaplama açılıyor...")
        takvim.takvim_menu()
        anamenu()
    elif secim == "5":
        print("\n>>> Ritmik Sayma açılıyor...")
        ritmik.ritmik_menu()
        anamenu()
    elif secim == "6":
        print("\n>>> Not Hesaplama menüsü açılıyor...")
        nothesaplama.not_menu()
        anamenu()
    elif secim == "7":
        print("\n>>> Çarpım Tablosu açılıyor...")
        anamenu()
    elif secim == "8":
        print("\n>>> BMI Hesaplama açılıyor...")
        anamenu()
    elif secim == "9":
        print("\n>>> Döviz / Birim Çevirici açılıyor...")
        anamenu()
    elif secim == "10":
        print("\n>>> Sıcaklık Çevirme açılıyor...")
        anamenu()
    elif secim == "11":
        print("\nProgramdan çıkılıyor... İyi günler!")
    else:
        print("\n[!] Hatalı seçim yaptınız! Lütfen menüdeki seçeneklerden birini giriniz.")
        anamenu()

anamenu()