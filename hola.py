class Hero():

    def __init__(self,name,health,armor,power,weapon):
        
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon   

        
    def print_info(self):
        print('Saludar al heroe :', self.name)
        print('Nivel de salud:', self.health)
        print('Clase de armadura:', self.armor)
        print('Poder de golpe:', self.power)
        print('Arma:', self.weapon, '\n')
        

    def strike(self, enemy):
            print(
            '→ ¡Golpe! ' + self.name + ' ataca a ' + enemy.name
            + ' con poder ' + str(self.power) + ', usando ' + self.weapon + '\n')
            enemy.armor -= self.power
            if enemy.armor < 0:   
                    enemy.health += enemy.armor
                    enemy.armor =0
                    print(
                        enemy.name + ' derrotado.\nClase de armadura soltada para ' +       
                        str(enemy.armor) + ', y nivel de salud reducido a' + str(enemy.health) + '\n')    

            if enemy.health < 0:
                    print("KO")

Sprinter = Hero("Barry Allen",100,260,195,"Speed force") 
Enemy = Hero("Digger Harkness",300,280,715,"Boomerang")

Sprinter.print_info()
Enemy.print_info()

Sprinter.strike(Enemy)