
'''
 House waring function
// Invitation
// familes attend
// transport
// house
// gift
// photos
//  food
'''


#DS        # HEAP
place = "indiranagar"        
floor = 3
housebulit= 2400
name ="shanthi"
print( "my house details:",place,floor,housebulit)

class invitation:
      #DS   # HEAP
      date="2-6-2022"
      location="indrianagar"
      time="6 am "

pallavi=invitation()
priyanka=invitation()
geethika=invitation()

class families:
   def attending(self):
       #STACK  #HEAP    # HEAP
        self.father= "rama"
        self.mother="seetha"
        self.brother="abhniva"
        slef.sister="preethi"
        
class family:
    def  __init__(self , f , m, s, b ):
         self.father = f
         self.mother=m
         self.brother =b
         self.sister=s

gowda=family("rama","seetha","parvathi","hanuman")
chowdary=family("james bond","preethi","naughty","fighter")
chowdarys=family("super man","wonderwomen","iran man","shark")

class public:
    def __init__(self, stop , f ):
        self.busstop =stop
        self.families =f 
        if self.busstop == "indirangar":
           self.ticket = 30
        if self.busstop == "jeevanbheema nagar":
          self.ticket = 40

bmtc=public ("indirangar",gowda)

class private:
    def __init__(self, d , f ):
        self.distance =d
        self.families =f 
        if self.distance == 12:
           self.petrol = 500
        if self.distance == 13:
           self.petrol = 600

bmw=private( 12,chowdarys )

guests= [gowda ,chowdary ,chowdarys]


def blessings(f, b ):
      print("family name",f,b)

def gifts( f, g ):
     notegift = {}
     notegift.update({f:g})
     print(notegift )
     
def photos( selfie ):
     print(" group photo",selfie[0].brother )
     
    
def house( relatives ):
     
     for i in relatives :
          bless=input("enter ur blessing")
          blessings(i,bless)
          g=input("enter ur gift")
          gifts( i, g)
          

house([gowda ,chowdary ,chowdarys])
photos([gowda ,chowdary ,chowdarys])



def food (  p ):

  if p == "veg":
   def veg():
        menu=["sweet1","sweet2","idly","vada""pangal","panner"]    
        print(menu)
   return veg
  else :
   def  nonveg():
          menu=["fish","chicken","mutton","kabab","sea food","egg"]    
          print(menu)
   return nonveg
    
gf=food("veg")
gf()
gf1=food("veg1")
gf1()
print(gf,gf1)







