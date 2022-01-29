#bu kod serisi yazılım bilimi youtube kanalı python serisi derslerini izleyip kodlarını yazdığıma dair ders notudur#
#videoların youtube kanal linki https://www.youtube.com/watch?v=R75Oo--O5Q4&ab_channel=Yaz%C4%B1l%C4%B1mBilimi#

#her ders ayrı ayrı yorum satısı arasına alınmıştır satırları açarak kodları çalıştırabilirsiniz#



import kk
import urllib.request
import sqlite3
import random
import time
import datetime
import operator
import requests
import smtplib

from bs4 import BeautifulSoup

#ders 2#

# x=3**22
# print(x)


#ders 3#

#x='yazilim bilimi \nevet'
#print(x)
#y="yazilim"
#z=" bilimi"
#print(y+z)


#ders 4#
#x=1
#print("yazilim",str(x),3)
#print(int("3")+5)


#ders 5#
#a=  "merhaba"
#print(a[1])
#print(a[0:4])
#print(len(a))


#ders 6#

#a=1
#print(type(a))


#ders 7#

#list=[1,2,3,"isim",int('312')]
#for x in range(5):
#    print(list[x])
#a="helloo"
#print(a[:2])
#print(list[:])


#ders 8#

#a=1
#b=2
#c="1/2"
#print("ben {} kadar elmayı {} kadar kişiye {} sayıda veririm".format(a,b,c))


#ders 9#

#a=str(input("who are u ?"))
#if a=="u":
#    print("OMG !")
#else:
#   print("ok ")


#ders 10#
""" bu yorum satırını bu derste öğrendim bundan sonra bunu kullanıcam
"""
#not değeri bool değerinin tersini almakda kullanılır.


#ders 11#
"""
x=0
while(x in range(10)):
    print(x)
    x = x + 1
"""


#ders 12#
"""
isim="index"
pss="hata"
while(True):
    a=str(input("kullanıcı adınızı giriniz:"))
    b=str(input("sifrenizi giriniz:"))
    if(a==isim and b==pss):
        print("hosgeldin index")
        break
    elif(a==isim or b==pss):
        print("kullanıcı adı yada sifre hatali")
        break
    else:
        print("boyle birisi yok sen kimsin ?")
        break
"""


#ders 13#
"""
liste=["kazim","bekir","necmiye","tekin"]
for i in liste:
    print(i[2])
b=20
for i in range(20):
    print(b*" ",i*"*"+i*"*")
    b=b-1
"""


#ders 14#
#faktoriyel *=i


#ders 15#
#continue deyimi döngüyü komple sonlandırmaz sadece o adımı atlar bir sonraki adıma geçer


#ders 16#
"""
def islemler(sayi):
    faktoriyel=1
    for i in range(1,sayi+1):
        faktoriyel*=i
    print("faktoriyel:",faktoriyel)
islemler(5)
"""


#ders 17#
"""
def islemler(sayi):
    faktoriyel=1
    for i in range(1,sayi+1):
        faktoriyel*=i
    return faktoriyel
a=islemler(5)
print(a)
"""


#ders 18#
"""
def a(a,b,c="bilgi yok",d="bilgi yok"):
    print("{} \n{} \n{} \n{}".format(a,b,c,d))
a(12,21)
"""


#ders 19#


#ders 20#
"""
def topla(liste):
    if len(liste)==0:
        return 0
    else:
        return liste[0]+topla(liste[1:])
print(topla([1,3,2,1,3,1]))
"""


#ders 21#
"""
a=10
def fonk():
    global a
    a=5
    print(a)
fonk()
print(a)
"""


#ders 22#
"""
sozluk={"fatih":"pc muhendisligi ogrencisi","pc":"gelismis hesap makinesi"}
#print(sozluk["fatih"])
for i in sozluk.items():
    print(i)
for i,j in sozluk.items():
    print(i+" "+j)#python burada kendi kafasına göre paketleme işlemi yapıyor çoğu dil bunu yapamıyordur

dersler={"ahmet":["mat","fizik"],"kevgir":["ahlak","din"],"ayse":["nesneye yonelik programlama","veri yapilari"]}
a=input("kisiyi giriniz:")
print("{} kisisinin aldigi dersler alttaki gibidir".format(a))
for i in dersler[a]:
    print(i)
"""


