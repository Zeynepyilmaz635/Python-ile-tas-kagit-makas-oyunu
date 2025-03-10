class taşKağıtMakasOyunu():
    def __init__(self, z):
        self.z=z
        self.finish=0
        self.puan1=0
        self.puan2=0
        self.n1=0
        self.n2=0
        
        
    
        
        
    def game(self):
        name1=input("1.oyuncunun adını giriniz :")
        name2=input("2.oyuncunun adını giriniz :")
        print("0-Taş 1-Kağıt 2-Makas")
        while(self.finish==0):
            self.n1=int(input(f"{name1} tercihinizi giriniz :"))
            self.n2=int(input(f"{name2} tercihinizi giriniz :"))
            if(self.n1==0 and self.n2==1):
                self.puan2+=10; 
                print(f"Vaovv {name2} Kazandı!")
            elif(self.n1==0 and self.n2==2):
                self.puan1+=10
                print(f"Vaovv {name1} Kazandı!")
            elif(self.n1==0 and self.n2==0):
                self.puan1+=0
                self.puan2+=0
                print("berabere!")
            elif(self.n1==1 and self.n2==0):
                self.puan1+=10
                print(f"Vaovv {name1} Kazandı!")
            elif(self.n1==1 and self.n2==1):
                self.puan1+=0
                self.puan2+=0
                print("berabere!")
            elif(self.n1==1 and self.n2==2):
                self.puan2+=10
                print(f"Vaovv {name2} Kazandı!")
            elif(self.n1==2 and self.n2==0):
                self.puan2+=10
                print(f"Vaovv {name2} Kazandı!")
            elif(self.n1==2 and self.n2==1):
                self.puan1+=10
                print(f"Vaovv {name1} Kazandı!")
            elif(self.n1==2 and self.n2==2):
                self.puan1+=0
                self.puan2+=0
                print("berabere!")
                
            if(self.puan1>=30 and self.puan2<30):
                print(f"Tebrikler {name1} oyunu {name2} kişisine karşı kazandınız!")
                self.finish=1
                
            elif(self.puan2>=30 and self.puan1<30):
                print(f"Tebrikler {name2} oyunu {name1} kişisine karşı kazandınız!")
                self.finish=1
            elif(self.puan2>=30 and self.puan1>=30):
                print(f"Tebrikler {name1} ve {name2} berabere kaldınız!")
                self.finish=1
                
                
z=taşKağıtMakasOyunu(26)  
z.game()         
                
                
                
                
                
            
        