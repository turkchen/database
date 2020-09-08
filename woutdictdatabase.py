from pathlib import Path
homek = str(Path.home())+"\\desktop\\nkeys.txt"
homev = str(Path.home())+"\\desktop\\nvalues.txt"
from time import sleep
try:
    with open(homek,"r+") as f:
        pass
except FileNotFoundError:
    with open(homek,"w") as f:
        pass
try:
    with open(homev,"r+") as f:
        pass
except FileNotFoundError:
    with open(homev,"w") as f:
        pass
sifre="zxcasdqwe123"
sayac = 0
while True:
    gsifre=input("Veritabanı erişimi için şifre gereklidir:(çıkış için q) ")
    if gsifre == "q":
        quit()
    sayac += 1
    if sayac == 4:
        print("Çok fazla şifre denemesi lütfen 60sn boyunca bekleyin.")
        for i in range(60):
            sleep(1)
            print("Kalan süre: {}".format(60-i))
    
    if gsifre==sifre:
        break
    else:
        print("Şifre yanlış. tekrar deneyiniz.(kalan hak{})".format(3-sayac))

with open(homek,"r",encoding="utf-8")as f:
    keyler=f.read()
    keyler=keyler.split(",")

with open(homev,"r",encoding="utf-8") as f:
    degerler=f.read()
    degerler=degerler.split(":")
    
liste=[]
print(liste)
while True:
    choose=input("Veri okuma için -> 0 \n Veri girişi için -> 1: \n")
    if choose == "q":
        quit()
    if choose == "0":
        with open(homek,"r",encoding="utf-8") as f:
            keyler=f.read()
            keyler=keyler.split(",")
        with open(homev,"r",encoding="utf-8")as f:
            degerler=f.read()
            degerler=degerler.split(":")
        while True:
            kisi=input("Kişi ismi(key): ")
            if kisi == "q":
                break
            if kisi in keyler:
                indexkisi=keyler.index(kisi)
                degerlerindex=degerler[indexkisi].split(",")
                print(kisi," Bilgiler: ")
                for i in range(len(degerlerindex)):
                    print(degerlerindex[i])
                print("\n"*4)
            else:
                print("aradığınız kişi veritabanımızda yok!")
    
    elif choose == "1":
        while True:
            gkey=input("Kişinin ismi: ")
            if gkey=="q":
                break
            for i in range(10):
                gne=input("Ne kaydedilecek? ")
                if gne == "q":
                    break
                göz=input("Kaydedilecek şeyin özelliği: ")
                liste.append(gne+"--->"+göz+",")
            with open(homek,"a+",encoding="utf-8") as f:
                f.write(gkey+",")
            with open (homev,"a+",encoding="utf-8") as f:
                for i in liste:
                    f.write(i)
                f.write(":")
        
    
    
    
    else:
        print("Lütfen tanımladığımız bir şeyi giriniz: ")

               

            
