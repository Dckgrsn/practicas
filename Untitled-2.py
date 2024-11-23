class Mutante():
    def _init_(self,poderes, nombre, nivel, nickname):
        self.name = nombre
        self.lvl = nivel
        self.nickname = nickname
        self.power = poderes
        
    def print_info(self):
        print('Nombre:', self.name)
        print('Nickname:', self.nickname)
        print('Poderes:', self.power)
        print('Nivel:' , self.lvl)
        
class Omega(Mutante):
    def _init_(self,nombre, nickname, poderes):
        super()._init_(nombre, "Omega", nickname, poderes)
        

class Xmen(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)
        
class Xforce(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)
        
class Alfa(Mutante):
    def _init_(self,nombre,  nickname, poderes):
        super()._init_(nombre, "Alfa", nickname, poderes)
        
class Beta(Mutante):
    def _init_(self,nombre, nickname, poderes):
        super()._init_(nombre, "Beta", nickname, poderes)
        

class Jinetes(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)


class Villians(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)        

class Blue(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes) 
        
class Gold(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)        
       
class Uncanny_Xmen(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)   
        
class sons(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)        
     
class Hellfire(Mutante):
    def _init_(self,nombre, nivel, nickname, poderes):
        super()._init_(nombre, nivel, nickname, poderes)        
