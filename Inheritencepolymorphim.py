

class education:

    def __init__(self, s :str , t:str ):
        print("education constructor")
        if isinstance( s ,str)and isinstance( t ,str) :
         self.school=s
         self.teacher=t
      
    def recognistion(self):
        self.topper = 99.9 

class Movie(education):

    def __init__(self,s:str,t:str,r:str,m:str ):
        print("Movie constructor")
        education.__init__(self,s,t)
        self.role =r
        self.moviename=m
     
    def recognistion(self,h:int):
      self.hits=h

    def fans(self,f:int):
      self.fans=f

class superstar(Movie):

   def __init__(self,s,t,r,m,j,h):
        print("superstar constructor")
        Movie.__init__(self,s,t,r,m)
        self.house=h
        self.jet=t
        
   def fans(self,f):
       self.fans=f


jamesbond=superstar("mirinda","prema","herione","dont miss","private jet","shanthi")
jamesbond.fans(100000000000)
jamesbond.recognistion(10)