#ders 23#
"""
kk.n()
print(1)
"""


#ders 24#
"""
url1="birinci site"
url2="ikinci site"
url3="ucuncu site"
urlliste=[url1,url2,url3]
say=1
for url in urlliste:
    urllib.request.urlretrieve(url,"Resim"+str(say)+".jpg")
    say+=1
"""

#ders 25#
"""
try:
    sayi1=int(input("sayi1:"))
    sayi2=int(input("sayi2:"))
    print(sayi1/sayi2)
except ValueError:
    print("girisleriniz sayi olmali")
except ZeroDivisionError:
    print("0 ile bolumun sonucu yoktur")
except (ValueError,ZeroDivisionError):#iç içe yazmak bu şekilde gerçekleşiyor
    print("hata oluştu")
"""
#ders 26#
"""
try:
    dosya=open("yazilim.txt","r")
except IOError:
    print("dosya bulunamadı")
finally:
    dosya.close()
"""
#ders 27#
"""
dosya=open("yazilim1.txt","w")#dosya hali hazırda varsa içindekileri çöpe atıp üstüne yazar
dosya.write("write methodunu test etmek icin yazilim1 adli dosyaya bunlari yaziyorum ")
dosya=open("yazilim2.txt","a")
dosya.write("salamlar")
"""


#ders 28#
"""
try:
    dosya=open("yazilim.txt","r")

    #read()
    #readline()
    #readlines()

    #print(dosya.read())
    #print(dosya.readline())
    #print(dosya.readline())
    #print(dosya.readlines())
    dosya.close()
except FileNotFoundError:
    print("dosya yok?")
"""


#ders 29#
"""
with open ("yazilim.txt","r") as dosya:#alt satırdan çıkıldığında otomatikman dosyanın kapanmasını sağlar
    dosya.seek(10)#dosyanın içinden eleman atlamaya yarar
    print(dosya.read())
    dosya.seek(5)#en baştan başlayarak 5 eleman atlamayı sağlar
    print(dosya.read(3))#read'in içindeki 3 alınacak olan eleman sayısını temsil eder
"""


#ders 30#
"""
with open("yazilim.txt","r+") as dosya:#r+ modu hem okuma hemde yazma modudur
    data=dosya.read()
    dosya.seek(0)
    data="php:ramus52\n"+data
    dosya.write(data)
    #DOSYANIN BASINA ELEMAN EKLEME
"""
"""
with open("yazilim.txt","r+") as dosya:
    data=dosya.readlines()
    dosya.seek(0)
    data.insert(0,"eklemeli islem\n")#0. satira ekleme islemi
    dosya.writelines(data)
"""


#dosya 31#
"""
con = sqlite3.connect("dersler.db")#database oluşturma(eger dersler.db diye bir database yoksa oluşturulur varsa o database e baglanir)
cursor = con.cursor()
def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT,soyad TEXT,numara INT,ogrencinotu INT)")
    con.commit()
def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('Fatih','Uslu',128,60)")
    con.commit()
    con.close()

tablo()
degerekle()
"""


#ders 32 ,33 ve 34#
"""

con = sqlite3.connect("tablo.db")
cursor = con.cursor()

def tablolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo1(zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")
def rastgeledegerekle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('§Y-§m-§d §H:§M:§S'))
    anahtarkelime="python sqlite3"
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO tablo1(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()
tablolustur()
# bu kisim eleman ekler dikkat
#i=0
#while(i<10):
 #   rastgeledegerekle()
  #  time.sleep(1)
   # i+=1


def degerlerial():
    cursor.execute("SELECT zaman,tarih FROM tablo1 WHERE deger = 2.0")
    data=cursor.fetchall()#degerleri data'ya atmayi saglar
    for i in data:
        print(i)
degerlerial()
def silveguncelle():
    cursor.execute("SELECT zaman,tarih FROM tablo1")
    data = cursor.fetchall()  # degerleri data'ya atmayi saglar
    print("----------------ilk degerler------------------")
    for i in data:
        print(i)
    cursor.execute("UPDATE tablo1 SET deger=99 WHERE deger = 2.0")#update yerine delete yazilincada silmeye yariyor
    cursor.execute("SELECT * FROM tablo1")
    data = cursor.fetchall()  # degerleri data'ya atmayi saglar
    print("----------------guncelledikten sonra------------------")
    for i in data:
        print(i)
silveguncelle()
con.close()
"""

