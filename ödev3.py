
ögrenciListesi = [ "Hermione Grange","Harry Potter" ,"Ron Weasly"]

 # Listedeki tüm öğrencileri tek tek ekrana yazdıran
def öğrenciListele():
    ögrenci=0
    for öğrenci in ögrenciListesi:
        print(ögrenciListesi[ögrenci])
        ögrenci += 1

öğrenciListele()


# Aldığı isim soy isim ile listeye öğrenci ekleyen
def ögrenciEkle():
    ögrenciadsoyad= input("Eklenecek olan öğrencinin adı soyadı: ")
    ögrenciListesi.append(ögrenciadsoyad)
    print(f"{ögrenciadsoyad} listeye eklenmiştir.")
    
ögrenciEkle()
öğrenciListele()    

# Listeye birden fazla öğrenci eklemeyi mümkün kılan
def ögrencilerEkle():
    ekleneceksayi = int (input("Kaç tane öğrencinin kaydı eklenecek: "))
    for i in range(ekleneceksayi):
        ekleneceköğrenci = input("Eklenecek öğrencinin adı soyadı: ")
        ögrenciListesi.append(ekleneceköğrenci)
        i +=1
 
ögrencilerEkle()
öğrenciListele()     

# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def ögrencilerSil():
    silineceksayi= int(input("Kaç tane öğrencinin kaydı silinecek: "))
    for i in range(silineceksayi):
        silinecekögrenci= input("silinecek öğrencinin adı soyadı: ")
        ögrenciListesi.remove(silinecekögrenci)
        i += 1

ögrencilerSil()
öğrenciListele()  

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def ögrenciNumaraBul():
    ögrenciadsoyad = input("Numarasını öğrenmek istediğiniz öğrencinin adı soyadı: ")
    ögrenciNo = ögrenciListesi.index(ögrenciadsoyad)
    print(f"{ögrenciadsoyad} adlı öğrencinin numarası {ögrenciNo}")

ögrenciNumaraBul()
öğrenciListele()
