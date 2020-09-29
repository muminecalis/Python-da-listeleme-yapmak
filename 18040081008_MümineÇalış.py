class Araba():
    
    liste = []
    
    def __init__(self, no, marka, model, yil, km, hasar_miktari, fiyat):
        self.no = no
        self.marka = marka
        self.model = model
        self.yil = yil
        self.km = km
        self.hasar_miktari = hasar_miktari
        self.fiyat = fiyat
        
        
    def FiyatHesapla(self):
        
        if self.yil >= 2016:
            carpan=1
        if self.yil >= 2012 and self.yil <= 2015:
            carpan=0.9
        if self.yil >= 2008 and self.yil <= 2011:
            carpan=0.8
        if self.yil <= 2007:
            carpan=0.6
        if self.km <= 50000:
            birim=1
        if self.km >=50000 and self.km <= 100000:
            birim=0.9
        if self.km >= 100000 and self.km <= 200000:
            birim=0.8
        if self.km >= 200000:
            birim=0.7
            
        self.fiyat=(self.fiyat(1-self.hasar_miktari))*carpan*birim
        
    def ekle(self):
        Araba.liste.append(self)
        print("\n", self.no, self.marka, self.model , self.fiyat, self.km,  self.yil, self.hasar_miktari)
    
    
    def ArabaAra(self,no):
        for arac.no in Araba.liste:
            if (type(arac.no)==self.no):
                print("""{}\t """.format(arac.no))
    def ArabaAra(self,marka):
        for arb.marka in Araba.liste:
            if(type(arb.marka)==self.marka):
                print("""{}\t""".format(arb.marka))
                
    def Guncelle (self):
        for a in Araba.liste:
        
        Liste[1][4]= 30000
        Liste[5][2]= "Albea"
        print("guncellendi..")
        
            
        
                
                
arb1= Araba("1","Renault","Megane",2012,70000,0,100000)
arb2= Araba("2","Renault","Megane",2017,29000,0.3,100000)
arb3= Araba("3","Renault","Latitude",2015,36000,0.1,120000)
arb4= Araba("4","Renault","Latitude",2011,117000,0.2,120000)
arb5= Araba("5","Fiat","Albea",2009,150000,0.3,50000)
arb6= Araba("6","Fiat","Linea",2010,90000,0.1,60000)
arb7= Araba("7","BMW","3.20",2008,210000,0.2,120000)
arb8= Araba("8","BMW","5.20",2012,130000,0.15,140000)
arb9= Araba("9","Citroen","c5",2005,97000,0.21,100000)
arb10= Araba("10","Citroen","c4",2009,128000,0.13,80000)
arb11= Araba("11","Opel","Astra",2006,197000,0.27,80000)
arb12= Araba("12","Opel","Vectra",2007,142000,0.63,100000)

arb1.ekle()
arb2.ekle()
arb3.ekle()
arb4.ekle()
arb5.ekle()
arb6.ekle()
arb7.ekle()
arb8.ekle()
arb9.ekle()
arb1.FiyatHesapla()
arb2.FiyatHesapla()
arb3.FiyatHesapla()
arb4.FiyatHesapla()
arb1.ArabaAra()
arb2.ArabaAra()
arb3.ArabaAra()
arb2.Guncelle()
arb6.Guncelle()

        
        
            
            
            
        