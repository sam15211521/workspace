import random


class MC: # class to create the main character. it gives his base health as well as 
    def __init__(self, name_input ='', level=1, skill_input = None, weapon_input =None, armor_input =None, health_points=100, magic_points=20, attack=10, x_cor=None, y_cor=None):
        self.name = name_input
        self.level = level
        self.skills = skill_input
        self.weapon= weapon_input
        self.armor = armor_input 
        self.health = health_points+ level*10
        self.magic = magic_points +level*3
        self.attack = attack + level
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.status = []


    def move(self, direction =''):
        #function to move in any direction one space at a time
        if direction.upper() =='A': #moving left
            if self.x_cor > 1:
                self.x_cor - 1
        if direction.upper() =='D': #moving right
            if self.x_cor < 20:
                self.x_cor - 1
        if direction.upper() =='S': # moving down
            if self.y_cor < 1:
                self.y_cor -1
        if direction.upper() =='W': # moving up
            if self.y_cor < 1:
                self.y_cor -1

    def attack_move(self, target):
        pass

    def equip_wepon(self, wepon):
        pass

    def equip_armor():
        pass

    def use_magic():
        pass

class Enemy:
    def __init__(self, name_input ='', skill_input = None, weapon_input =None, armor_input =None, health_points=100, magic_points=20, level, attack, x_cor, y_cor):
        self.name = name_input
        self.skills = skill_input
        self.weapon= weapon_input
        self.armor = armor_input 
        self.health = health_points
        self.magic = magic_points
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.level = level
        self.attack = attack
        self.status = []
class Item:
    def __init__(self, wepon_damage, wepon_defence, weapon_type):
        self.damage = wepon_damage
        self.defence = wepon_defence
        self.type = weapon_type
class Weapon:
    def __init__(self, wepon_damage, wepon_defence, weapon_type):
        self.damage = wepon_damage
        self.defence = wepon_defence
        self.type = weapon_type
class Obstical:
    def __init__(self, tall, health_points) -> None:
        self.heigth  = tall
        self.health = health_points
class Armor:
    def __init__(self, DP, armor_type) -> None:
        self.defence = DP
        self.type = armor_type
class Skill:
    def __init__(self, target = 'Enemy', damage, healing, cost):
        self.target = target
        self.damage =damage
        self.healing = healing
        self.cost = cost 




