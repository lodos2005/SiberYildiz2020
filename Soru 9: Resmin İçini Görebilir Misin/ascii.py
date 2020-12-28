with open('strings.txt','r') as str:
    enbuyukstring = ''
    enbuyuk= 0
    for i in str:
        deger = sum(map(ord, i.strip()))
        if (deger > enbuyuk):
            enbuyuk = deger
            enbuyukstring = i.strip()

print(enbuyuk)
print(enbuyukstring)
