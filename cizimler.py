import turtle

def cizim_menu():
    print("\n")
    print("╔═════════════════════════════════════╗")
    print("║           ŞEKİL ÇİZDİRME            ║")
    print("║                                     ║")
    print("║  1- Kare Çiz                        ║")
    print("║  2- Üçgen Çiz                       ║")
    print("║  3- Yıldız Çiz                      ║")
    print("║  4- Çember (Daire) Çiz              ║")
    print("║  5- İstediğin Çokgeni Çiz           ║")
    print("║  6- Ana Menüye Dön                  ║")
    print("╚═════════════════════════════════════╝")

    secim = input("Çizmek istediğiniz şekli seçiniz: ")

    if secim == "1":
        turtle.reset() 
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
        cizim_menu()

    elif secim == "2":
        turtle.reset()
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
        cizim_menu()

    elif secim == "3":
        turtle.reset()
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)
        cizim_menu()

    elif secim == "4":
        turtle.reset()
        yaricap = int(input("Yarıçapı giriniz: "))
        turtle.circle(yaricap)
        cizim_menu()

    elif secim == "5":
        turtle.reset()
        kenar = int(input("Şekil kaç kenarlı olsun?: "))
        for i in range(kenar):
            turtle.forward(80)
            turtle.right(360/kenar)
        cizim_menu()

    elif secim == "6":
        print("\n>>> Ana menüye dönülüyor...")

    else:
        print("\n[!] Hatalı seçim yaptınız! Lütfen 1-6 arasında bir seçim yapınız.")
        cizim_menu()
