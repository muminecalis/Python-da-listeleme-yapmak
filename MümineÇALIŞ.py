class Calisan:
    def __init__(self , personel_id , isim , soyad , cocuk_sayisi , maas , calisan_sayisi) :
        
        self.personel_id = personel_id
        self.isim = isim
        self.soyad = soyad
        self.cocuk_sayisi = cocuk_sayisi
        self.maas = maas
        self.calisan_sayisi = calisan_sayisi
yonetici1 = Calisan(112 , "Mumine" , "Calis" , 1 , 40000 , 10)



yonetici1_calisan_listesi={"Sayin Sena":["Unver",2,4000,0] , "Sayin Binnur":["Karakas",3,30000,0] , "Sayin Gamze":["Bal",3,3000,0] , "Sayin Tarik":["Damlica",4,6800,0] , 
"Sayin Burak":["Toktas",5,2800,0] , "Sayin Salim":["Pancar",7,1000,0] , "Sayin Hilal":["Ceylan",1,7800,0] , "Sayin Suheda":["Sagra",4,1800,0] , "Sayin Sevgi":["Kayahan",2,3000,0] , "Sayin Seda":["Gordes",2,8500,0]}


for eleman in yonetici1_calisan_listesi:
    maas = yonetici1_calisan_listesi [eleman][2]
    if maas <= 2000:
        zamli_maas=maas*1.03
        print(eleman,yonetici1_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")
       
    
    if maas >=2000 and maas <=6000:
        zamli_maas=maas*1.04
        print(eleman,yonetici1_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")
           
            
            
    if maas >=6000:
        zamli_maas=maas*1.05
        print(eleman,yonetici1_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")

    def yeni_maas ():
        return zamli_maas+yonetici1_calisan_listesi [eleman][1]*55
    print(eleman,yonetici1_calisan_listesi[eleman][0], yeni_maas(),"TL cocuktan dolayi yeni maasiniz.")

yonetici2 = Calisan(110 , "Esra" , "Dogan" , 4 , 25000 , 12)


yonetici2_calisan_listesi={"Sayin Sumeyye":["Uzun",6,2500,0] , "Sayin Berna":["Derman",4,3800,0] , "Sayin Nehir":["Tarak",2,4000,0] , "Sayin Ali":["Sahin",1,5000,0] , 
"Sayin Emre":["Aydın",3,4200,0] , "Sayin Suleyman":["Tuncer",10,4000,0] , "Sayin Kadir":["Sevilmis",2,3200,0] , "Sayin Tugba":["Gemlik",3,6000,0] , "Sayin Sanayi":["Senar", 8,1800,0] , "Sayin Kemal":["Kunduracı",2,2000,0] , "Sayin Dogan":["Yataganli",4,3200,0] , "Sayin Melis":["Alara",2,8000,0]}


for eleman in yonetici2_calisan_listesi:
    maas = yonetici2_calisan_listesi [eleman][2]
    if maas <= 2000:
        zamli_maas=maas*1.03
        print(eleman,yonetici2_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")
       
    if maas >=2000 and maas <=6000:
        zamli_maas=maas*1.04
        print(eleman,yonetici2_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")
           
            
            
    if maas >=6000:
        zamli_maas=maas*1.05
        print(eleman,yonetici2_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")

    def yeni_maas ():
        return zamli_maas+yonetici2_calisan_listesi [eleman][1]*55
    print(eleman,yonetici2_calisan_listesi[eleman][0], yeni_maas(),"TL cocuktan dolayi yeni maasiniz.")


yonetici3 = Calisan(155 , "Busra" , "Gur" , 3 , 20000 , 10)


yonetici3_calisan_listesi={"Sayin Seyma":["Donmez",3,5000,0] , "Sayin Beyza":["Karatas",1,1000,0] , "Sayin Aleyna":["Savas",6,1000,0] , "Sayin Halil":["Duran",0,2500,0] , 
"Sayin Huseyin":["Cayci",3,9000,0] , "Sayin Nuran":["Toklu",2,4000,0] , "Sayin Sevilay":["Taner",2,1500,0] , "Sayin Tacettin":["Taci",2,4200,0] , "Sayin Soner":["Bulut",5,6500,0] , "Sayin Aslı":["Ozay",2,8000,0]}
    	
for eleman in yonetici3_calisan_listesi:
    maas = yonetici3_calisan_listesi [eleman][2]
    if maas <= 2000:
        zamli_maas=maas*1.03
        print(eleman,yonetici3_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")
       
    
    if maas >=2000 and maas <=6000:
        zamli_maas=maas*1.04
        print(eleman,yonetici3_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")
           
            
            
    if maas >=6000:
        zamli_maas=maas*1.05
        print(eleman,yonetici3_calisan_listesi[eleman][0], zamli_maas,"TL","zamli","maas","alacaksiniz.")

    def yeni_maas ():
        return zamli_maas+yonetici3_calisan_listesi [eleman][1]*55
    print(eleman,yonetici3_calisan_listesi[eleman][0], yeni_maas(),"TL cocuktan dolayi yeni maasiniz.")

yonetici1 = {"Sayin Mumine":["Calis" , 1 , 40000 , 10 , 30]}

for eleman in yonetici1:
    maas=yonetici1[eleman][2]
    if maas <= 10000:
        zamli_maas=maas*1.05
        print(eleman,yonetici1[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
        
        
    if maas >= 10000 and maas <= 20000:
        zamli_maas=maas*1.06
        print(eleman,yonetici1[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
        
    if maas >= 20000:
        zamli_maas=maas*1.07
        print(eleman,yonetici1[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
        
        
            
    
    def yeni_maas():
        return ((zamli_maas + yonetici1 [eleman][1]*85) + (yonetici1[eleman][4]*yonetici1[eleman][3]))
    print(eleman,yonetici1[eleman][0],yeni_maas(),"Tl", "prim" ,"ve" , "cocuk sayisindan dolayı" , "alacaginiz" , "tutardir.")

    
    
    
     
    
    
yonetici2 = {"Sayin Esra":["Dogan",4,25000,12,30]}  

for eleman in yonetici2:
    maas=yonetici2[eleman][2]
    
    if maas <= 10000:
        zamli_maas=maas*1.05
        print(eleman,yonetici2[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
        
        
    if maas >= 10000 and maas <= 20000:
        zamli_maas=maas*1.06
        print(eleman,yonetici2[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
        
    if maas >= 20000:
        zamli_maas=maas*1.07
        print(eleman,yonetici2[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
            
    
    def yeni_maas():
        return ((zamli_maas + yonetici2 [eleman][1]*85) + (yonetici2[eleman][4]*yonetici2[eleman][3]))
    print(eleman,yonetici2[eleman][0],yeni_maas(),"Tl", "prim" ,"ve" , "cocuk sayisindan dolayı" , "alacaginiz" , "tutardir.")
    
    
yonetici3 = {"Sayin Busra":["Gur",3,20000,10,30]}

for eleman in yonetici3:
    maas=yonetici3[eleman][2]
    
    if maas <= 10000:
        zamli_maas=maas*1.05
        print(eleman,yonetici3[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
        
        
    if maas >= 10000 and maas <= 20000:
        zamli_maas=maas*1.06
        print(eleman,yonetici3[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
        
    if maas >= 20000:
        zamli_maas=maas*1.07
        print(eleman,yonetici3[eleman][0],zamli_maas,"TL" , "zamli" , "maas" , "alacaksiniz.")
            
    
    def yeni_maas():
        return ((zamli_maas + yonetici3 [eleman][1]*85) + (yonetici3[eleman][4]*yonetici3[eleman][3]))
    print(eleman,yonetici3[eleman][0],yeni_maas(),"Tl", "prim" ,"ve" , "cocuk sayisindan dolayı" , "alacaginiz" , "tutardir.")  
    
yonetici1_calisan_listesi={"Sena":["Unver",2,4000,0] , "Binnur":["Karakas",3,30000,0] , "Gamze":["Bal",3,3000,0] , "Tarik":["Damlica",4,6800,0] , 
"Burak":["Toktas",5,2800,0] , "Salim":["Pancar",7,1000,0] , "Hilal":["Ceylan",1,7800,0] , "Suheda":["Sagra",4,1800,0] , "Sevgi":["Kayahan",2,3000,0] , "Seda":["Gordes",2,8500,0]}
ortalama_maas1=0
for eleman in yonetici1_calisan_listesi:
    ortalama_maas1=((yonetici1_calisan_listesi[eleman][2])+ortalama_maas1)
ortalama_maas1= ortalama_maas1/10
print(ortalama_maas1,"Tl Mumine Calis calisanlarinin maas ortalamasidir.")

yonetici2_calisan_listesi={"Sayin Sumeyye":["Uzun",6,2500,0] , "Sayin Berna":["Derman",4,3800,0] , "Sayin Nehir":["Tarak",2,4000,0] , "Sayin Ali":["Sahin",1,5000,0] , 
"Sayin Emre":["Aydın",3,4200,0] , "Sayin Suleyman":["Tuncer",10,4000,0] , "Sayin Kadir":["Sevilmis",2,3200,0] , "Sayin Tugba":["Gemlik",3,6000,0] , "Sayin Sanayi":["Senar", 8,1800,0] , "Sayin Kemal":["Kunduracı",2,2000,0] , "Sayin Dogan":["Yataganli",4,3200,0] , "Sayin Melis":["Alara",2,8000,0]}
ortalama_maas2=0
for eleman in yonetici2_calisan_listesi:
    ortalama_maas2=((yonetici2_calisan_listesi[eleman][2])+ortalama_maas2)
ortalama_maas2=ortalama_maas2/12
print(ortalama_maas2,"Tl Esra Dogan calisanlarinin maas ortalamasidir.")

yonetici3_calisan_listesi={"Sayin Seyma":["Donmez",3,5000,0] , "Sayin Beyza":["Karatas",1,1000,0] , "Sayin Aleyna":["Savas",6,1000,0] , "Sayin Halil":["Duran",0,2500,0] , 
"Sayin Huseyin":["Cayci",3,9000,0] , "Sayin Nuran":["Toklu",2,4000,0] , "Sayin Sevilay":["Taner",2,1500,0] , "Sayin Tacettin":["Taci",2,4200,0] , "Sayin Soner":["Bulut",5,6500,0] , "Sayin Aslı":["Ozay",2,8000,0]}
ortalama_maas3=0
for eleman in yonetici3_calisan_listesi:
    ortalama_maas3=((yonetici3_calisan_listesi[eleman][2])+ortalama_maas3)
ortalama_maas3=ortalama_maas3/10
print(ortalama_maas3,"Tl Busra Gur calisanlarinin maas ortalamasidir.")

yonetici_listesi={"Sayin Mumine":["Calis",1,40000,10] , "Sayin Esra":["Dogan",4,25000,12],"Sayin Busra":["Gur",3,20000,10]}
ortalama_yonetici=0
for eleman in yonetici_listesi:
    ortalama_yonetici=((yonetici_listesi[eleman][2])+ortalama_yonetici)
ortalama_yonetici=ortalama_yonetici/3
print(ortalama_yonetici,"Tl yoneticilerin ortalama maasidir.")

sirket_calisanlari={"Sayin Sena":["Unver",2,4000,0] , "Sayin Binnur":["Karakas",3,30000,0] , "Sayin Gamze":["Bal",3,3000,0] , "Sayin Tarik":["Damlica",4,6800,0] , 
"Sayin Burak":["Toktas",5,2800,0] , "Sayin Salim":["Pancar",7,1000,0] , "Sayin Hilal":["Ceylan",1,7800,0] , "Sayin Suheda":["Sagra",4,1800,0] , "Sayin Sevgi":["Kayahan",2,3000,0] , "Sayin Seda":["Gordes",2,8500,0],"Sayin Sumeyye":["Uzun",6,2500,0] , "Sayin Berna":["Derman",4,3800,0] , "Sayin Nehir":["Tarak",2,4000,0] , "Sayin Ali":["Sahin",1,5000,0] , 
"Sayin Emre":["Aydın",3,4200,0] , "Sayin Suleyman":["Tuncer",10,4000,0] , "Sayin Kadir":["Sevilmis",2,3200,0] , "Sayin Tugba":["Gemlik",3,6000,0] , "Sayin Sanayi":["Senar", 8,1800,0] , "Sayin Kemal":["Kunduracı",2,2000,0] , "Sayin Dogan":["Yataganli",4,3200,0] , "Sayin Melis":["Alara",2,8000,0],"Sayin Seyma":["Donmez",3,5000,0] , "Sayin Beyza":["Karatas",1,1000,0] , "Sayin Aleyna":["Savas",6,1000,0] , "Sayin Halil":["Duran",0,2500,0] , 
"Sayin Huseyin":["Cayci",3,9000,0] , "Sayin Nuran":["Toklu",2,4000,0] , "Sayin Sevilay":["Taner",2,1500,0] , "Sayin Tacettin":["Taci",2,4200,0] , "Sayin Soner":["Bulut",5,6500,0] , "Sayin Aslı":["Ozay",2,8000,0] , "Sayin Mumine":["Calis",1,40000,10] , "Sayin Esra":["Dogan",4,25000,12] , "Sayin Busra":["Gur",2,20000,10]}
ortalama_sirket=0
for eleman in sirket_calisanlari:
    ortalama_sirket=((sirket_calisanlari[eleman][2])+ortalama_sirket)
ortalama_sirket=ortalama_sirket/35
print(ortalama_sirket,"Tl tum sirket calisanlarinin ortalamasıdır")


personeller={"Sayin Sena":["Unver",2,4000,0] , "Sayin Binnur":["Karakas",3,30000,0] , "Sayin Gamze":["Bal",3,3000,0] , "Sayin Tarik":["Damlica",4,6800,0] , 
"Sayin Burak":["Toktas",5,2800,0] , "Sayin Salim":["Pancar",7,1000,0] , "Sayin Hilal":["Ceylan",1,7800,0] , "Sayin Suheda":["Sagra",4,1800,0] , "Sayin Sevgi":["Kayahan",2,3000,0] , "Sayin Seda":["Gordes",2,8500,0],"Sayin Sumeyye":["Uzun",6,2500,0] , "Sayin Berna":["Derman",4,3800,0] , "Sayin Nehir":["Tarak",2,4000,0] , "Sayin Ali":["Sahin",1,5000,0] , 
"Sayin Emre":["Aydın",3,4200,0] , "Sayin Suleyman":["Tuncer",10,4000,0] , "Sayin Kadir":["Sevilmis",2,3200,0] , "Sayin Tugba":["Gemlik",3,6000,0] , "Sayin Sanayi":["Senar", 8,1800,0] , "Sayin Kemal":["Kunduracı",2,2000,0] , "Sayin Dogan":["Yataganli",4,3200,0] , "Sayin Melis":["Alara",2,8000,0],"Sayin Seyma":["Donmez",3,5000,0] , "Sayin Beyza":["Karatas",1,1000,0] , "Sayin Aleyna":["Savas",6,1000,0] , "Sayin Halil":["Duran",0,2500,0] , 
"Sayin Huseyin":["Cayci",3,9000,0] , "Sayin Nuran":["Toklu",2,4000,0] , "Sayin Sevilay":["Taner",2,1500,0] , "Sayin Tacettin":["Taci",2,4200,0] , "Sayin Soner":["Bulut",5,6500,0] , "Sayin Aslı":["Ozay",2,8000,0]}
for eleman in personeller:
    maas=personeller[eleman][2]
    
    
    if maas <= 2000:
        zamli_maas=maas*1.03
        print(eleman,personeller[eleman][0], zamli_maas,"Tl bu yilki zamli maasinizdir.")
       
    
    if maas >=2000 and maas <=6000:
        zamli_maas=maas*1.04
        print(eleman,personeller[eleman][0], zamli_maas,"Tl bu yilki zamli maasinizdir.")
           
            
            
    if maas >=6000:
        zamli_maas=maas*1.05
        print(eleman,personeller[eleman][0],zamli_maas,"Tl bu yilki zamli maasinizdir.")

        def iki_yil_sonra_maas():
            return zamli_maas*1.08
        print(eleman,personeller[eleman][0],iki_yil_sonra_maas(),"Tl iki yil sonraki maasinizdir.")
        def uc_yil_sonra_maas():
            return iki_yil_sonra_maas()*1.09
        print(eleman,personeller[eleman][0],uc_yil_sonra_maas(),"Tl uc yil sonraki maasinizdir.")
        
yoneticiler={"Sayin Mumine":["Calis",1,40000,10] , "Sayin Esra":["Dogan",4,25000,12],"Sayin Busra":["Gur",3,20000,10]}
for eleman in yoneticiler:
    maas=yoneticiler[eleman][2]
    if maas <= 10000:
        zamli_maas=maas*1.05
        print(eleman,yoneticiler[eleman][0],zamli_maas,"Bu yilki zamli maasinizdir.")
        
        
    if maas >= 10000 and maas <= 20000:
        zamli_maas=maas*1.06
        print(eleman,yoneticiler[eleman][0],zamli_maas,"TL bu yilki zamli maasinizdir.")
        
    if maas >= 20000:
        zamli_maas=maas*1.07
        print(eleman,yoneticiler[eleman][0],zamli_maas,"Tl bu yilki zamli maasinizdir.")
        
        def iki_yil_sonra_maas():
            return zamli_maas*1.10
        print(eleman,yoneticiler[eleman][0],iki_yil_sonra_maas(),"Tl iki yil sonraki maasinizdir.")
        def uc_yil_sonra_maas():
            return iki_yil_sonra_maas()*1.12
        print(eleman,yoneticiler[eleman][0],uc_yil_sonra_maas(),"Tl uc yil sonraki maasinizdir.")
        
        
    
calisan_listesi=["Sena Unver", "Binnur Karakas" ,"Gamze Bal", "Tarik Damlica","Burak Toktas", "Salim Pancar","Hilal Ceylan" , "Suheda Sagra" , "Sevgi Kayahan" , "Seda Gordes" , "Sumeyye Uzun" , "Berna Derman" , "Nehir Tarak" , "Ali Sahin" , "Emre Aydin" , "Suleyman Tuncer" , "Kadir Sevilmis" , "Tugba Gemlik" , "Sanayi Senar" , "Kemal Kunduraci" , "Dogan Yataganli" , "Melis Alara" , "Seyma Donmez" , "Beyza Karatas" , "Aleyna Savas" , "Halil Duran" , "Huseyin Cayci" , "Nuran Toklu" , "Sevilay Taner" , "Tacettin Taci" , "Soner Bulut" , "Aslı Ozay"] 

calisan_listesi.append("Mumine Calis")
calisan_listesi.append("Esra Dogan")
calisan_listesi.append("Busra Gur")

calisanlar= len(calisan_listesi)
t=0
while(t<calisanlar):
    print(calisan_listesi[t])
    t=t+1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








    




    
    
    
       