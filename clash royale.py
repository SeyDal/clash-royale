import pygame,time,random,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
class Hero :
    def __init__(self,damage,hit_point,hit_speed,range,area_damage,hero_cost,hero_type,target):
        self.Damage=damage
        self.hit_point=hit_point
        self.hit_speed=hit_speed
        self.range=range
        self.area_damage=area_damage
        self.hero_cost=hero_cost
        self.type=hero_type
        self.target=target

#heros infornarions
class Wizard(Hero):
    def __init__(self,position):
        Hero.__init__(self,228,598,1.4,5.5,True,4,"ground",("air","ground","building"))
        self.position = position


class Ballon(Hero):
    def __init__(self,position):
        Hero.__init__(self,798,1396,3,1,False,5,"air",("building"))
        self.position=position


class Pekka(Hero):
    def __init__(self,position):
        Hero.__init__(self,598,1059,1.8,1,False,4,"ground",("ground","building"))
        self.position=position


class Archer(Hero):
    def __init__(self,position):
        Hero.__init__(self,86,254,1.2,2,True,2,"ground",("air","ground","building"))
        self.position=position


class Power :
    def __init__(self):
        self.radius=5
        self.duration=7.5
        self.boost=35
        self.hero_cost=3


class Giant(Hero):
    def __init__(self, position):
        Hero.__init__(self, 211, 3344, 1.5, 1 , False, 5, "ground", ("building"))
        self.position = position


class Barbar(Hero):
    def __init__(self, position):
        Hero.__init__(self, 155, 636, 1.5, 1, False, 2, "ground", ("ground", "building"))
        self.position = position


class Megaminion(Hero):
    def __init__(self, position):
        Hero.__init__(self, 258, 695, 1.5, 2, True, 3, "air", ("air","ground", "building"))
        self.position = position

#builging information
class Building :
    def __init__(self,damage,hit_point,hit_speed,range):
        self.damage=damage
        self.hit_point=hit_point
        self.hit_speed=hit_speed
        self.range=range

class King_tower (Building):
    def __init__(self,position):
        Building.__init__(self,90,4500,1,7)
        self.position=position

class Princess_tower (Building):
    def __init__(self,position):
        Building.__init__(self,100,2800,0.8,7.5)
        self.position=position



