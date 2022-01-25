import random


class MC: # class to create the main character. it gives his base health as well as 
    def __init__(self, name_input ='', level, skill_input = None, weapon_input =None, armor_input =None, health_points=100, magic_points=20, attack=10):
        self.name = name_input\
        self.level = level
        self.skills = skill_input
        self.weapon= weapon_input
        self.armor = armor_input 
        self.health = health_points+ level*10
        self.magic = magic_points +level*3
        self.attack = attack + level
        self.status = []


    def move():
        
class Enemy:
    def __init__(self, name_input ='', skill_input = None, weapon_input =None, armor_input =None, health_points=100, magic_points=20):
        self.name = name_input
        self.skills = skill_input
        self.weapon= weapon_input
        self.armor = armor_input 
        self.health = health_points
        self.magic = magic_points
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
        pass

