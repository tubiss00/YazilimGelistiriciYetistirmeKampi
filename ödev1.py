#print = yazdırmak için
#str = strings
name = str("Tuğba")
print(name)
#int = integers
age = int(22)
print(age)
#round = yuvarlamak
x = round(6.549)
print(x)
#def = define Fonksiyon tanımlamak için kullanılır.
# == = eşittir
# != = eşit değildir

mailadress = "tubiss"
şifre = "0123456789"
kullanıcıadı = input("Kullanıcı Adı : ")
şifre  =  input( "Şifre : " )

if mailadress == kullanıcıadı and şifre == şifre : 
     print("Giriş Başarılı")
elif mailadress != kullanıcıadı and şifre == şifre :
     print("Kullanıcı Adı Hatalı")
elif mailadress == kullanıcıadı and şifre != şifre :
     print("Şifre Hatalı")
else :
   print("Kullanıcı Adı ve Şifre Hatalı")

KursaKayıt = mailadress == kullanıcıadı and şifre == şifre 
if KursaKayıt :
    KursaKayıt = True 
    print("Kursa Başarıyla Kayıt Oldunuz.")
else : 
    KursaKayıt = False 
    print("İçeriği Görmek İçin Kayıt Olun ve Giriş Yapın.")
       
kurslar = [" 2023 Java Yazılım Geliştirme Yetiştirme Kampı", "Pyhton&Selenium Geliştirme Yetiştirme Kampı"]
öğretmenler = ["Engin Demirog", "Halit Kalaycı"]

if mailadress == kullanıcıadı and şifre == şifre :
    KursaKayıt = True
    print (kurslar)
    print(öğretmenler)