class Fatura():
    liste = []
    fatura_ortalamasi = 0
    
    def __init__(self, fatura_no, kullanim_turu, kullanim_miktari, fatura_bedeli):
        self.fatura_no = fatura_no
        self.kullanim_turu = kullanim_turu
        self.kullanim_miktari = kullanim_miktari
        self.fatura_bedeli = fatura_bedeli
        
        fatura1:Fatura("1" , "mesken" , 12)
        fatura1.ekle()

        fatura2:Fatura("2" , "sanayi" , 150)
        fatura2.ekle()

        fatura3:("3" , "tarim" , 400)
        fatura3.ekle()

        fatura4:("4" , "mesken" , 16)
        fatura4.ekle()

        fatura5:("5" , "tarim" , 380)
        fatura5.ekle()

        fatura6:("6" , "mesken" , 5)
        fatura6.ekle()

        
    def listele(self):
         print("\n\nfatura_no\t kullanim_turu\t kullanim_miktari\t fatura_bedeli\t")
         for faturaa in Fatura.liste:
             
             if(type(faturaa) == Fatura):
                 print("""{}\t {}\t {}\t {}\t {}""".format(faturaa.fatura_no, faturaa.kullanim_turu, faturaa.kullanim_miktari, faturaa.fatura_bedeli))
   
    def fatura_hesapla(self):        
        fatura_bedeli=0
        
        if self.kullanim_turu == "mesken":
            carpan=1.15
        elif self.kullanim_turu == "sanayi":
            carpan=2.12
        elif self.kullanim_turu == "tarim":
            carpan=0.8
            
        if (self.kullanim_miktari <= 15):
            birim=4.67
        elif(self.kullanim_miktari > 15 and self.kullanim_miktari <= 200):
            birim=5.17
        elif(self.kullanim_miktari > 200):
            birim=5.67
            
        fatura_bedeli = kullanim_miktari*birim*carpan
        

            
    def ekle(self):
        Fatura.liste.append(self)
        print("\n", self.fatura_no, self.kullanim_turu, self.kullanim_miktari, self.fatura_bedeli,  " adlı fatura listeye kaydedildi...")
        
    def fatura_ortalamasi(self):
        ortalama=0
        sayi=0
        for faturaa in Fatura.liste:
            if(type(faturaa)== fatura):
                sayi += 1
                ortalama += faturaa.fatura_bedeli
                Fatura.fatura_ortalamasi = ortalama/len(Fatura.liste) 
                print(Fatura.fatura_ortalamasi)
                
                
                
    def dosyaya_kaydet(self):
        liste2 = []
        dosya=open("fatura.txt")
        liste=dosya.readlines()
        for fatura in liste:
            fatura=fatura.split()
            liste2.append(fatura)
        for i in range (len(liste2)):
            fatura=liste2
            
            
            
                



                
            
                
            
            
        
        