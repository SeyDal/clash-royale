import pygame,time,random,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
#heros infornarions
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

class Wizard(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,228,598,1.4,5.5,True,5,"ground",("air","ground","building"))
        self.position = position
        self.id=id

        #each list includes 4 image of the hero : [up1 , up2 , down1 , down2]

        self.move_image=[pygame.image.load('images/wizard_move_up1.png'),pygame.image.load('images/wizard_move_up2.png')
            ,pygame.image.load('images/wizard_move_down1.png'),pygame.image.load('images/wizard_move_down2.png')]
        self.attack_image=[pygame.image.load('images/wizard_attack_up1.png'),pygame.image.load('images/wizard_attack_up2.png')
            ,pygame.image.load('images/wizard_attack_down1.png'),pygame.image.load('images/wizard_attack_down2.png')]

class Balloon(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,798,1396,3,1,False,5,"air",("building"))
        self.position=position
        self.id=id
        self.move_image = [pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')
            ,pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')]
        self.attack_image=[pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')
            ,pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')]


class Pekka(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,598,1059,1.8,1,False,4,"ground",("ground","building"))
        self.position=position
        self.id=id
        self.move_image = [pygame.image.load('images/pekka_move_up1.png'),pygame.image.load('images/pekka_move_up2.png')
            ,pygame.image.load('images/pekka_move_down1.png'),pygame.image.load('images/pekka_move_down2.png')]
        self.attack_image=[pygame.image.load('images/pekka_attack_up1.png'),pygame.image.load('images/pekka_attack_up2.png')
            ,pygame.image.load('images/pekka_attack_down1.png'),pygame.image.load('images/pekka_attack_down2.png')]


class Archer(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,86,254,1.2,2,True,2,"ground",("air","ground","building"))
        self.position=position
        self.id=id
        self.move_image =[pygame.image.load('images/archer_move_up1.png'),pygame.image.load('images/archer_move_up2.png')
            ,pygame.image.load('images/archer_move_down1.png'),pygame.image.load('images/archer_move_down2.png')]
        self.attack_image=[pygame.image.load('images/archer_attack_up1.png'),pygame.image.load('images/archer_attack_up2.png')
            ,pygame.image.load('images/archer_attack_down1.png'),pygame.image.load('images/archer_attack_down2.png')]

class Power :
    def __init__(self,position,id):
        self.radius=5
        self.duration=7.5
        self.boost=35
        self.hero_cost=3
        self.position=position
        self.id=id
        self.move_image =[pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load()]
        self.attack_image=[pygame.image.load(),pygame.image.load(),pygame.image.load(),pygame.image.load()]


class Giant(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 211, 3344, 1.5, 1 , False, 5, "ground", ("building"))
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/giant_move_up1.png'),pygame.image.load('images/giant_move_up2.png')
            ,pygame.image.load('images/giant_move_down1.png'),pygame.image.load('images/giant_move_down2.png')]
        self.attack_image=[pygame.image.load('images/giant_attack_up1'),pygame.image.load('images/giant_attack_up2.png')
            ,pygame.image.load('images/giant_attack_down1.png'),pygame.image.load('images/giant_attack_down2.png')]

class Knight(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 159, 1399, 1.2, 1, False, 3, "ground", ("ground", "building"))
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/knight_move_up1.png'),pygame.image.load('images/knight_move_up2.png')
            ,pygame.image.load('images/knight_move_down1.png'),pygame.image.load('images/knight_move_down2.png')]
        self.attack_image=[pygame.image.load('images/knight_attack_up1.png'),pygame.image.load('images/knight_attack_up2.png')
            ,pygame.image.load('images/knight_attack_down1.png'),pygame.image.load('images/knight_attack_down2.png')]


class Mega_minion(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 258, 695, 1.5, 2, True, 3, "air", ("air","ground", "building"))
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/mega_minion_move_up1.png'),pygame.image.load('images/mega_minion_move_up2.png')
            ,pygame.image.load('images/mega_minion_move_down1.png'),pygame.image.load('images/mega_minion_move_down2.png')]
        self.attack_image=[pygame.image.load('images/mega_minion_attack_up1'),pygame.image.load('images/mega_minion_attack_up2.png')
            ,pygame.image.load('images/mega_minion_attack_down1.png'),pygame.image.load('images/mega_minion_attack_down2.png')]

#builging information
class Building :
    def __init__(self,damage,hit_point,hit_speed,range):
        self.damage=damage
        self.hit_point=hit_point
        self.hit_speed=hit_speed
        self.range=range


class King_tower (Building):
    def __init__(self,position,id):
        Building.__init__(self,90,4500,1,7)
        self.position=position
        self.image=None
        self.id=id


class Princess_tower (Building):
    def __init__(self,position,id):
        Building.__init__(self,100,2800,0.8,7.5)
        self.position=position
        self.image=None
        self.id=id



#functions
def draw_map():
    '''draw map of the game at the first of the main while loop'''
    global window
    map_picture = pygame.image.load('images/field1-Recovered.jpg')
    window.blit(map_picture,(0,0))
    first_troops()
    random_select_troop

    for i in range(4):
        window.blit(trooplist[i],(605,window_height-(trooplist[i].get_size()[1]*(i+1))))


def first_troops():
    '''choose the 4 first cards to play'''
    global trooplist,dictroop
    dictroop_temp = dictroop
    if len(trooplist)==0:
        for i in range(4):
            card_id = random.randint(0,len(dictroop_temp)-1)
            trooplist.append(list(dictroop_temp.values())[card_id])
            del(dictroop[str(list(dictroop_temp.keys())[card_id])])
        return trooplist

def random_select_troop():
    '''choose the next new cards'''
    global trooplist
    dictroop_temp = dictroop
    while True:
        card_id = random.randint(0,len(dictroop_temp)-1)
        if list(dictroop_temp.values())[card_id] in trooplist:
            continue
        trooplist.append(list(dictroop_temp.values())[card_id])
        return trooplist




def quit_game():
    pygame.quit()
    sys.exit()
#picture
archer_card=pygame.image.load('images/ArcherCard.png')
wizard_card=pygame.image.load('images/WizardCard.png')
giant_card=pygame.image.load('images/GiantCard.png')
balloon_card=pygame.image.load('images/BalloonCard.png')
knight_card=pygame.image.load('images/KnightCard.png')
pekka_card=pygame.image.load('images/MiniPEKKACard.png')
mega_minion_card=pygame.image.load('images/MegaMinionCard.png')
#variables
dictroop = {"Archer" :archer_card  , "Wizard" : wizard_card , "Giant" : giant_card
    , "Knight" : knight_card , "Megaminion" : mega_minion_card , "pekka" : pekka_card , "Baloon" : balloon_card }
trooplist = []
window_width=700
window_height=800
#main()
pygame.init()
window=pygame.display.set_mode((window_width,window_height))

while True :

    draw_map()
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quit_game()
    time.sleep(0.3)
    pygame.display.update()