#ders 35#
"""
class dusman:
    kalan_can=3
    def saldir(self):
        print("hücuuuum")
        self.kalan_can-=1
    def hayatta_mi(self):
        if(self.kalan_can<=0):
            print("öldü")
        else:
            print(str(self.kalan_can)+"canin kaldi")
dusman1=dusman()
dusman2=dusman()
dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()
"""


#ders 36,37 ve 38#
"""
class dusman:

    def __init__(self,isim="düşman",kalan_can=500,saldiri_gucu=10,mermi_sayisi=30):#eğer değer girilmezse hata vermemesi için default değerler tanimlandi
        self.isim =isim#class'a ait olduğunu göstermek için self dememiz gerekli yoksa ayri bir değişken olduğunu zanneder
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi
    def print(self):#class'bağlayabilmek için self dedik
        print("basiliyor.....")
        print("isim:",self.isim,"kalan can:",self.kalan_can,"saldiri gücü:",self.saldiri_gucu,"mermi sayisi:",self.mermi_sayisi)
    def saldir(self):
        print(self.isim+"saldiriyor.")
        harcanan_mermi=random.randrange(0,10)#rastgele sayida mermi harcansin diye
        print(str(harcanan_mermi)+"kadar mermi harcandi")
        self.mermi_sayisi-=harcanan_mermi
        return(harcanan_mermi,self.saldiri_gucu)
    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print("vuruldum")
        self.kalan_can-=(harcanan_mermi*saldiri_gucu)
    def mermi_bitti_mi(self):
        if(self.mermi_sayisi<=0):
            print(self.isim+"konuşuyor: Mermim bitti oyun dişiyim")
            return True
        return False
    def hayatta_mi(self):
        if(self.kalan_can<=0):
            print(self.isim+"konuşuyor:ölüyoruuuuum..... ")
dusmanlar=[]
i=0
while(i<10):#ismi bile 1 den 10 a kadar siralanmiş özellikleri rastgele olan dusman objeleri tanımlamak için kullanıldı
    rastgelecan=random.randrange(100,200)
    rastgelesaldirigucu=random.randrange(10,20)
    rastgelemermi=random.randrange(20,30)
    yenidusman=dusman("dusman"+str(i+1),rastgelecan,rastgelesaldirigucu,rastgelemermi)#düşmanın adını ekleme yöntemimimiz oldukça havalı kullanılabilir
    dusmanlar.append(yenidusman)
    i+=1
i=0
while(i<3):
    randomdusman1=random.randrange(0,10)
    randomdusman2=random.randrange(0,10)
    donendeger=dusmanlar[randomdusman1].saldir() #(15,5)şeklinde geriye tupple dönecek
    dusmanlar[randomdusman2].saldiriyaugra(donendeger[0],donendeger[1])
    print("round bitti")
    i+=1
"""


