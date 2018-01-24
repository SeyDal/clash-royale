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
        self.attack_image=[pygame.image.load('images/giant_attack_up1.png'),pygame.image.load('images/giant_attack_up2.png')
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
        self.attack_image=[pygame.image.load('images/mega_minion_attack_up1.png'),pygame.image.load('images/mega_minion_attack_up2.png')
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
    window.fill((0,0,0))
    window.blit(map_picture,(0,0))



def first_troops():
    '''choose the 4 first cards to play'''
    global trooplist,dictroop
    dictroop_temp = dictroop
    if len(trooplist)==0:
        while len(trooplist)<=4:
            card_id = random.randint(0,len(dictroop_temp)-1)
            if list(dictroop_temp.values())[card_id] in trooplist:
                continue
            trooplist.append(list(dictroop_temp.values())[card_id])
            trooplist_position.append((605, window_height - (trooplist[-1].get_size()[1] * (len(trooplist)))))
            trooplist_name.append(list(dictroop_temp.keys())[card_id])
        return trooplist



def random_select_troop():
    '''choose the next new cards'''
    global trooplist,trooplist_name,trooplist_position
    dictroop_temp = dictroop
    while True:
        card_id = random.randint(0,len(dictroop_temp)-1)
        if list(dictroop_temp.values())[card_id] in trooplist:
            continue
        trooplist[card_selected[1]]=(list(dictroop_temp.values())[card_id])
        trooplist_name[card_selected[1]]=(list(dictroop_temp.keys())[card_id])
        trooplist_position[card_selected[1]]=((605,window_height-trooplist[card_selected[1]].get_size()[1]*(card_selected[1]+1)))
        return None


def drop_card():
    global card_selected,heros_in_game
    first_troops()
    if pygame.mouse.get_pressed()[0]==True :
        for i in range(len(trooplist_position)) :
            if trooplist_position[i][0] <= pygame.mouse.get_pos()[0] <= trooplist_position[i][0]+trooplist[i].get_size()[0] \
                and trooplist_position[i][1]<= pygame.mouse.get_pos()[1] <= trooplist_position[i][1]+trooplist[i].get_size()[1] and card_selected[0]==False :
                card_selected[0]=True
                card_selected[1]=i
            if card_selected[0]==True and card_selected[1]==i :
                mouse_pos=pygame.mouse.get_pos()
                card_size=trooplist[i].get_size()
                if mouse_pos[0]<card_size[0]/2 :
                    if mouse_pos[1]<card_size[1]/2:
                        trooplist_position[i]=(0,0)
                    elif mouse_pos[1]>window_height-card_size[1]/2:
                        trooplist_position[i]=(0,window_height-card_size[1])
                    else :
                        trooplist_position[i]=(0,mouse_pos[1]-card_size[1]/2)
                elif mouse_pos[0] > window_width-card_size[0] / 2:
                    if mouse_pos[1] < card_size[1] / 2:
                        trooplist_position[i] = (window_width-card_size[0], 0)
                    elif mouse_pos[1] > window_height - card_size[1] / 2:
                        trooplist_position[i] = (window_width-card_size[0], window_height - card_size[1])
                    else:
                        trooplist_position[i] = (window_width-card_size[0], mouse_pos[1] - card_size[1]/ 2)
                elif mouse_pos[1] < card_size[1] / 2:
                    trooplist_position[i] = (mouse_pos[0]-card_size[0]/2, 0)
                elif mouse_pos[1] > window_height-card_size[1]/2 :
                    trooplist_position[i] = (mouse_pos[0]-card_size[0]/2,window_height-card_size[1])
                else :
                    trooplist_position[i]=(pygame.mouse.get_pos()[0]-(trooplist[i].get_size()[0]/2),pygame.mouse.get_pos()[1]-(trooplist[i].get_size()[1]/2))
    elif card_selected[0]==True :
            if (  trooplist_position[card_selected[1]][0] <= window_width-100-trooplist[card_selected[1]].get_size()[0]/2)  :
                card_selected[0]=False
                heros_in_game.append(eval(trooplist_name[card_selected[1]])(trooplist_position[card_selected[1]],1))
                random_select_troop()
            else :
                trooplist_position[card_selected[1]]=(605,window_height-(card_selected[1]+1)*trooplist[card_selected[1]].get_size()[1])
                card_selected[0]=False
    for i in range(4):
        window.blit(trooplist[i],trooplist_position[i])



def move():
    global alive_troops
    for i in alive_troops:
        X0 = i.position[0]
        Y0 = i.position[1]
        X = X0
        Y = Y0
        if i.id == 1:
            if i.position[1] > 420 :
                if X > 300:
                    if X > 470:
                        X -= 5
                        try:
                            Y -= abs((bridge_down_right_position[1] - i.position[1]) / (
                                    bridge_down_right_position[0] - i.position[0])) * 5
                        except ZeroDivisionError:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 - 5
                    else:
                        X += 5
                        try:
                            Y -= abs((bridge_down_right_position[1] - i.position[1]) / (
                                    bridge_down_right_position[0] - i.position[0])) * 5
                        except:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 - 5
                elif X > 90:
                    X -= 5
                    try:
                        Y -= abs((bridge_down_left_position[1] - i.position[1]) / (
                                bridge_down_left_position[0] - i.position[0])) * 5
                    except:
                        Y = Y0 - 5
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 - 5
                else:
                    X += 5
                    try:
                        Y += abs((bridge_down_left_position[1] - i.position[1]) / (
                                bridge_down_left_position[0] - i.position[0])) * 5
                    except:
                        Y = Y0 - 5
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 - 5


            else:
                if X > 300:
                    if X > 470:
                        X -= 5
                        try:
                            Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                    QueenTower_up_right_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 - 5
                    else:
                        X += 5
                        try:
                            Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                    QueenTower_up_right_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 - 5
                elif X > 90:
                    X -= 5
                    try:
                        Y -= abs((QueenTower_up_lef_position[1] - i.position[1]) / (
                                QueenTower_up_lef_position[0] - i.position[0]))*5
                    except:
                        Y = Y0 - 5
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 - 5
                else:
                    X += 5
                    try:
                        Y -= abs((QueenTower_up_lef_position[1] - i.position[1]) / (
                                QueenTower_up_lef_position[0] - i.position[0]))*5
                    except:
                        Y = Y0 - 5
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 - 5
            i.position = (X, Y)


        elif i.id == 2 :
            X0 = i.position[0]
            Y0 = i.position[1]
            X = X0
            Y = Y0
            if i.position[1] < 375 :
                if X > 300:
                    if X > 470:
                        X -= 5
                        try:
                            Y += abs((bridge_up_right_position[1] - i.position[1]) / (
                                    bridge_up_right_position[0] - i.position[0])) * 5
                        except ZeroDivisionError:
                            Y = Y0 + 5
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 + 5
                    else:
                        X += 5
                        try:
                            Y += abs((bridge_up_right_position[1] - i.position[1]) / (
                                    bridge_up_right_position[0] - i.position[0])) * 5
                        except:
                            Y = Y0 + 5
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 + 5
                elif X > 90:
                    X -= 5
                    try:
                        Y += abs((bridge_up_left_position[1] - i.position[1]) / (
                                bridge_up_left_position[0] - i.position[0])) * 5
                    except:
                        Y = Y0 + 5
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 + 5
                else:
                    X += 5
                    try:
                        Y += abs((bridge_up_left_position[1] - i.position[1]) / (
                                bridge_up_left_position[0] - i.position[0])) * 5
                    except:
                        Y = Y0 + 5
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 + 5


            else:
                if X > 300:
                    if X > 470:
                        X -= 5
                        try:
                            Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                    QueenTower_down_right_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 + 8
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 + 8
                    else:
                        X += 5
                        try:
                            Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                    QueenTower_down_right_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 + 8
                        if abs(Y - Y0) > 8.5:
                            Y = Y0 + 8
                elif X > 90:
                    X -= 5
                    try:
                        Y += abs((QueenTower_down_lef_position[1] - i.position[1]) / (
                                QueenTower_down_lef_position[0] - i.position[0]))*5
                    except:
                        Y = Y0 + 8
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 + 8
                else:
                    X += 5
                    try:
                        Y += abs((QueenTower_down_lef_position[1] - i.position[1]) / (
                                QueenTower_down_lef_position[0] - i.position[0]))*5
                    except:
                        Y = Y0 + 8
                    if abs(Y - Y0) > 8.5:
                        Y = Y0 + 8
            i.position = (X, Y)




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
    , "Knight" : knight_card , "Mega_minion" : mega_minion_card , "Pekka" : pekka_card , "Balloon" : balloon_card }
card_selected=[False,0]
heros_in_game=[]
trooplist = []
trooplist_position=[]
trooplist_name=[]
window_width=700
window_height=800


bridge_up_left_position = (90.5 , 370.5)
bridge_down_left_position = (90.5 , 420.5)
bridge_up_right_position = (470.5 , 370.5)
bridge_down_right_position = (470.5 , 420.5)

QueenTower_up_lef_position = (90 , 85)
QueenTower_up_right_position = (470 , 85)
QueenTower_down_lef_position = (90 , 700)
QueenTower_down_right_position = (470 , 700)

#main()
pygame.init()
window=pygame.display.set_mode((window_width,window_height))

while True :
    draw_map()
    for i in heros_in_game :
        window.blit(i.move_image[1],i.position)
    drop_card()

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quit_game()
    pygame.display.update()


