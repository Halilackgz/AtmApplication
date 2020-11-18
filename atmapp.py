

def işlemyap(tercih2,kullanıcıid,kullanıcıadı,şifresi,kullanıcıhesap):
    if tercih2 == "1":

        miktar = float(input("çekmek istediğiniz miktarı girin:"))

        if miktar < kullanıcıhesap:

            kullanıcıhesap -= miktar 
            kullanıcıhesap = str(kullanıcıhesap)

            print("kalan bakiyeniz ",kullanıcıhesap," $ dır.")

            güncelhesap = [kullanıcıid,kullanıcıadı,şifresi,kullanıcıhesap]
            return güncelhesap

        elif miktar > kullanıcıhesap:

            print("yeterli bakiyeniz yok !!")
            return None

    elif tercih2 == "2":

        miktar = float(input("yüklemek istediğiniz miktarı girin:"))

        kullanıcıhesap += miktar
        kullanıcıhesap = str(kullanıcıhesap)

        print("hesap bakiyeniz ",kullanıcıhesap, " $ dır.")
        güncelhesap = [kullanıcıid,kullanıcıadı,şifresi,kullanıcıhesap]
        return güncelhesap

    
    elif tercih2 == "3":

        print("tekrar bekleriz")
        return None
        
    else:
        print("bir işlem seçtiğinizden emin olun !!")
        return None

def karşılamayap(kullanıcıadı,kullanıcıhesap):

    print("hoşgeldin ",kullanıcıadı)
    print("bakiyeniz: ",kullanıcıhesap," $ dır")
    tercih = input("1:para çekmek için\n2:para yüklemek için\n3:çıkmak için\n")

    return tercih

def context():
    
    text = open("C:\\Users\\Halil\\OneDrive\\Masaüstü\\Python With HAT\\kullanıcılar.txt","r",encoding="utf-8")
    obj=text.readlines()
    i = 0
    kullancı=list()

    while i < 3:
        veri = obj[i].split(",")
        kullancı.append(veri)
        i+=1
    return kullancı

def uptadeContext(kullanıcıbilgi):
    #burada dosya güncelleme işlemi yapılacak kişinin hangi satırda olduğunun bilinmessi için id eklenecek
    #ve id okunarak o satır silinip tekrar güncellenecek
    if kullanıcıbilgi  == None:
        print("bir hata oluştu")
        return
    else:
        textoku = open("C:\\Users\\Halil\\OneDrive\\Masaüstü\\Python With HAT\\kullanıcılar.txt","r",encoding="utf-8")
        veri = textoku.readlines()
        index = int(kullanıcıbilgi[0])
        textoku.close()

        del veri[index]

        veri.insert(index,kullanıcıbilgi[0]+","+kullanıcıbilgi[1]+","+kullanıcıbilgi[2]+","+kullanıcıbilgi[3]+"\n")
        text = open("C:\\Users\\Halil\\OneDrive\\Masaüstü\\Python With HAT\\kullanıcılar.txt","w",encoding="utf-8")
        text.writelines(veri)

        text.close()
        print("işlem başarılı")

def girişkontrol(username,password):
    kullanıcı = context()
    for i in kullanıcı:

        if username == i[1] and password == i[2]:
            return i
        else:
            continue
    return None
    
def main():
    
    username = input("kullanıcı adını giriniz:")
    password = input("parolanızı girin:")

    control = True

    while control:
        veri = girişkontrol(username,password)
        if veri != None:
            kullanıcıid = veri[0]
            kullanıcıadı = veri[1]
            şifre = veri[2]
            kullanıcıhesap = veri[3]
            kullanıcıhesap = float(kullanıcıhesap)

            tercih = karşılamayap(kullanıcıadı,kullanıcıhesap)
        
            güncelveri = işlemyap(tercih,kullanıcıid,kullanıcıadı,şifre,kullanıcıhesap)
            uptadeContext(güncelveri)

            yenidenişlemkontrol = input("başka bir işlem yapmak ister misin (evet/hayır):")

            if yenidenişlemkontrol == "evet":
                control = True
            elif yenidenişlemkontrol == "hayır":
                control = False
            else:
                print("bir sorun oluştu")
                control = False
        elif veri == None:
            print("böyle bir kullanıcı yok")
            control = False
        else:
            print("bir hata oluştu")
            control=False

main()

