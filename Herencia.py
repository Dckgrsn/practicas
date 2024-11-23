from time import sleep 
class Hero():

    def _init_(self, name, health, armor, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon 
        
    def print_info(self):
        print('Nivel de salud:', self.health)
        print('Clase de armadura:', self.armor, '\n')
        print('Arma:', self.weapon)
             
class Warrior(Hero):
    def hello(self):
        print('->New Hero.Un enmascarado heroe aparece en medio de las sombras y  es', self.name)
        self.print_info()
        sleep(4)
        
    def attack(self, enemy):
        print('->¡BOOM!' 'El enmascarado', self.name, 'está atacando a', enemy.name, 'con', self.weapon )
        enemy.armor -= 36
        if enemy.armor <0:
            enemy.health +=enemy.armor
            enemy.armor = 0
        print("El enmascarado a golpeado al enemigo. \nAhora su amadura: " + str(enemy.armor) + ', y nivel de salud:' + str(enemy.health) + '\n')
        sleep(5)
        
class Magician(Hero):
    def hello(self):
        print('->¡¡¡¡UN HECHICERO!!!!!!' 'Un poderoso hechicero sale del suelo y es', self.name)
        self.print_info()
        sleep(6)
        
    def attack(self,enemy):
        print('->PUFF' 'El poderoso hechihero ataca al enmascarado', self.name,'con', self.weapon )
        enemy.armor -= 85
        if enemy.amor <0:
            enemy.health +=enemy.armor
            enemy.armor=0
        print("El hechicero ha herido al enmascarado. \nAhora su amadura: " + str(enemy.armor) + ', y nivel de salud:' + str(enemy.health) + '\n')
        sleep(6)
        
Warrior = Warrior('Dick Greason', 40, 90,"batarang")
Magician = Magician('Enchantress',70, 100,"hands")