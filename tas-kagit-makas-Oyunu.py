import random

#Kimin kimi yeneceğini belirleyen sözlük, bunun sayesinde else içerisindeki if-elif kısmını daha kısa tutabilirim.
yenilenler = {
    "taş": "makas",
    "makas": "kağıt",
    "kağıt": "taş"
}

secenekler = ["taş", "kağıt", "makas"]

bilgisayar_puan= 0
kullanici_puan = 0

while True:
    bilgisayar_secim = random.choice(secenekler)

    print("\nTaş, Kağıt, Makas!\nHangisini seçmek istersiniz?\n\nOyundan çıkmak için 'q' yazınız.")
    kullanici_secim = input()

    if kullanici_secim.lower() == "q":
        print(f"\nSon skor\nBİlgisayar [{bilgisayar_puan}]\nKullanıcı [{kullanici_puan}]")
        print("Oynadığınız için teşekkürler, görüşmek üzere.")
        break

    # Aşağıdaki elif bloğu sayesinde kullanıcı q vaya seçeneklerden birini yazmadığında hata mesajı veriyor ve continue sayesinde bu tur atlanıp while döngüsüne devam ediyor. Ayrıca "not in" ibaresi de secenekler içerisinde bulunmuyor anlamına geliyor.
    elif kullanici_secim.lower() not in secenekler:
        print("\nGeçersiz giriş! Lütfen taş, kağıt veya makas yazın.")
        continue

    else:
        print(f"Bilgisayar {bilgisayar_secim} seçti.\nSen {kullanici_secim} seçtin.\n")
        if kullanici_secim.lower() == bilgisayar_secim.lower():
            print("Berabere!") 
        elif yenilenler[kullanici_secim.lower()] == bilgisayar_secim:
            print("Kazandınız!")
            kullanici_puan = kullanici_puan + 1
        # Yukarıdaki elif mantığı şu şekilde işliyor: yenilenler[kullanici_secim.lower()] yukarıdaki sözlüğe bakıyor, diyelim ki kullanıcı taş seçti. Bu sözlük sayesinde buradaki değer makas oluyor ama kullanıcının seçtiği mantıken hala taş. Sonra karşılaştırma ile bakıyor bilgisayar da makas seçmiş mi. Eğer aynı ise  kullanıcı onu yenen -bu örnekte taş- değeri seçmiş oluyor böylece kullanıcı kazanıyor.
        else:
            print ("Kaybettiniz.")
            bilgisayar_puan = bilgisayar_puan + 1