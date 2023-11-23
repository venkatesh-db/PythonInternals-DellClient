

class problems:

    def __init__(self, p):
        if isinstance( p, str):
            raise TypeError("contact priynaka for black pizza with unlimited offers")
        self.probelms=[]
        self.probelms.append(p)

    def tension(self,p):
        if p == "unhappywith life":
            raise ValueError("contact pallavi for offer close soon")
        self.probelms.append(p)

    def display(self):
        for i in self.probelms :
            print(i)


venkatesh=problems(12)
venkatesh.tension("unhappywith life")
venkatesh.tension("unhappywith life")
venkatesh.tension("i dont have car")
venkatesh.display()