#ders 39#
"""
class calisan():
    def __init__(self,isim,maas,departman):
       print("calisan sinifinin yapici fonksiyonu")
       self.isim=isim
       self.maas=maas
       self.departman=departman
    def bilgilerigoster(self):
        print("calisan sinifinin bilgileri gosteriliyor")
        print("isim:",self.isim ,"maas:",self.maas ,"departman:",self.departman)
    def maasazamyap(self,zam_miktari):
        print("maasazamyapiliyor")
        self.maas+=zam_miktari
    def departmandegistir(self,yeni_departman):
        print("departman degiştiriliyor")
        self.departman=yeni_departman
#calisan=calisan("fatihcan uslu",3000,"ai developer")
#calisan.bilgilerigoster()
class yonetici(calisan):#artik yonetici sinifi calisan sinifini annesi olarak kabul etti ve o class taki bütün parametreleri metodları kendisine aldı. yonetici sinifi calisan sinifindan miras aldi
    def __init__(self,isim,maas,departman,kisi_sayisi):#yukaridaki init fonksiyonunun üzerine yeni bir init fonksiyonu çağırarak override ediyoruz
        print("override edilmiş init fonksiyonunu")
        #self.isim=isim
        #self.maas=maas#isim maas ve deparman yukaridaki init içerisinden gelir
        #self.departman=departman

        super().__init__(isim,maas,departman) #üstteki gibi çağırmaktansa bu şekilde super()methodu ile tek satırdada işlemi halledebilirsin

        self.kisi_sayisi=kisi_sayisi#yeni eklediğimiz kisi sayisi buradaki init içerisinden gelir (ek özellik)
        super().bilgilerigoster()

    def bilgilerigoster(self):#üsttede olduğu için override edilecek
        print("yönetici sinifinin bilgileri gosteriliyor")
        print("isim:", self.isim, "maas:", self.maas, "departman:", self.departman,"sorumlu olduu kişi sayisi:", self.kisi_sayisi)
    def kisisayisiarttir(self,arttir):
        print("kisi sayisi arttiriliyor")
        self.kisi_sayisi+=arttir


yonetici=yonetici("fatihcan uslu",3000,"ai developer",20)
yonetici.kisisayisiarttir(17)
yonetici.bilgilerigoster()
"""


#ders 40#
"""
class ogrenci():
    def ogrencicalis(self):
        print("ogrenci suanda ders calisiyor")
class calisan():
    def calis(self):
        print("personel suanda calisiyor")
class yazilimci(ogrenci,calisan):#yazilimci'nin ebeveynleri ögrenci ve calisan sinifi oldu .
    def ogrencicalis(self):
        print("yazilimci suanda ders calisiyor")
    def calis(self):
        print("yazilimci suanda calisiyor")

yazilimci=yazilimci()
yazilimci.ogrencicalis()
yazilimci.calis()
"""


#ders 41#

#çalışmalar cmd üzerinden gerçekleşti ve çalışmadı

