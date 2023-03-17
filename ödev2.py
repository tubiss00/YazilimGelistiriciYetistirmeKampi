krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]

print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])

print(len(krediler))

krediler[0] = "Çabuk Kredi"
print(krediler)

print(krediler[2])

for kredi in krediler:
    print("<option>" + kredi + "</option>")

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3, 10): # 3'ten başla, 10'a kadar
    print(i)

for i in range(0, 11, 2): # 0'dan başla, 11'e kadar, 2'şer artır
    print(i)
