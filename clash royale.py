import pygame
class hero :
    def __init__(self,damage,hit_point,hit_speed,range,area_damage,hero_cost,hero_type,target):
        self.Damage=damage
        self.hit_point=hit_point
        self.hit_speed=hit_speed
        self.range=range
        self.area_damage=area_damage
        self.hero_cost=hero_cost
        self.type=hero_type
        self.target=target

class wizard(hero):
    def __init__(self,position):
        hero.__init__(self,228,598,1.4,5.5,True,4,"ground",("air","ground","building"))
        self.position = position
        