#ders 42#
"""
imdburl="https://www.imdb.com/chart/top/"#sayfanin url adresi
r=requests.get(imdburl)#sayfanın bütün kaynak kodunu r adlı değişkene atıyoruz
soup=BeautifulSoup(r.content,"html.parser")#BeautifulSoup'dan oluşan soup isimli bir nesne

gelen_veri=soup.find_all("table",{"class":"chart full-width"})#bütün siteden sadece table ve class="chart full-width" özelliklerini barındıran veriyi aldık
#print(gelen_veri,"\n ***********************","\n",len(gelen_veri))
#print(gelen_veri[0].contents)#tablo 3'te kaç tane veri olduğunu gösterecek
#print(len(gelen_veri[0].contents))#tablonun kaç tane elemanı olduğunu ekrana yazıyor 7 demesinin sebebi 3 tane istediğimiz elemanı 4 tane ise \n barındırmasından kaynaklanır
filmtablosu=(gelen_veri[0].contents[len(gelen_veri[0].contents)-2])#asil aradiğimiz verileri yani filmin isimlerinin yazdiği kisim tbody içinde olduğu için 5. kısma gittik
#print(filmtablosu)

filmtablosu=filmtablosu.find_all("tr")
for film in filmtablosu:#her tr için for döngüsü
    filmbasliklari=film.find_all("td",{"class":"titleColumn"})#sadece title column olan td değerlerini çekmiş olduk. filmbasliklari tek elemanli bir listedir
    filmismi=filmbasliklari[0].text
    filmismi=filmismi.replace("\n","")

    #imdb için
    filminimdb = film.find_all("td", {"class": "ratingColumn imdbRating"})
    imdbson=filminimdb[0].text
    imdbson=imdbson.replace("\n","")

    print(filmismi,"(",imdbson,")")
"""
#ders 43 ,44 ve 45#
"""
def sozlukolustur(tumkelimeler):
    kelimesayisi={}#bu iş için sözlük yapısı daha uygun olduğu için öyle yapıyoruz
    for kelime in tumkelimeler:
        if kelime in kelimesayisi:#eğer kelime daha öncedende kullanıldıysa kelime sayisini bir arttırıyoruz
            kelimesayisi[kelime]+=1
        else:#buda demektirki kelime ilk defa gelmiştir bu kelime sözlüğe eklenmelidir
            kelimesayisi[kelime]=1
    return kelimesayisi#kelime sayisini geri gönder



def sembolleritemizle(tumkelimeler):#olmamasi gereken sembolleri döngü ile temizleriz
    sembolsuzkelimeler=[]
    semboller="<>[],/'’”1234567890."
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")

        if(len(kelime) > 0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler

#bende aziz sancarin wiki hesabında aziz sancar yazan bütün kelimelere baktim
url="https://tr.wikipedia.org/wiki/Aziz_Sancar"
tumkelimeler=[]
r = requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
for kelimegruplari in soup.find_all("p"):
    icerik=kelimegruplari.text
    kelimeler=icerik.lower().split()#Aziz Sancar gibi kelimeler özel harf olduğundan büyük yazılır bu bizim için sıkıntı teşkil edebilir. split ise büyük bir metni alir parçalayarak kelimelerin adındaki listenin içine atar
    #print(kelimeler)#kelimeler listesini öylesine gösterdik
    for kelime in kelimeler:
        tumkelimeler.append(kelime)#bütün kelimeleri tumkelimeler listesine attık ayrı ayrı satırlar yerine tek satırda toplanmış oldu print ile kontrol edebilirsiniz
        #print(kelime)
tumkelimeler=sembolleritemizle(tumkelimeler)
for kelime in tumkelimeler:
    print(kelime)
sozluk=sozlukolustur(tumkelimeler)
for anahtar,deger in sorted(sozluk.items(),key=operator.itemgetter(1)):#sözlük garip gözükmesin diye bu şekilde yaptık
    print(anahtar,"=",deger)
"""


#ders 46# # gmail üzerinden 100 lerce kişiye mail göndermek
"""
content="mail"
mail=smtplib.SMTP("smtp.gmail.com",587)# bu fonksiyon 2 parametre alır . ilk parametremiz hangi mail serverina bağlanmak istiyorsun.ikinci parametremiz bu mail serveri hangi portu kullanıyor
mail.ehlo()#gmail'e kendimizi tanıtma işlemi
mail.starttls()#mail kullanıcı adı ve şifremizi şifreleyerek gmail'e gönderir
mail.login("","")#your email adress and password
mail.sendmail("","",content)#mail sender and mail getter
#daha az güvenli uygulamalara için istenilen izni açmazsan çalışmaz derslin videosunda nasil yapildiği yaziyor
"""


#ders 47#
"""
url="http://data.fixer.io/api/latest?access_key=296489d1b269257b8ecb49a6400a7dd8&format=1"#bu web sitesi bizim işimize şuanda yarayan veriyi parayla sattığı için sadece izin verdiği kısım olan euro'dan diğer bütün para birimlerine dönüşümü yapabildim
#birinci=input("birinci döviz:")#çalışmıyor
ikinci=input("ikinci döviz:")
miktar=float(input("miktar:"))
response=requests.get(url)
print(response)
print("\n")
print("*******************")
json_verisi=response.json()
print("sectiginiz para birimi olan",ikinci,"'nin EUR karsisindaki birim fiyati",json_verisi["rates"][ikinci],"kadar.",miktar,"kadar adedi ise",miktar*json_verisi["rates"][ikinci],"kadardir")
#bu apiyi kullanabilmek için ücretlendirme taleb ediyor o yüzden orada çalışamam
print("*******************\n")
print("EUR'un diger butun para birimleri karsisindaki degeri ise asagidaki gibidir :\n\n")
print(json_verisi["rates"])
"""



















