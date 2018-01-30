import pygame,time,random,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import  pygame.time as GAME_TIME

#heros infornarions
class Hero :
    def __init__(self,damage,hit_point,hit_speed,range,area_damage,hero_cost,hero_type,target,speed):
        self.damage=damage
        self.hit_point=hit_point
        self.hit_speed=hit_speed
        self.range=range
        self.area_damage=area_damage
        self.hero_cost=hero_cost
        self.type=hero_type
        self.target=target
        self.speed=speed

class Inferno(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,200,1500,4,12,True,5,"building",("air","ground","building"),10)
        self.position=position
        self.id=id
        self.move_image =[pygame.image.load('images/Inferno.png'),pygame.image.load('images/Inferno.png')
            ,pygame.image.load('images/Inferno.png'),pygame.image.load('images/Inferno.png')]
        self.attack_image=[pygame.image.load('images/Inferno.png'),pygame.image.load('images/Inferno.png')
            ,pygame.image.load('images/Inferno.png'),pygame.image.load('images/Inferno.png')]
        self.weapon_image = [pygame.image.load ("images/Inferno_arrow.png") , self.position]
        self.max_health = 1500


class Tesla(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,150,1500,4,10,False,4,"building",("air","ground","building"),10)
        self.position=position
        self.id=id
        self.move_image =[pygame.image.load('images/Tesla.png'),pygame.image.load('images/Tesla.png')
            ,pygame.image.load('images/Tesla.png'),pygame.image.load('images/Tesla.png')]
        self.attack_image=[pygame.image.load('images/Tesla.png'),pygame.image.load('images/Tesla.png')
            ,pygame.image.load('images/Tesla.png'),pygame.image.load('images/Tesla.png')]
        self.weapon_image = [pygame.image.load ("images/Tesla_arrow.png") , self.position]
        self.max_health = 1500



class Wizard(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,228,598,4,8,True,5,"ground",("air","ground","building"),10)
        self.position = position
        self.id=id

        #each list includes 4 image of the hero : [up1 , up2 , down1 , down2]

        self.move_image=[pygame.image.load('images/wizard_move_up1.png'),pygame.image.load('images/wizard_move_up2.png')
            ,pygame.image.load('images/wizard_move_down1.png'),pygame.image.load('images/wizard_move_down2.png')]
        self.attack_image=[pygame.image.load('images/wizard_attack_up1.png'),pygame.image.load('images/wizard_attack_up2.png')
            ,pygame.image.load('images/wizard_attack_down1.png'),pygame.image.load('images/wizard_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/Wizard_fire.png") , self.position]
        self.max_health = 598

class Balloon(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,798,1696,5,2,False,5,"air",("building"),15)
        self.position=position
        self.id=id
        self.move_image = [pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')
            ,pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')]
        self.attack_image=[pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')
            ,pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]
        self.max_health = 1396



class Pekka(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,300,1059,6,4,False,4,"ground",("ground","building"),8)
        self.position=position
        self.id=id
        self.move_image = [pygame.image.load('images/pekka_move_up1.png'),pygame.image.load('images/pekka_move_up2.png')
            ,pygame.image.load('images/pekka_move_down1.png'),pygame.image.load('images/pekka_move_down2.png')]
        self.attack_image=[pygame.image.load('images/pekka_attack_up1.png'),pygame.image.load('images/pekka_attack_up2.png')
            ,pygame.image.load('images/pekka_attack_down1.png'),pygame.image.load('images/pekka_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]
        self.max_health = 1059


class Archer(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,120,254,4,6,False,2,"ground",("air","ground","building"),10)
        self.position=position
        self.id=id
        self.move_image =[pygame.image.load('images/archer_move_up1.png'),pygame.image.load('images/archer_move_up2.png')
            ,pygame.image.load('images/archer_move_down1.png'),pygame.image.load('images/archer_move_down2.png')]
        self.attack_image=[pygame.image.load('images/archer_attack_up1.png'),pygame.image.load('images/archer_attack_up2.png')
            ,pygame.image.load('images/archer_attack_down1.png'),pygame.image.load('images/archer_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/Queen_tower_arrow.png") , self.position]
        self.max_health = 254




class Giant(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 211, 3344, 5, 4 , False, 5, "ground", ("building"),15)
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/giant_move_up1.png'),pygame.image.load('images/giant_move_up2.png')
            ,pygame.image.load('images/giant_move_down1.png'),pygame.image.load('images/giant_move_down2.png')]
        self.attack_image=[pygame.image.load('images/giant_attack_up1.png'),pygame.image.load('images/giant_attack_up2.png')
            ,pygame.image.load('images/giant_attack_down1.png'),pygame.image.load('images/giant_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]
        self.max_health = 3344

class Knight(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 119, 1399, 4, 4, False, 3, "ground", ("ground", "building"),12)
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/knight_move_up1.png'),pygame.image.load('images/knight_move_up2.png')
            ,pygame.image.load('images/knight_move_down1.png'),pygame.image.load('images/knight_move_down2.png')]
        self.attack_image=[pygame.image.load('images/knight_attack_up1.png'),pygame.image.load('images/knight_attack_up2.png')
            ,pygame.image.load('images/knight_attack_down1.png'),pygame.image.load('images/knight_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]
        self.max_health = 1399


class Mega_minion(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 228, 695, 3, 5, True, 3, "air", ("air","ground", "building"),10)
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/mega_minion_move_up1.png'),pygame.image.load('images/mega_minion_move_up2.png')
            ,pygame.image.load('images/mega_minion_move_down1.png'),pygame.image.load('images/mega_minion_move_down2.png')]
        self.attack_image=[pygame.image.load('images/mega_minion_attack_up1.png'),pygame.image.load('images/mega_minion_attack_up2.png')
            ,pygame.image.load('images/mega_minion_attack_down1.png'),pygame.image.load('images/mega_minion_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/Megaminion_arrow.png") , self.position]
        self.max_health = 695

    #builging information
class Building :
    def __init__(self,damage,hit_point,hit_speed,range,type,target):
        self.damage=damage
        self.hit_point=hit_point
        self.hit_speed=hit_speed
        self.range=range
        self.type=type
        self.target=target
        self.destroyed_image=pygame.image.load('images\Queen_tower_broken.png')



class King_tower (Building):
    def __init__(self,position,id,image):
        Building.__init__(self,100,4500,1,8,"building",('air','ground','building'))
        self.position=position
        self.image=[image,image,image,image]
        self.attack_image=[image,image,image,image]
        self.weapon_image = [pygame.image.load ("images/King_tower_arrow.png") , self.position]
        self.id=id
        self.max_health = 4500


class Princess_tower (Building):
    def __init__(self,position,id,image):
        Building.__init__(self,65,2800,2,16,"building",('air','ground','building'))
        self.position=position
        self.image=[image,image,image,image]
        self.attack_image=[image,image,image,image]
        self.weapon_image = [pygame.image.load ("images/Queen_tower_arrow.png") , self.position]
        self.id=id
        self.max_health = 2800



#functions
def draw_map():
    '''draw map of the game at the first of the main while loop'''
    global window,map_picture
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
    ''' a function to drag cards and create an object of its type'''
    global card_selected,heros_in_game,elixirs_teem1,last_card,last_card_check
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
    elif card_selected[0] == True:
        if (trooplist_position[card_selected[1]][0] <= window_width - 100 - trooplist[card_selected[1]].get_size()[
            0] / 2) \
                and elixirs_teem1 >= eval(trooplist_name[card_selected[1]])(trooplist_position[card_selected[1]],
                                                                            1).hero_cost:
            if towers[0] in destroyed_towers and towers[1] in destroyed_towers:
                if trooplist_position[card_selected[1]][1]+trooplist[card_selected[1]].get_size()[1]/2 > 269 + 25 :
                    card_selected[0] = False
                    if 380<trooplist_position[card_selected[1]][1]<460 :
                        heros_in_game.append(eval(trooplist_name[card_selected[1]])((trooplist_position[card_selected[1]][0],460), 1))
                    else :
                        heros_in_game.append(eval(trooplist_name[card_selected[1]])(trooplist_position[card_selected[1]], 1))
                    attacking_heros_in_game.append(False)
                    target_heros_in_game.append([])
                    last_card=heros_in_game[-1]
                    last_card_check=False
                    elixirs_teem1 -= heros_in_game[-1].hero_cost
                    random_select_troop()
                else:
                    trooplist_position[card_selected[1]] = (
                        605, window_height - (card_selected[1] + 1) * trooplist[card_selected[1]].get_size()[1])
                    card_selected[0] = False
            elif towers[0] not in destroyed_towers and towers[1] not in destroyed_towers:
                if trooplist_position[card_selected[1]][1]+trooplist[card_selected[1]].get_size()[1]/2 > red_image.get_size()[1]:
                    card_selected[0] = False
                    if 380 < trooplist_position[card_selected[1]][1] < 460:
                        heros_in_game.append(
                            eval(trooplist_name[card_selected[1]])((trooplist_position[card_selected[1]][0], 460), 1))
                    else:
                        heros_in_game.append(
                            eval(trooplist_name[card_selected[1]])(trooplist_position[card_selected[1]], 1))
                    attacking_heros_in_game.append(False)
                    target_heros_in_game.append([])
                    last_card = heros_in_game[-1]
                    last_card_check = False
                    elixirs_teem1 -= heros_in_game[-1].hero_cost
                    random_select_troop()
                else:
                    trooplist_position[card_selected[1]] = (
                        605, window_height - (card_selected[1] + 1) * trooplist[card_selected[1]].get_size()[1])
                    card_selected[0] = False
            elif towers[0] not in destroyed_towers and towers[1] in destroyed_towers:
                if trooplist_position[card_selected[1]][1]+trooplist[card_selected[1]].get_size()[1]/2 > red_image.get_size()[1] or \
                        (trooplist_position[card_selected[1]][0]-trooplist[card_selected[1]].get_size()[0]/2 >= red_image.get_size()[0] and trooplist_position[card_selected[1]][1]+trooplist[card_selected[1]].get_size()[1]/2 > 269 + 25):
                    card_selected[0] = False
                    if 380 < trooplist_position[card_selected[1]][1] < 460:
                        heros_in_game.append(
                            eval(trooplist_name[card_selected[1]])((trooplist_position[card_selected[1]][0], 460), 1))
                    else:
                        heros_in_game.append(
                            eval(trooplist_name[card_selected[1]])(trooplist_position[card_selected[1]], 1))
                    attacking_heros_in_game.append(False)
                    target_heros_in_game.append([])
                    last_card = heros_in_game[-1]
                    last_card_check = False
                    elixirs_teem1 -= heros_in_game[-1].hero_cost
                    random_select_troop()
                else:
                    trooplist_position[card_selected[1]] = (
                        605, window_height - (card_selected[1] + 1) * trooplist[card_selected[1]].get_size()[1])
                    card_selected[0] = False
            elif towers[0] in destroyed_towers and towers[1] not in destroyed_towers:
                if trooplist_position[card_selected[1]][1]+trooplist[card_selected[1]].get_size()[1]/2 > red_image.get_size()[1] or \
                        (trooplist_position[card_selected[1]][0]-trooplist[card_selected[1]].get_size()[0]/2 <= red_image.get_size()[0] and trooplist_position[card_selected[1]][1]+trooplist[card_selected[1]].get_size()[1]/2 > 269 + 25):
                    card_selected[0] = False
                    if 380 < trooplist_position[card_selected[1]][1] < 460:
                        heros_in_game.append(
                            eval(trooplist_name[card_selected[1]])((trooplist_position[card_selected[1]][0], 460), 1))
                    else:
                        heros_in_game.append(
                            eval(trooplist_name[card_selected[1]])(trooplist_position[card_selected[1]], 1))
                    attacking_heros_in_game.append(False)
                    target_heros_in_game.append([])
                    last_card = heros_in_game[-1]
                    last_card_check = False
                    elixirs_teem1 -= heros_in_game[-1].hero_cost
                    random_select_troop()
                else:
                    trooplist_position[card_selected[1]] = (
                        605, window_height - (card_selected[1] + 1) * trooplist[card_selected[1]].get_size()[1])
                    card_selected[0] = False
            else:
                trooplist_position[card_selected[1]] = (
                    605, window_height - (card_selected[1] + 1) * trooplist[card_selected[1]].get_size()[1])
                card_selected[0] = False

        else:
            trooplist_position[card_selected[1]] = (
            605, window_height - (card_selected[1] + 1) * trooplist[card_selected[1]].get_size()[1])
            card_selected[0] = False
    for i in range(4):
        window.blit(trooplist[i], trooplist_position[i])

def move():
    #moving troops by using mathematics
    global heros_in_game
    for i in heros_in_game:
        k = 1
        m = 10
        if i.type=='ground' and image_counter % i.speed == 0 :

            if attacking_heros_in_game[heros_in_game.index(i)]==False :
                X0 = i.position[0]
                Y0 = i.position[1]
                X = X0
                Y = Y0
                if i.id == 1:
                    if i.position[1] > 420 :
                        if X > 300:
                            if X > 510 :
                                if abs(X - bridge_down_right_position[0]) < abs(Y - bridge_down_right_position[1]):
                                    if X > 520 or X < 500:
                                        X -= k
                                    try:
                                        Y -= abs((bridge_down_right_position[1] - i.position[1]) / (
                                                bridge_down_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5 :
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1 :
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X -= abs((bridge_down_right_position[0] - i.position[0]) / (
                                                bridge_down_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                            else:
                                if abs(X - bridge_down_right_position[0]) < abs(Y - bridge_down_right_position[1]):
                                    if X > 520 or X < 500:
                                        X += k
                                    try:
                                        Y -= abs((bridge_down_right_position[1] - i.position[1]) / (
                                                bridge_down_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5 :
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1 :
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X += abs((bridge_down_right_position[0] - i.position[0]) / (
                                                bridge_down_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1
                        elif X > 90:
                            if abs(X - bridge_down_left_position[0]) < abs(Y - bridge_down_left_position[1]):
                                if X > 100 or X < 80:
                                    X -= k
                                try:
                                    Y -= abs((bridge_down_left_position[1] - i.position[1]) / (
                                            bridge_down_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 - 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 - 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 - 1
                            else:
                                Y -= k
                                try:
                                    X -= abs((bridge_down_left_position[0] - i.position[0]) / (
                                            bridge_down_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 - 5
                                if abs(X - X0) > 5.5:
                                    X = X0 - 5
                                if abs(Y - Y0) < 1:
                                    X = X0 - 1
                        else:
                            if abs(X - bridge_down_left_position[0]) < abs(Y - bridge_down_left_position[1]):
                                if X > 100 or X < 80:
                                    X += k
                                try:
                                    Y -= abs((bridge_down_left_position[1] - i.position[1]) / (
                                            bridge_down_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 - 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 - 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 - 1

                            else:
                                Y -= k
                                try:
                                    X += abs((bridge_down_left_position[0] - i.position[0]) / (
                                            bridge_down_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1


                    else:
                        if X > 300 :
                            if X > 510:
                                if towers[1] not in destroyed_towers :
                                    if abs(X - QueenTower_up_right_position[0]) < abs(Y - QueenTower_up_right_position[1]) :
                                        if X > 520 or X < 500:
                                            X -= k
                                        try:
                                            Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                                    QueenTower_up_right_position[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 - 1
                                    else:
                                        Y -= k
                                        try:
                                            X -= abs((QueenTower_up_right_position[0] - i.position[0]) / (
                                                    QueenTower_up_right_position[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 - 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 - 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 - 1

                                else:
                                    if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                        if X > 310 or X < 290:
                                            X -= k
                                        try:
                                            Y -= abs((King_tower_up[1] - i.position[1]) / (
                                                    King_tower_up[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 - 1
                                    else:
                                        Y -= k
                                        try:
                                            X -= abs((King_tower_up[0] - i.position[0]) / (
                                                    King_tower_up[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 - 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 - 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 - 1
                            else:
                                if towers[1] not in destroyed_towers :
                                    if abs(X - QueenTower_up_right_position[0]) < abs(Y - QueenTower_up_right_position[1]):
                                        if X > 520 or X < 500:
                                            X += k
                                        try:
                                            Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                                    QueenTower_up_right_position[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 - 1
                                    else:
                                        Y -= k
                                        try:
                                            X += abs((QueenTower_up_right_position[0] - i.position[0]) / (
                                                    QueenTower_up_right_position[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 + 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 + 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 + 1
                                else:
                                    if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                        if X > 310 or X < 290:
                                            X -= k
                                        try:
                                            Y -= abs((King_tower_up[1] - i.position[1]) / (
                                                    King_tower_up[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 - 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 - 1
                                    else:
                                        Y -= k
                                        try:
                                            X -= abs((King_tower_up[0] - i.position[0]) / (
                                                    King_tower_up[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 - 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 - 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 - 1
                        elif X > 90:
                            if towers[0] not in destroyed_towers:
                                if abs(X - QueenTower_up_left_position[0]) < abs(Y - QueenTower_up_left_position[1]):
                                    if X > 100 or X < 80:
                                        X -= k
                                    try:
                                        Y -= abs((QueenTower_up_left_position[1] - i.position[1]) / (
                                                QueenTower_up_left_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X -= abs((QueenTower_up_left_position[0] - i.position[0]) / (
                                                QueenTower_up_left_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                            else:
                                if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                    if X > 310 or X < 290:
                                        X += k
                                    try:
                                        Y -= abs((King_tower_up[1] - i.position[1]) / (
                                                King_tower_up[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X += abs((King_tower_up[0] - i.position[0]) / (
                                                King_tower_up[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1

                        else:
                            if towers[0] not in destroyed_towers:
                                if abs(X - QueenTower_up_left_position[0]) < abs(Y - QueenTower_up_left_position[1]):
                                    if X > 100 or X < 80:
                                        X += k
                                    try:
                                        Y -= abs((QueenTower_up_left_position[1] - i.position[1]) / (
                                                QueenTower_up_left_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X += abs((QueenTower_up_left_position[0] - i.position[0]) / (
                                                QueenTower_up_left_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1
                            else:
                                if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                    if X > 310 or X < 290:
                                        X += k
                                    try:
                                        Y -= abs((King_tower_up[1] - i.position[1]) / (
                                                King_tower_up[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X += abs((King_tower_up[0] - i.position[0]) / (
                                                King_tower_up[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1

                    i.position = (X, Y)


                elif i.id == 2 :
                    X0 = i.position[0]
                    Y0 = i.position[1]
                    X = X0
                    Y = Y0
                    if i.position[1] < 380 :
                        if X > 300:
                            if X > 510 :
                                if abs(X - bridge_up_right_position[0]) < abs(Y - bridge_up_right_position[1]):
                                    if X > 520 or X < 500:
                                        X -= k
                                    try:
                                        Y += abs((bridge_up_right_position[1] - i.position[1]) / (
                                                bridge_up_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5 :
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1 :
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X -= abs((bridge_up_right_position[0] - i.position[0]) / (
                                                bridge_up_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                            else:
                                if abs(X - bridge_up_right_position[0]) < abs(Y - bridge_up_right_position[1]):
                                    if X > 520 or X < 500:
                                        X += k
                                    try:
                                        Y += abs((bridge_up_right_position[1] - i.position[1]) / (
                                                bridge_up_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5 :
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1 :
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X += abs((bridge_down_right_position[0] - i.position[0]) / (
                                                bridge_down_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1
                        elif X > 90:
                            if abs(X - bridge_up_left_position[0]) < abs(Y - bridge_up_left_position[1]):
                                if X > 100 or X < 80:
                                    X -= k
                                try:
                                    Y += abs((bridge_up_left_position[1] - i.position[1]) / (
                                            bridge_up_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 + 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 + 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 + 1
                            else:
                                Y += k
                                try:
                                    X -= abs((bridge_up_left_position[0] - i.position[0]) / (
                                            bridge_up_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 - 5
                                if abs(X - X0) > 5.5:
                                    X = X0 - 5
                                if abs(Y - Y0) < 1:
                                    X = X0 - 1
                        else:

                            if abs(X - bridge_up_left_position[0]) < abs(Y - bridge_up_left_position[1]):
                                if X > 100 or X < 80:
                                    X += k
                                try:
                                    Y += abs((bridge_up_left_position[1] - i.position[1]) / (
                                            bridge_up_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 + 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 + 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 + 1
                            else:
                                Y += k
                                try:
                                    X += abs((bridge_up_left_position[0] - i.position[0]) / (
                                            bridge_up_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1


                    else:
                        if X > 300 :
                            if X > 510:
                                if towers[3] not in destroyed_towers :
                                    if abs(X - QueenTower_down_right_position[0]) < abs(Y - QueenTower_down_right_position[1]) :
                                        if X > 520 or X < 500:
                                            X -= k
                                        try:
                                            Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                                    QueenTower_down_right_position[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 + 1
                                    else:
                                        Y += k
                                        try:
                                            X -= abs((QueenTower_down_right_position[0] - i.position[0]) / (
                                                    QueenTower_down_right_position[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 - 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 - 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 - 1

                                else:
                                    if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                        if X > 310 or X < 290:
                                            X -= k
                                        try:
                                            Y += abs((King_tower_up[1] - i.position[1]) / (
                                                    King_tower_up[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 + 1
                                    else:
                                        Y += k
                                        try:
                                            X -= abs((King_tower_up[0] - i.position[0]) / (
                                                    King_tower_up[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 - 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 - 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 - 1
                            else:
                                if towers[3] not in destroyed_towers :
                                    if abs(X - QueenTower_down_right_position[0]) < abs(Y - QueenTower_down_right_position[1]):
                                        if X > 520 or X < 500:
                                            X += k
                                        try:
                                            Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                                    QueenTower_down_right_position[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 + 1
                                    else:
                                        Y += k
                                        try:
                                            X += abs((QueenTower_down_right_position[0] - i.position[0]) / (
                                                    QueenTower_down_right_position[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 + 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 + 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 + 1
                                else:
                                    if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                        if X > 310 or X < 290:
                                            X -= k
                                        try:
                                            Y += abs((King_tower_down[1] - i.position[1]) / (
                                                    King_tower_down[0] - i.position[0])) * m
                                        except ZeroDivisionError:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) > 5.5:
                                            Y = Y0 + 5
                                        if abs(Y - Y0) < 1:
                                            Y = Y0 + 1
                                    else:
                                        Y += k
                                        try:
                                            X -= abs((King_tower_down[0] - i.position[0]) / (
                                                    King_tower_down[1] - i.position[1])) * m
                                        except ZeroDivisionError:
                                            X = X0 - 5
                                        if abs(X - X0) > 5.5:
                                            X = X0 - 5
                                        if abs(Y - Y0) < 1:
                                            X = X0 - 1
                        elif X > 90:
                            if towers[2] not in destroyed_towers:
                                if abs(X - QueenTower_down_left_position[0]) < abs(Y - QueenTower_down_left_position[1]):
                                    if X > 100 or X < 80:
                                        X -= k
                                    try:
                                        Y += abs((QueenTower_down_left_position[1] - i.position[1]) / (
                                                QueenTower_down_left_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X -= abs((QueenTower_down_left_position[0] - i.position[0]) / (
                                                QueenTower_down_left_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                            else:
                                if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                    if X > 310 or X < 290:
                                        X += k
                                    try:
                                        Y += abs((King_tower_down[1] - i.position[1]) / (
                                                King_tower_down[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X += abs((King_tower_down[0] - i.position[0]) / (
                                                King_tower_down[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1

                        else:
                            if towers[2] not in destroyed_towers:
                                if abs(X - QueenTower_down_left_position[0]) < abs(Y - QueenTower_down_left_position[1]):
                                    if X > 100 or X < 80:
                                        X += k
                                    try:
                                        Y += abs((QueenTower_down_left_position[1] - i.position[1]) / (
                                                QueenTower_down_left_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X += abs((QueenTower_down_left_position[0] - i.position[0]) / (
                                                QueenTower_down_left_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1
                            else:
                                if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                    if X > 310 or X < 290:
                                        X += k
                                    try:
                                        Y += abs((King_tower_down[1] - i.position[1]) / (
                                                King_tower_down[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X += abs((King_tower_down[0] - i.position[0]) / (
                                                King_tower_down[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1
                    i.position = (X, Y)

def move_up():
    #moving air troops
    global heros_in_game
    for i in heros_in_game:
        k = 1
        m = 1
        if i.type is "air" and  image_counter %i.speed==0:
            if attacking_heros_in_game[heros_in_game.index(i)]==False :
                X0 = i.position[0]
                Y0 = i.position[1]
                X = X0
                Y = Y0
                if i.id == 1:
                    if X > 300:
                        if X > 510:
                            if towers[1] not in destroyed_towers:
                                if abs(X - QueenTower_up_right_position[0]) < abs(Y - QueenTower_up_right_position[1]):
                                    if X > 520 or X < 500:
                                        X -= k
                                    try:
                                        Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                                QueenTower_up_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X -= abs((QueenTower_up_right_position[0] - i.position[0]) / (
                                                QueenTower_up_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1

                            else:
                                if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                    if X > 310 or X < 290:
                                        X -= k
                                    try:
                                        Y -= abs((King_tower_up[1] - i.position[1]) / (
                                                King_tower_up[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X -= abs((King_tower_up[0] - i.position[0]) / (
                                                King_tower_up[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                        else:
                            if towers[1] not in destroyed_towers:
                                if abs(X - QueenTower_up_right_position[0]) < abs(Y - QueenTower_up_right_position[1]):
                                    if X > 520 or X < 500:
                                        X += k
                                    try:
                                        Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                                QueenTower_up_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X += abs((QueenTower_up_right_position[0] - i.position[0]) / (
                                                QueenTower_up_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1
                            else:
                                if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                    if X > 310 or X < 290:
                                        X -= k
                                    try:
                                        Y -= abs((King_tower_up[1] - i.position[1]) / (
                                                King_tower_up[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 - 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 - 1
                                else:
                                    Y -= k
                                    try:
                                        X -= abs((King_tower_up[0] - i.position[0]) / (
                                                King_tower_up[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                    elif X > 90:
                        if towers[0] not in destroyed_towers:
                            if abs(X - QueenTower_up_left_position[0]) < abs(Y - QueenTower_up_left_position[1]):
                                if X > 100 or X < 80:
                                    X -= k
                                try:
                                    Y -= abs((QueenTower_up_left_position[1] - i.position[1]) / (
                                            QueenTower_up_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 - 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 - 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 - 1
                            else:
                                Y -= k
                                try:
                                    X -= abs((QueenTower_up_left_position[0] - i.position[0]) / (
                                            QueenTower_up_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 - 5
                                if abs(X - X0) > 5.5:
                                    X = X0 - 5
                                if abs(Y - Y0) < 1:
                                    X = X0 - 1
                        else:
                            if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                if X > 310 or X < 290:
                                    X += k
                                try:
                                    Y -= abs((King_tower_up[1] - i.position[1]) / (
                                            King_tower_up[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 - 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 - 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 - 1
                            else:
                                Y -= k
                                try:
                                    X += abs((King_tower_up[0] - i.position[0]) / (
                                            King_tower_up[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1

                    else:
                        if towers[0] not in destroyed_towers:
                            if abs(X - QueenTower_up_left_position[0]) < abs(Y - QueenTower_up_left_position[1]):
                                if X > 100 or X < 80:
                                    X += k
                                try:
                                    Y -= abs((QueenTower_up_left_position[1] - i.position[1]) / (
                                            QueenTower_up_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 - 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 - 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 - 1
                            else:
                                Y -= k
                                try:
                                    X += abs((QueenTower_up_left_position[0] - i.position[0]) / (
                                            QueenTower_up_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1
                        else:
                            if abs(X - King_tower_up[0]) < abs(Y - King_tower_up[1]):
                                if X > 310 or X < 290:
                                    X += k
                                try:
                                    Y -= abs((King_tower_up[1] - i.position[1]) / (
                                            King_tower_up[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 - 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 - 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 - 1
                            else:
                                Y -= k
                                try:
                                    X += abs((King_tower_up[0] - i.position[0]) / (
                                            King_tower_up[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1
                    i.position = (X, Y)

                elif i.id == 2 :
                    X0 = i.position[0]
                    Y0 = i.position[1]
                    X = X0
                    Y = Y0
                    if X > 300:
                        if X > 510:
                            if towers[3] not in destroyed_towers:
                                if abs(X - QueenTower_down_right_position[0]) < abs(
                                        Y - QueenTower_down_right_position[1]):
                                    if X > 520 or X < 500:
                                        X -= k
                                    try:
                                        Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                                QueenTower_down_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X -= abs((QueenTower_down_right_position[0] - i.position[0]) / (
                                                QueenTower_down_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1

                            else:
                                if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                    if X > 310 or X < 290:
                                        X -= k
                                    try:
                                        Y += abs((King_tower_up[1] - i.position[1]) / (
                                                King_tower_up[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X -= abs((King_tower_up[0] - i.position[0]) / (
                                                King_tower_up[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                        else:
                            if towers[3] not in destroyed_towers:
                                if abs(X - QueenTower_down_right_position[0]) < abs(
                                        Y - QueenTower_down_right_position[1]):
                                    if X > 520 or X < 500:
                                        X += k
                                    try:
                                        Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                                QueenTower_down_right_position[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X += abs((QueenTower_down_right_position[0] - i.position[0]) / (
                                                QueenTower_down_right_position[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 + 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 + 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 + 1
                            else:
                                if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                    if X > 310 or X < 290:
                                        X -= k
                                    try:
                                        Y += abs((King_tower_down[1] - i.position[1]) / (
                                                King_tower_down[0] - i.position[0])) * m
                                    except ZeroDivisionError:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) > 5.5:
                                        Y = Y0 + 5
                                    if abs(Y - Y0) < 1:
                                        Y = Y0 + 1
                                else:
                                    Y += k
                                    try:
                                        X -= abs((King_tower_down[0] - i.position[0]) / (
                                                King_tower_down[1] - i.position[1])) * m
                                    except ZeroDivisionError:
                                        X = X0 - 5
                                    if abs(X - X0) > 5.5:
                                        X = X0 - 5
                                    if abs(Y - Y0) < 1:
                                        X = X0 - 1
                    elif X > 90:
                        if towers[2] not in destroyed_towers:
                            if abs(X - QueenTower_down_left_position[0]) < abs(Y - QueenTower_down_left_position[1]):
                                if X > 100 or X < 80:
                                    X -= k
                                try:
                                    Y += abs((QueenTower_down_left_position[1] - i.position[1]) / (
                                            QueenTower_down_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 + 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 + 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 + 1
                            else:
                                Y += k
                                try:
                                    X -= abs((QueenTower_down_left_position[0] - i.position[0]) / (
                                            QueenTower_down_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 - 5
                                if abs(X - X0) > 5.5:
                                    X = X0 - 5
                                if abs(Y - Y0) < 1:
                                    X = X0 - 1
                        else:
                            if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                if X > 310 or X < 290:
                                    X += k
                                try:
                                    Y += abs((King_tower_down[1] - i.position[1]) / (
                                            King_tower_down[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 + 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 + 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 + 1
                            else:
                                Y += k
                                try:
                                    X += abs((King_tower_down[0] - i.position[0]) / (
                                            King_tower_down[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1

                    else:
                        if towers[2] not in destroyed_towers:
                            if abs(X - QueenTower_down_left_position[0]) < abs(Y - QueenTower_down_left_position[1]):
                                if X > 100 or X < 80:
                                    X += k
                                try:
                                    Y += abs((QueenTower_down_left_position[1] - i.position[1]) / (
                                            QueenTower_down_left_position[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 + 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 + 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 + 1
                            else:
                                Y += k
                                try:
                                    X += abs((QueenTower_down_left_position[0] - i.position[0]) / (
                                            QueenTower_down_left_position[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1
                        else:
                            if abs(X - King_tower_down[0]) < abs(Y - King_tower_down[1]):
                                if X > 310 or X < 290:
                                    X += k
                                try:
                                    Y += abs((King_tower_down[1] - i.position[1]) / (
                                            King_tower_down[0] - i.position[0])) * m
                                except ZeroDivisionError:
                                    Y = Y0 + 5
                                if abs(Y - Y0) > 5.5:
                                    Y = Y0 + 5
                                if abs(Y - Y0) < 1:
                                    Y = Y0 + 1
                            else:
                                Y += k
                                try:
                                    X += abs((King_tower_down[0] - i.position[0]) / (
                                            King_tower_down[1] - i.position[1])) * m
                                except ZeroDivisionError:
                                    X = X0 + 5
                                if abs(X - X0) > 5.5:
                                    X = X0 + 5
                                if abs(Y - Y0) < 1:
                                    X = X0 + 1
                i.position = (X, Y)



def show_heros_in_game (image_counter):
    ''' printing objects that are alive an exist in a special list'''
    for hero in heros_in_game :
        if attacking_heros_in_game[heros_in_game.index(hero)]==False :
            if hero.id==1 :
                if image_counter % (hero.speed *4)< hero.speed*2:
                    pos = (hero.position[0] - hero.move_image[0].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[0].get_size()[1] / 2)
                    window.blit(hero.move_image[0],pos)
                    pygame.draw.rect(window,(50,50,50),(hero.position[0] - hero.move_image[0].get_size()[0] /
                                                        2+50,hero.position[1] - hero.move_image[0].get_size()[1] / 2+40,50,7))
                    pygame.draw.rect(window,(50,50,200),(hero.position[0] - hero.move_image[0].get_size()[0] / 2+50,
                                                         hero.position[1] - hero.move_image[0].get_size()[1] / 2+40,(hero.hit_point/hero.max_health)*50,7))

                else :
                    pos = (hero.position[0] - hero.move_image[1].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[1].get_size()[1] / 2)
                    window.blit(hero.move_image[1],pos)
                    pygame.draw.rect(window, (50, 50, 50), (hero.position[0] - hero.move_image[0].get_size()[0] /
                                                            2 + 50, hero.position[1] - hero.move_image[0].get_size()[
                                                                1] / 2 + 40, 50, 7))
                    pygame.draw.rect(window, (50, 50, 200),
                                     (hero.position[0] - hero.move_image[0].get_size()[0] / 2 + 50,
                                      hero.position[1] - hero.move_image[0].get_size()[1] / 2 + 40,
                                      (hero.hit_point / hero.max_health) * 50, 7))


            if hero.id==2 :
                if image_counter % (hero.speed*4) < hero.speed*2:
                    pos = (hero.position[0] - hero.move_image[2].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[2].get_size()[1] / 2)
                    window.blit(hero.move_image[2],pos)
                    pygame.draw.rect(window, (50, 50, 50), (hero.position[0] - hero.move_image[0].get_size()[0] /
                                                            2 + 50, hero.position[1] - hero.move_image[0].get_size()[
                                                                1] / 2 + 40, 50, 7))
                    pygame.draw.rect(window, (200, 50, 50),
                                     (hero.position[0] - hero.move_image[0].get_size()[0] / 2 + 50,
                                      hero.position[1] - hero.move_image[0].get_size()[1] / 2 + 40,
                                      (hero.hit_point / hero.max_health) * 50, 7))
                else :
                    pos = (hero.position[0] - hero.move_image[3].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[3].get_size()[1] / 2)
                    window.blit(hero.move_image[3],pos)
                    pygame.draw.rect(window, (50, 50, 50), (hero.position[0] - hero.move_image[0].get_size()[0] /
                                                            2 + 50, hero.position[1] - hero.move_image[0].get_size()[
                                                                1] / 2 + 40, 50, 7))
                    pygame.draw.rect(window, (200, 50, 50),
                                     (hero.position[0] - hero.move_image[0].get_size()[0] / 2 + 50,
                                      hero.position[1] - hero.move_image[0].get_size()[1] / 2 + 40,
                                      (hero.hit_point / hero.max_health) * 50, 7))

        else :

            if hero.id==1 :
                if image_counter % (hero.hit_speed*16) < hero.hit_speed*8:
                    pos = (hero.position[0] - hero.move_image[0].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[0].get_size()[1] / 2)
                    window.blit(hero.attack_image[0],pos)
                    pygame.draw.rect(window, (50, 50, 50), (hero.position[0] - hero.move_image[0].get_size()[0] /
                                                            2 + 50, hero.position[1] - hero.move_image[0].get_size()[
                                                                1] / 2 + 40, 50, 7))
                    pygame.draw.rect(window, (50, 50, 200),
                                     (hero.position[0] - hero.move_image[0].get_size()[0] / 2 + 50,
                                      hero.position[1] - hero.move_image[0].get_size()[1] / 2 + 40,
                                      (hero.hit_point / hero.max_health) * 50, 7))
                else :
                    pos = (hero.position[0] - hero.move_image[1].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[1].get_size()[1] / 2)
                    window.blit(hero.attack_image[1],pos)
                    pygame.draw.rect(window, (50, 50, 50), (hero.position[0] - hero.move_image[0].get_size()[0] /
                                                            2 + 50, hero.position[1] - hero.move_image[0].get_size()[
                                                                1] / 2 + 40, 50, 7))
                    pygame.draw.rect(window, (50, 50, 200),
                                     (hero.position[0] - hero.move_image[0].get_size()[0] / 2 + 50,
                                      hero.position[1] - hero.move_image[0].get_size()[1] / 2 + 40,
                                      (hero.hit_point / hero.max_health) * 50, 7))
                window.blit(hero.weapon_image[0], (hero.weapon_image[1][0] - hero.weapon_image[0].get_size()[0] / 2,
                                                    hero.weapon_image[1][1] - hero.weapon_image[0].get_size()[1] / 2))

            if hero.id==2 :
                if image_counter % (16*hero.hit_speed) < 8*hero.hit_speed:
                    pos = (hero.position[0] - hero.move_image[2].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[2].get_size()[1] / 2)
                    window.blit(hero.attack_image[2],pos)
                    pygame.draw.rect(window, (50, 50, 50), (hero.position[0] - hero.move_image[0].get_size()[0] /
                                                            2 + 50, hero.position[1] - hero.move_image[0].get_size()[
                                                                1] / 2 + 40, 50, 7))
                    pygame.draw.rect(window, (200, 50, 50),
                                     (hero.position[0] - hero.move_image[0].get_size()[0] / 2 + 50,
                                      hero.position[1] - hero.move_image[0].get_size()[1] / 2 + 40,
                                      (hero.hit_point / hero.max_health) * 50, 7))
                else :
                    pos = (hero.position[0] - hero.move_image[3].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[3].get_size()[1] / 2)
                    window.blit(hero.attack_image[3],pos)
                    pygame.draw.rect(window, (50, 50, 50), (hero.position[0] - hero.move_image[0].get_size()[0] /
                                                            2 + 50, hero.position[1] - hero.move_image[0].get_size()[
                                                                1] / 2 + 40, 50, 7))
                    pygame.draw.rect(window, (200, 50, 50),
                                     (hero.position[0] - hero.move_image[0].get_size()[0] / 2 + 50,
                                      hero.position[1] - hero.move_image[0].get_size()[1] / 2 + 40,
                                      (hero.hit_point / hero.max_health) * 50, 7))
                window.blit(hero.weapon_image[0], (hero.weapon_image[1][0] - hero.weapon_image[0].get_size()[0] / 2,
                                                    hero.weapon_image[1][1] - hero.weapon_image[0].get_size()[1] / 2))


def fire() :
    '''function for heros to find enemy troops anf firing them'''
    global game_result
    for hero1 in heros_in_game :
        if image_counter % (hero1.hit_speed) == 0:
            shoot_result1=False
            for hero2 in heros_in_game :
                if shoot_result1==False :
                    if hero1.id != hero2.id :
                        if image_counter % 20 < 10:
                            x1=hero1.position[0]+hero1.attack_image[(hero1.id-1)*2].get_size()[0] / 2
                            y1=hero1.position[1]+hero1.attack_image[(hero1.id-1)*2].get_size()[1] / 2
                            x2=hero2.position[0]+hero2.attack_image[(hero1.id-1)*2].get_size()[0] / 2
                            y2=hero2.position[1]+hero2.attack_image[(hero1.id-1)*2].get_size()[1] / 2
                        else :
                            x1 = hero1.position[0] + hero1.attack_image[(hero1.id - 1) * 2+1].get_size()[0] / 2
                            y1 = hero1.position[1] + hero1.attack_image[(hero1.id - 1) * 2+1].get_size()[1] / 2
                            x2 = hero2.position[0] + hero2.attack_image[(hero1.id - 1) * 2+1].get_size()[0] / 2
                            y2 = hero2.position[1] + hero2.attack_image[(hero1.id - 1) * 2+1].get_size()[1] / 2

                        distance=((x1-x2)**2+(y1-y2)**2)**0.5
                        if distance/20<=hero1.range and (hero2.type in hero1.target) :
                            if attacking_heros_in_game[heros_in_game.index(hero1)]==False:
                                hero1.weapon_image[1] = hero1.position
                                attacking_heros_in_game[heros_in_game.index(hero1)]=True
                                target_heros_in_game[heros_in_game.index(hero2)].append(hero1)
                                shoot(hero2.position , hero1.weapon_image , hero1 , hero2)
                                shoot_result1=True
                                window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                            else:
                                attacking_heros_in_game[heros_in_game.index(hero1)] = True
                                target_heros_in_game[heros_in_game.index(hero2)].append(hero1)
                                shoot(hero2.position, hero1.weapon_image, hero1, hero2)
                                shoot_result1=True
                                window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                        else :
                            if attacking_heros_in_game[heros_in_game.index(hero1)]==True:
                                if hero1 in target_heros_in_game[heros_in_game.index(hero2)]:
                                    attacking_heros_in_game[heros_in_game.index(hero1)]= False
                                    del target_heros_in_game[heros_in_game.index(hero2)][target_heros_in_game[heros_in_game.index(hero2)].index(hero1)]

                else :
                    break
            shoot_result2=False
            for tower in towers_in_game :
                if shoot_result2==False :
                    if hero1.id != tower.id :
                        if image_counter % 20 < 10:
                            x1=hero1.position[0]+hero1.attack_image[(hero1.id-1)*2].get_size()[0] / 2
                            y1=hero1.position[1]+hero1.attack_image[(hero1.id-1)*2].get_size()[1] / 2
                            x2=tower.position[0]+tower.attack_image[(hero1.id-1)*2].get_size()[0] / 2
                            y2=tower.position[1]+tower.attack_image[(hero1.id-1)*2].get_size()[1] / 2
                        else :
                            x1 = hero1.position[0] + hero1.attack_image[(hero1.id - 1) * 2+1].get_size()[0] / 2
                            y1 = hero1.position[1] + hero1.attack_image[(hero1.id - 1) * 2+1].get_size()[1] / 2
                            x2 = tower.position[0] + tower.attack_image[(hero1.id - 1) * 2+1].get_size()[0] / 2
                            y2 = tower.position[1] + tower.attack_image[(hero1.id - 1) * 2+1].get_size()[1] / 2

                        distance=((x1-x2)**2+(y1-y2)**2)**0.5
                        if distance/20<=hero1.range and (tower.type in hero1.target) :
                            if attacking_heros_in_game[heros_in_game.index(hero1)]==False:
                                hero1.weapon_image[1] = hero1.position
                                attacking_heros_in_game[heros_in_game.index(hero1)]=True
                                target_towers_in_game[towers_in_game.index(tower)].append(hero1)
                                shoot(tower.position , hero1.weapon_image , hero1 , tower)
                                shoot_result2=True
                                window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,
                                                                    hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                            else:
                                attacking_heros_in_game[heros_in_game.index(hero1)] = True
                                target_towers_in_game[towers_in_game.index(tower)].append(hero1)
                                shoot(tower.position, hero1.weapon_image, hero1, tower)
                                shoot_result2=True
                                window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,
                                                                    hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                        else:
                            if attacking_heros_in_game[heros_in_game.index(hero1)] == True:
                                if hero1 in target_towers_in_game[towers_in_game.index(tower)]:
                                    attacking_heros_in_game[heros_in_game.index(hero1)] = False
                                    hero1.weapon_image[1] = hero1.position
                                    del target_towers_in_game[towers_in_game.index(tower)][target_towers_in_game[towers_in_game.index(tower)].index(hero1)]

                else :
                    break
    for tower in towers_in_game :
        if image_counter % (tower.id*4) == 0:
            shoot_result3=False
            for hero in heros_in_game :
                if shoot_result3==False :
                    if tower.id != hero.id :
                        if image_counter % 20 < 10:
                            x1=tower.position[0]+tower.attack_image[(tower.id-1)*2].get_size()[0] / 2
                            y1=tower.position[1]+tower.attack_image[(tower.id-1)*2].get_size()[1] / 2
                            x2=hero.position[0]+hero.attack_image[(tower.id-1)*2].get_size()[0] / 2
                            y2=hero.position[1]+hero.attack_image[(tower.id-1)*2].get_size()[1] / 2
                        else :
                            x1 = tower.position[0] + tower.attack_image[(tower.id - 1) * 2+1].get_size()[0] / 2
                            y1 = tower.position[1] + tower.attack_image[(tower.id - 1) * 2+1].get_size()[1] / 2
                            x2 = hero.position[0] + hero.attack_image[(tower.id - 1) * 2+1].get_size()[0] / 2
                            y2 = hero.position[1] + hero.attack_image[(tower.id - 1) * 2+1].get_size()[1] / 2

                        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                        if distance / 20 <= tower.range and (hero.type in tower.target):
                            if attacking_towers_in_game[towers_in_game.index(tower)] == False:
                                tower.weapon_image[1] = tower.position
                                attacking_towers_in_game[towers_in_game.index(tower)] = True
                                target_heros_in_game[heros_in_game.index(hero)].append(tower)
                                shoot2(hero.position, tower.weapon_image, tower, hero)
                                shoot_result3=True
                                window.blit(tower.weapon_image[0], (
                                tower.weapon_image[1][0] - tower.weapon_image[0].get_size()[0] / 2,
                                tower.weapon_image[1][1] - tower.weapon_image[0].get_size()[1] / 2))
                            else:
                                attacking_towers_in_game[towers_in_game.index(tower)] = True
                                target_heros_in_game[heros_in_game.index(hero)].append(tower)
                                shoot2(hero.position, tower.weapon_image, tower, hero)
                                shoot_result3=True
                                window.blit(tower.weapon_image[0], (
                                tower.weapon_image[1][0] - tower.weapon_image[0].get_size()[0] / 2,
                                tower.weapon_image[1][1] - tower.weapon_image[0].get_size()[1] / 2))
                        else:
                            if attacking_towers_in_game[towers_in_game.index(tower)] == True:
                                if tower in target_heros_in_game[heros_in_game.index(hero)]:
                                    attacking_towers_in_game[towers_in_game.index(tower)] = False
                                    tower.weapon_image[1]=tower.position
                                    del target_heros_in_game[heros_in_game.index(hero)][
                                        target_heros_in_game[heros_in_game.index(hero)].index(tower)]
                else :
                    break


    for hero in heros_in_game:
        if hero.hit_point <= 0 :
            k=heros_in_game.index(hero)
            for i in target_heros_in_game[k]:
                if i in heros_in_game :
                    attacking_heros_in_game[heros_in_game.index(i)]=False
                    heros_in_game[heros_in_game.index(i)].weapon_image[1]=heros_in_game[heros_in_game.index(i)].position
                if i in towers_in_game :
                    attacking_towers_in_game[towers_in_game.index(i)]=False
                    towers_in_game[towers_in_game.index(i)].weapon_image[1]=towers_in_game[towers_in_game.index(i)].position
            del heros_in_game[k]
            del attacking_heros_in_game[k]
            del target_heros_in_game[k]
    for tower in towers_in_game :
        if tower.hit_point <= 0 :
            k=towers_in_game.index(tower)
            for i in target_towers_in_game[k]:
                if i in heros_in_game :
                    attacking_heros_in_game[heros_in_game.index(i)]=False
                    heros_in_game[heros_in_game.index(i)].weapon_image[1]=heros_in_game[heros_in_game.index(i)].position
            destroyed_towers.append(towers_in_game[k])
            if towers_in_game[k].id==2:
                game_result[0]+=1
            else :
                game_result[1]+=1
            if towers[4] in destroyed_towers:
                game_result[0] = 3
            if towers[5] in destroyed_towers:
                game_result[1] = 3
            del towers_in_game[k]
            del attacking_towers_in_game[k]
            del target_towers_in_game[k]

def area_damage():
    ''' area damage make it possible to fire a group of enemy heros that are in an certain area'''
    for hero1 in heros_in_game :
        if hero1.area_damage != False:
            for hero2 in heros_in_game :
                if hero1.id != hero2.id :
                    x = hero1.position[0]
                    y = hero1.position[1]
                    x1 = hero2.position[0]
                    y1 = hero2.position[1]
                    distance = ((x - x1)**2 + (y-y1)**2)**0.5
                    if distance / 20 <= hero1.range and (hero2.type in hero1.target):
                        hero2.hit_point -= hero1.damage/2
            for tower in towers_in_game :
                if hero1.id != tower.id :
                    x = hero1.position[0]
                    y = hero1.position[1]
                    x1 = tower.position[0]
                    y1 = tower.position[1]
                    distance = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
                    if distance / 20 <= hero1.range :
                        tower.hit_point -= hero1.damage/2

def hoosh():
    ''' artificial intelligence of the game'''
    global heros_in_use,attacking_heros_in_game,heros_in_game,target_heros_in_game,last_card,last_card_check,elixirs_teem2
    long_range_troops = ["Wizard","Mega_minion"]
    enemy_number = 0
    for i in heros_in_game:
        if i.id == 1:
            enemy_number += 1

    rand_x1 = random.randint(50, 170)
    rand_y = random.randint(200, 350)
    rand_x2 = random.randint(400, 550)
    if enemy_number == 0:
        if len(heros_in_game) != 0:
            for hero in heros_in_game :
                if type(hero) in [type(Giant((0,0),2)),type(Balloon((0,0),2)),type(Knight((0,0),2))] :
                    for hero1 in [Archer((hero.position[0],320),2),Wizard((hero.position[0],320),2),Mega_minion((hero.position[0],320),2)]:
                        if type(hero1) in heros_in_use2 and hero1.hero_cost <= elixirs_teem2 :
                            if elixirs_teem2 - hero1.hero_cost >= 0 :
                                heros_in_game.append(hero1)
                                attacking_heros_in_game.append(False)
                                target_heros_in_game.append([])
                                elixirs_teem2-=hero1.hero_cost

                if type(hero) in [type(Wizard((0,0),2)),type(Archer((0,0),2)),type(Mega_minion((0,0),2))] :
                    for hero1 in [Giant((hero.position[0],320),2),Balloon((hero.position[0],320),2),Pekka((hero.position[0],320),2),Knight((hero.position[0],320),2)]:
                        if type(hero1) in heros_in_use2 and hero1.hero_cost <= elixirs_teem2 :
                            if elixirs_teem2 - hero1.hero_cost >= 0:
                                heros_in_game.append(hero1)
                                attacking_heros_in_game.append(False)
                                target_heros_in_game.append([])
                                elixirs_teem2-=hero1.hero_cost

        elif elixirs_teem2==8 :
            for hero in [Mega_minion((random.choice([rand_x1,rand_x2]),rand_y),2),Archer((random.choice([rand_x1,rand_x2]),rand_y),2)]:
                if  type(hero) in heros_in_use2 :
                    if elixirs_teem2 - hero.hero_cost >= 0:
                        heros_in_game.append(hero)
                        attacking_heros_in_game.append(False)
                        target_heros_in_game.append([])
                        elixirs_teem2 -= hero.hero_cost
                        break


    elif last_card in heros_in_game and  last_card_check == False:
        if elixirs_teem2 >4 :
            for i in heros_in_use :
                hero=eval(i+'((0,0),2)')
                if hero.type not in last_card.target and last_card.type in hero.target :
                    if hero.hero_cost <= elixirs_teem2 :
                        if elixirs_teem2 - hero.hero_cost >= 0:
                            elixirs_teem2-=hero.hero_cost
                            last_card_check=True
                            if last_card.position[0]<300 :
                                heros_in_game.append(eval(i+'('+str((rand_x1,rand_y))+',2)'))
                                attacking_heros_in_game.append(False)
                                target_heros_in_game.append([])
                            else:
                                heros_in_game.append(eval(i+'('+str((rand_x2,rand_y))+',2)'))
                                attacking_heros_in_game.append(False)
                                target_heros_in_game.append([])
                            return None
            for i in heros_in_use :
                hero=eval(i+'((0,0),2)')
                if last_card.target==("building") :
                    if hero.type=="building" :
                        if elixirs_teem2 - hero.hero_cost >= 0:
                            elixirs_teem2 -= hero.hero_cost
                            last_card_check = True
                            if last_card.position[0] < 300:
                                heros_in_game.append(eval(i +'('+ str((rand_x1, rand_y))+',2)'))
                                attacking_heros_in_game.append(False)
                                target_heros_in_game.append([])
                            else:
                                heros_in_game.append(eval(i +'('+ str((rand_x2, rand_y))+',2)'))
                                attacking_heros_in_game.append(False)
                                target_heros_in_game.append([])
                            return None
                elif  hero.target==("ground","building","air") and image_counter%100==0:
                    if elixirs_teem2 - hero.hero_cost >= 0:
                        elixirs_teem2 -= hero.hero_cost
                        last_card_check = True
                        if last_card.position[0] < 300:
                            heros_in_game.append(eval(i +'('+ str((rand_x1, rand_y))+',2)'))
                            attacking_heros_in_game.append(False)
                            target_heros_in_game.append([])
                        else:
                            heros_in_game.append(eval(i +'('+ str((rand_x2, rand_y))+',2)'))
                            attacking_heros_in_game.append(False)
                            target_heros_in_game.append([])
                        return None
                elif type(last_card)==type(hero) :
                    if elixirs_teem2 - hero.hero_cost >= 0:
                        elixirs_teem2 -= hero.hero_cost
                        last_card_check = True
                        if last_card.position[0] < 300:
                            heros_in_game.append(eval(i + '(' + str((rand_x1, rand_y)) + ',2)'))
                            attacking_heros_in_game.append(False)
                            target_heros_in_game.append([])
                        else:
                            heros_in_game.append(eval(i + '(' + str((rand_x2, rand_y)) + ',2)'))
                            attacking_heros_in_game.append(False)
                            target_heros_in_game.append([])
                        return None



def hooshang () :
    '''part 2 of hoosh !!!'''
    global heros_in_use, attacking_heros_in_game, heros_in_game, target_heros_in_game, last_card_check, elixirs_teem2
    long_range_troops = ["Wizard", "Mega_minion"]
    enemy_number = 0
    for i in heros_in_game:
        if i.id == 1:
            enemy_number += 1

    rand_x1 = random.randint(50, 170)
    rand_y = random.randint(170, 250)
    rand_x2 = random.randint(400, 550)

    if enemy_number > 0 :
        for last_card in heros_in_game :
            if last_card.id == 1 and last_card.position[1] < 369 :
                if elixirs_teem2 > 4:
                    for i in heros_in_use:
                        hero = eval(i + '((0,0),2)')
                        if hero.type not in last_card.target and last_card.type in hero.target:
                            if hero.hero_cost <= elixirs_teem2:
                                if elixirs_teem2 - hero.hero_cost >= 0:
                                    elixirs_teem2 -= hero.hero_cost
                                    last_card_check = True
                                    if last_card.position[0] < 300:
                                        heros_in_game.append(eval(i + '(' + str((rand_x1, rand_y)) + ',2)'))
                                        attacking_heros_in_game.append(False)
                                        target_heros_in_game.append([])
                                    else:
                                        heros_in_game.append(eval(i + '(' + str((rand_x2, rand_y)) + ',2)'))
                                        attacking_heros_in_game.append(False)
                                        target_heros_in_game.append([])
                                    return None
                    for i in heros_in_use:
                        hero = eval(i + '((0,0),2)')
                        if last_card.target == ("building"):
                            if hero.type == "building":
                                if elixirs_teem2 - hero.hero_cost >= 0:
                                    elixirs_teem2 -= hero.hero_cost
                                    last_card_check = True
                                    if last_card.position[0] < 300:
                                        heros_in_game.append(eval(i + '(' + str((rand_x1, rand_y)) + ',2)'))
                                        attacking_heros_in_game.append(False)
                                        target_heros_in_game.append([])
                                    else:
                                        heros_in_game.append(eval(i + '(' + str((rand_x2, rand_y)) + ',2)'))
                                        attacking_heros_in_game.append(False)
                                        target_heros_in_game.append([])
                                    return None
                        elif hero.type == "building" and image_counter%200==0:
                            if elixirs_teem2 - hero.hero_cost >= 0:
                                elixirs_teem2 -= hero.hero_cost
                                last_card_check = True
                                if last_card.position[0] < 300:
                                    heros_in_game.append(eval(i + '(' + str((rand_x1, rand_y)) + ',2)'))
                                    attacking_heros_in_game.append(False)
                                    target_heros_in_game.append([])
                                else:
                                    heros_in_game.append(eval(i + '(' + str((rand_x2, rand_y)) + ',2)'))
                                    attacking_heros_in_game.append(False)
                                    target_heros_in_game.append([])
                                return None
                        elif type(last_card) == type(hero):
                            if elixirs_teem2 - hero.hero_cost >= 0:
                                elixirs_teem2 -= hero.hero_cost
                                last_card_check = True
                                if last_card.position[0] < 300:
                                    heros_in_game.append(eval(i + '(' + str((rand_x1, rand_y)) + ',2)'))
                                    attacking_heros_in_game.append(False)
                                    target_heros_in_game.append([])
                                else:
                                    heros_in_game.append(eval(i + '(' + str((rand_x2, rand_y)) + ',2)'))
                                    attacking_heros_in_game.append(False)
                                    target_heros_in_game.append([])
                                return None



def InTesla () :
    #decrease tesla and inferno hit point
    for tower in heros_in_game :
        if tower.type == "building" :
            tower.hit_point -= 1

def shoot2(target_position , weapon_image , tower , hero):
    '''movint troops bolet'''

    if target_position[0] - 15 < weapon_image[1][0]  and target_position[0] +15 > weapon_image[1][0] :
        if target_position[1] -20 < weapon_image[1][1]  and target_position[1] +20 > weapon_image[1][1]  :
            hero.hit_point -= tower.damage
            attacking_towers_in_game[towers_in_game.index(tower)] = False
            weapon_image[1] = tower.position
    x1 = weapon_image[1][0]
    y1 = weapon_image[1][1]
    a = 5
    b = 10
    t = 10
    if x1 > target_position[0]:
        if y1 > target_position[1]:
            if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
                if x1 < target_position[0] + a and x1 > target_position[0] - a:
                    x1 -= a
                else:
                    x1 -= a
                try:
                    y1 -= abs((target_position[1] - y1) / (target_position[0] - x1)) * t
                except:
                    y1 = weapon_image[1][1] - b
                if abs(weapon_image[1][1] - y1) > b:
                    y1 = weapon_image[1][1] - b
                if abs(weapon_image[1][1] - y1) < 1:
                    y1 = weapon_image[1][1] - 1
            else:
                if y1 < target_position[1] + a and y1 > target_position[1] - a:
                    y1 -= a
                else:
                    y1 -= a
                try:
                    x1 -= abs((target_position[0] - x1) / (target_position[1] - y1)) * t
                except:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) > b:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) < 1:
                    x1 = weapon_image[1][0] - 1

        else:
            if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
                if x1 < target_position[0] + a and x1 > target_position[0] - a:
                    x1 -= a
                else:
                    x1 -= a
                try:
                    y1 += abs((target_position[1] - y1) / (target_position[0] - x1)) * t
                except:
                    y1 = weapon_image[1][1] + b
                if abs(weapon_image[1][1] - y1) > b:
                    y1 = weapon_image[1][1] + b
                if abs(weapon_image[1][1] - y1) < 1:
                    y1 = weapon_image[1][1] + 1
            else:
                if y1 < target_position[1] + a and y1 > target_position[1] - a:
                    y1 += a
                else:
                    y1 += a
                try:
                    x1 -= abs((target_position[0] - x1) / (target_position[1] - y1)) * t
                except:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) > b:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) < 1:
                    x1 = weapon_image[1][0] - 1

    elif y1 < target_position[1]:
        if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
            if x1 < target_position[0] + a and x1 > target_position[0] - a:
                x1 += a
            else:
                x1 += a
            try:
                y1 += abs((target_position[1] - y1) / (target_position[0] - x1)) * t
            except:
                y1 = weapon_image[1][1] + b
            if abs(weapon_image[1][1] - y1) > b:
                y1 = weapon_image[1][1] + b
            if abs(weapon_image[1][1] - y1) < 1:
                y1 = weapon_image[1][1] + 1
        else:
            if y1 < target_position[1] + a and y1 > target_position[1] - a:
                y1 += a
            else:
                y1 += a
            try:
                x1 += abs((target_position[0] - x1) / (target_position[1] - y1)) * t
            except:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) > b:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) < 1:
                x1 = weapon_image[1][0] + 1

    else:
        if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
            if x1 < target_position[0] + a and x1 > target_position[0] - a:
                x1 += a
            else:
                x1 += a
            try:
                y1 -= abs((target_position[1] - y1) / (target_position[0] - x1)) * t
            except:
                y1 = weapon_image[1][1] - b
            if abs(weapon_image[1][1] - y1) > b:
                y1 = weapon_image[1][1] - b
            if abs(weapon_image[1][1] - y1) < 1:
                y1 = weapon_image[1][1] - 1
        else:
            if y1 < target_position[1] + a and y1 > target_position[1] - a:
                y1 -= a
            else:
                y1 -= a
            try:
                x1 += abs((target_position[0] - x1) / (target_position[1] - y1)) * t
            except:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) > b:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) < 1:
                x1 = weapon_image[1][0] + 1
    weapon_image[1] = (x1, y1)


def shoot(target_position , weapon_image , hero1 , hero2):
    if target_position[0] - 15 < weapon_image[1][0]  and target_position[0] +15 > weapon_image[1][0] :
        if target_position[1] -20 < weapon_image[1][1]  and target_position[1] +20 > weapon_image[1][1]  :
            hero2.hit_point -= hero1.damage
            attacking_heros_in_game[heros_in_game.index(hero1)] = False
            weapon_image[1] = hero1.position
            area_damage()

    x1 = weapon_image[1][0]
    y1 = weapon_image[1][1]
    a = 5
    b= 10
    t = 10
    if x1 > target_position[0]:
        if y1 > target_position[1] :
            if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
                if x1 < target_position[0] + a and x1 > target_position[0] - a:
                    x1 -= a
                else:
                    x1 -= a
                try :
                    y1 -= abs((target_position[1] - y1) / (target_position[0] - x1))*t
                except :
                    y1 = weapon_image[1][1] - b
                if abs(weapon_image[1][1] - y1) > b :
                    y1 = weapon_image[1][1] - b
                if abs(weapon_image[1][1] - y1) < 1 :
                    y1 = weapon_image[1][1] - 1
            else :
                if y1 < target_position[1] + a and y1 > target_position[1] - a:
                    y1 -= a
                else:
                    y1 -= a
                try:
                    x1 -= abs((target_position[0] - x1) / (target_position[1] - y1)) * t
                except:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) > b:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) < 1:
                    x1 = weapon_image[1][0] - 1

        else:
            if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
                if x1 < target_position[0] + a and x1 > target_position[0] - a:
                    x1 -= a
                else:
                    x1 -= a
                try :
                    y1 += abs((target_position[1] - y1) / (target_position[0] - x1))*t
                except :
                    y1 = weapon_image[1][1] + b
                if abs(weapon_image[1][1] - y1) > b :
                    y1 = weapon_image[1][1] + b
                if abs(weapon_image[1][1] - y1) < 1 :
                    y1 = weapon_image[1][1] + 1
            else :
                if y1 < target_position[1] + a and y1 > target_position[1] - a:
                    y1 += a
                else:
                    y1 += a
                try:
                    x1 -= abs((target_position[0] - x1) / (target_position[1] - y1)) * t
                except:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) > b:
                    x1 = weapon_image[1][0] - b
                if abs(weapon_image[1][0] - x1) < 1:
                    x1 = weapon_image[1][0] - 1

    elif y1 < target_position[1] :
        if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
            if x1 < target_position[0] + a and x1 > target_position[0] - a:
                x1 += a
            else:
                x1 += a
            try:
                y1 += abs((target_position[1] - y1) / (target_position[0] - x1)) * t
            except:
                y1 = weapon_image[1][1] + b
            if abs(weapon_image[1][1] - y1) > b:
                y1 = weapon_image[1][1] + b
            if abs(weapon_image[1][1] - y1) < 1:
                y1 = weapon_image[1][1] + 1
        else:
            if y1 < target_position[1] + a and y1 > target_position[1] - a:
                y1 += a
            else:
                y1 += a
            try:
                x1 += abs((target_position[0] - x1) / (target_position[1] - y1)) * t
            except:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) > b:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) < 1:
                x1 = weapon_image[1][0] + 1

    else :
        if abs(weapon_image[1][0] - x1) < abs(target_position[1] - y1):
            if x1 < target_position[0] + a and x1 > target_position[0] - a:
                x1 += a
            else:
                x1 += a
            try:
                y1 -= abs((target_position[1] - y1) / (target_position[0] - x1)) * t
            except:
                y1 = weapon_image[1][1] - b
            if abs(weapon_image[1][1] - y1) > b:
                y1 = weapon_image[1][1] - b
            if abs(weapon_image[1][1] - y1) < 1:
                y1 = weapon_image[1][1] - 1
        else:
            if y1 < target_position[1] + a and y1 > target_position[1] - a:
                y1 -= a
            else:
                y1 -= a
            try:
                x1 += abs((target_position[0] - x1) / (target_position[1] - y1)) * t
            except:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) > b:
                x1 = weapon_image[1][0] + b
            if abs(weapon_image[1][0] - x1) < 1:
                x1 = weapon_image[1][0] + 1
    weapon_image[1] = (x1 , y1)




def show_towers():
    for i in towers_in_game :
        window.blit(i.image[1],(i.position[0]-i.image[1].get_size()[0]/2,i.position[1]-i.image[1].get_size()[1]/2))
        window.blit(i.weapon_image[0], (
            i.weapon_image[1][0] - i.weapon_image[0].get_size()[0] / 2,
            i.weapon_image[1][1] - i.weapon_image[0].get_size()[1] / 2))
        if i.id == 1 :
            pygame.draw.rect(window, (50, 50, 50), (i.position[0] - i.image[0].get_size()[0] /
                                                    2 + 50, i.position[1] - i.image[0].get_size()[1] / 2 ,
                                                    60, 7))
            pygame.draw.rect(window, (50, 50, 200), (i.position[0] - i.image[0].get_size()[0] / 2 + 50,
                                                     i.position[1] - i.image[0].get_size()[1] / 2 ,
                                                     (i.hit_point / i.max_health) * 60, 7))
        else :
            pygame.draw.rect(window, (50, 50, 50), (i.position[0] - i.image[0].get_size()[0] /
                                                    2 + 50, i.position[1] - i.image[0].get_size()[1] / 2,
                                                    60, 7))
            pygame.draw.rect(window, (200, 50, 50), (i.position[0] - i.image[0].get_size()[0] / 2 + 50,
                                                     i.position[1] - i.image[0].get_size()[1] / 2,
                                                     (i.hit_point / i.max_health) * 60, 7))
    for i in destroyed_towers :
        window.blit(i.destroyed_image,(i.position[0]-i.destroyed_image.get_size()[0]/2,i.position[1]-i.destroyed_image.get_size()[1]/2))


def show_time():
    font = pygame.font.SysFont("comicsansms", 32)
    if GAME_TIME.get_ticks() <= 3*60*1000 :
        game_time=str(2-GAME_TIME.get_ticks()//1000//60)+':'+str(60-GAME_TIME.get_ticks()//1000%60)
        text = font.render(game_time, True, (255, 255, 255))
        window.blit(text,(650 - text.get_width() // 2, 50 - text.get_height() // 2))
    elif GAME_TIME.get_ticks() <= 4*60*1000:
        game_time = str(3 - GAME_TIME.get_ticks() // 1000 // 60) + ':' + str(60 - GAME_TIME.get_ticks() // 1000 % 60)
        text = font.render(game_time, True, (255, 255, 255))
        window.blit(text, (650 - text.get_width() // 2, 50 - text.get_height() // 2))

def show_elixir():
    global elixirs_teem1, elixirs_teem2, last_elixir_given_time
    if GAME_TIME.get_ticks() - last_elixir_given_time >= elixir_reload_time * 1000:
        if elixirs_teem1 < 8:
            elixirs_teem1 += 1
        if elixirs_teem2 < 8:
            elixirs_teem2 += 1
        last_elixir_given_time = GAME_TIME.get_ticks()
    if elixirs_teem1 <= 8:
        window.blit(pygame.image.load('images\limo\\' + str(elixirs_teem1) + '.png'), (610, 100))
    else:
        window.blit(pygame.image.load('images\limo\8.png'), (610, 100))

    font = pygame.font.SysFont("comicsansms", 32)
    text1 = font.render(str(elixirs_teem1), True, (150, 0, 150))
    window.blit(text1, (612 - text1.get_width() // 2, 148 - text1.get_height() // 2))

def show_forbidden_area():
    ''' forbiden area that you cant drop cards in there if there is enemy tower'''
    if card_selected[0]==True :
        if towers[0] not in destroyed_towers :
            window.blit(red_image,(0,0))
        else:
            window.blit(red_image, (0, -125))
        if towers[1] not in destroyed_towers :
            window.blit(red_image,(red_image.get_size()[0],0))
        else :
            window.blit(red_image, (red_image.get_size()[0], -125))

def game_controler():
    '''a function to check if the game is over or not'''
    global end_game,game_result_before_extra_time
    if game_result[0]>=3 or game_result[1]>=3 :
        end_game=True
    if GAME_TIME.get_ticks()==3*60*1000:
        if game_result[0]!=game_result[1]:
            end_game=True
    if GAME_TIME.get_ticks()>3*60*1000:
        if game_result[0]!=game_result[1]:
            end_game=True
    if GAME_TIME.get_ticks()>=4*60*1000:
        end_game=True


def show_crowns():
    window.blit(pygame.image.load('images/red_crown.png'), (635, 200))
    window.blit(pygame.image.load('images/blue_crown.png'), (640, 250))
    font = pygame.font.SysFont("comicsansms", 32)
    text1 = font.render(str(game_result[0]), True, (0, 0, 255))
    text2=font.render(str(game_result[1]),True,(255,0,0))
    window.blit(text1, (620 - text1.get_width() // 2, 275 - text1.get_height() // 2))
    window.blit(text2, (620 - text2.get_width() // 2, 225 - text2.get_height() // 2))




def start_menu():
    global card_selected1,value,value_position,dictroop,dictroop1
    for i in range(len(value)):
        window.blit(value[i], value_position[i])
    if pygame.mouse.get_pressed()[0] == True:
        for i in range(len(value_position)):
            if value_position[i][0] <= pygame.mouse.get_pos()[0] <= value_position[i][0] + \
                    value[i].get_size()[0] \
                    and value_position[i][1] <= pygame.mouse.get_pos()[1] <= value_position[i][1] + \
                    value[i].get_size()[1] and card_selected1[0] == False:
                card_selected1[0] = True
                card_selected1[1] = i
            if card_selected1[0] == True and card_selected1[1] == i:
                mouse_pos = pygame.mouse.get_pos()
                card_size = value[i].get_size()
                if mouse_pos[0] < card_size[0] / 2:
                    if mouse_pos[1] < card_size[1] / 2:
                        value_position[i] = (0, 0)
                    elif mouse_pos[1] > window_height - card_size[1] / 2:
                        value_position[i] = (0, window_height - card_size[1])
                    else:
                        value_position[i] = (0, mouse_pos[1] - card_size[1] / 2)
                elif mouse_pos[0] > window_width - card_size[0] / 2:
                    if mouse_pos[1] < card_size[1] / 2:
                        value_position[i] = (window_width - card_size[0], 0)
                    elif mouse_pos[1] > window_height - card_size[1] / 2:
                        value_position[i] = (window_width - card_size[0], window_height - card_size[1])
                    else:
                        value_position[i] = (window_width - card_size[0], mouse_pos[1] - card_size[1] / 2)
                elif mouse_pos[1] < card_size[1] / 2:
                    value_position[i] = (mouse_pos[0] - card_size[0] / 2, 0)
                elif mouse_pos[1] > window_height - card_size[1] / 2:
                    value_position[i] = (mouse_pos[0] - card_size[0] / 2, window_height - card_size[1])
                else:
                    value_position[i] = (pygame.mouse.get_pos()[0] - (value[i].get_size()[0] / 2),
                                             pygame.mouse.get_pos()[1] - (value[i].get_size()[1] / 2))
    elif card_selected1[0] == True:
        i=card_selected1[1]
        if 150<value_position[i][0]<550 and 360<value_position[i][1]<550 :
            dictroop[list(dictroop1.keys())[i]]=value[i]
            card_selected1[0] = False
        else :
            card_selected1[0]=False
            value_position[i]=value_position2[i]

menu_sound_play=False
menu_sound_play_counter=0
battle_sound_play_counter=0

def game_sound():
    global menu_sound_play,menu_sound_play_counter,battle_sound_play_counter
    if start_game==False and menu_sound_play_counter==0 :
        menu_sound.play(-1)
        menu_sound_play_counter+=1
        menu_sound_play=False
    if start_game==True and battle_sound_play_counter==0:
        if menu_sound_play==False :
            pygame.mixer.stop()
            menu_sound_play=True
        battle_sound.play(-1)
        battle_sound_play_counter+=1




def quit_game():
    pygame.quit()
    sys.exit()
#picture and sounds
pygame.mixer.init()
menu_sound=pygame.mixer.Sound('sounds/menu.ogg')
menu_sound.set_volume(1)
battle_sound=pygame.mixer.Sound('sounds/battle.ogg')
battle_sound.set_volume(1)

map_picture = None
Tesla_card = pygame.image.load('images/TeslaCard.png')
Inferno_card = pygame.image.load('images/InfernoCard.png')
red_image=pygame.image.load('images/red.png')
archer_card=pygame.image.load('images/ArcherCard.png')
wizard_card=pygame.image.load('images/WizardCard.png')
giant_card=pygame.image.load('images/GiantCard.png')
balloon_card=pygame.image.load('images/BalloonCard.png')
knight_card=pygame.image.load('images/KnightCard.png')
pekka_card=pygame.image.load('images/MiniPEKKACard.png')
mega_minion_card=pygame.image.load('images/MegaMinionCard.png')
#variables
last_card=None
last_card_check=False
card_selected1=[False,0]
start_game=False
end_game=False
game_result=[0,0]
game_result_before_extra_time=None
last_elixir_given_time=0
if GAME_TIME.get_ticks() <= 3 * 60 * 1000 :
    elixir_reload_time = 2
else :
    elixir_reload_time = 1.5
elixirs_teem1=3
elixirs_teem2=3
dictroop1 = {"Archer" :archer_card  , "Wizard" : wizard_card , "Giant" : giant_card
    , "Knight" : knight_card , "Mega_minion" : mega_minion_card , "Pekka" : pekka_card , "Balloon" : balloon_card , "Inferno" : Inferno_card , "Tesla" : Tesla_card}
dictroop={}
temp_troop = list(dictroop1.keys())
heros_in_use=[]
heros_in_use2=[]
for i in range(6):
    card = random.choice(temp_troop)
    heros_in_use.append(card)
    temp_troop.remove(card)
for i in heros_in_use :
    heros_in_use2.append(type(eval(i+'((0,0),2)')))

card_selected=[False,0]
heros_in_game=[]
attacking_heros_in_game=[]
target_heros_in_game=[]
towers_in_game=[Princess_tower((10+75,20+75),2,pygame.image.load('images\Queen_tower_up.png')),Princess_tower((430+75,20+75),2,pygame.image.load('images\Queen_tower_up.png')),
                Princess_tower((10+75, 650+75), 1, pygame.image.load('images\Queen_tower_down.png')),Princess_tower((430+75,650+75),1,pygame.image.load('images\Queen_tower_down.png')),
                King_tower((225+75,0+75),2,pygame.image.load('images\King_tower_up.png')),King_tower((225+75,650+75),1,pygame.image.load('images\King_tower_down.png'))]
value=list(dictroop1.values())
value_position=[]
for i in range(7):
    value_position.append(( value[i].get_size()[0] * i + 9*i ,60))
for i in range(7, len(value)):
    j = i - 7
    value_position.append(( value[i].get_size()[0] * j + 9*j ,value[i].get_size()[1]+60))
value_position2=value_position[:]


towers = towers_in_game[:]
attacking_towers_in_game=[False,False,False,False,False,False]
target_towers_in_game=[[],[],[],[],[],[]]
destroyed_towers=[]
trooplist = []
trooplist_position=[]
trooplist_name=[]
window_width=700
window_height = 800


bridge_up_left_position = (90 , 380)
bridge_down_left_position = (90 , 420)
bridge_up_right_position = (510 , 380)
bridge_down_right_position = (510 , 420)

QueenTower_up_left_position = (90 , 85)
QueenTower_up_right_position = (510 , 85)
QueenTower_down_left_position = (90 , 700)
QueenTower_down_right_position = (510 , 700)

King_tower_up = (300 , 75)
King_tower_down = (300 , 725)

#main()
pygame.init()
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Clash Royale')
image_counter=0

while True :
    game_sound()
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN :
            if event.key==pygame.K_1 and start_game==False  :
                map_picture = pygame.image.load('images/field_2.jpg')
            if event.key==pygame.K_2 and start_game==False :
                map_picture = pygame.image.load('images/field_1.jpg')
            if event.key==pygame.K_3 and start_game==False :
                map_picture = pygame.image.load('images/field_3.jpg')
            if event.key == pygame .K_SPACE and len(dictroop)>5 and map_picture!=None :
                start_game = True
        if event.type == GAME_GLOBALS.QUIT:
            quit_game()
    if start_game==False :
        window.blit(pygame.image.load('images/menu.png'),(0,0))
        start_menu()
    elif end_game==False and start_game==True :
        draw_map()
        show_forbidden_area()
        image_counter+=1
        drop_card()
        if image_counter%100==0 :
            hooshang()
        if image_counter%150==0 :
            hoosh()
        fire()
        if image_counter % 100 :
            InTesla()
        move()
        move_up()
        show_towers()
        show_heros_in_game(image_counter)
        show_time()
        show_elixir()
        show_crowns()
        game_controler()
    elif end_game==True:
        draw_map()
        if game_result[0]>game_result[1]:
            for i in towers_in_game :
                if i.id==2 :
                    k=towers_in_game.index(i)
                    destroyed_towers.append(towers_in_game[k])
                    del towers_in_game[k]
                    del attacking_towers_in_game[k]
                    del target_towers_in_game[k]

        elif game_result[1]>game_result[0]:
            for i in towers_in_game :
                if i.id==1 :
                    k = towers_in_game.index(i)
                    destroyed_towers.append(towers_in_game[k])
                    del towers_in_game[k]
                    del attacking_towers_in_game[k]
                    del target_towers_in_game[k]

        show_towers()
        if game_result[0]>game_result[1]:
            window.blit(pygame.image.load('images/Blue_winner.png'),(0,0))
            window.blit(pygame.image.load('images/red_crown.png'), (635 - 350, 200 + 250))
            window.blit(pygame.image.load('images/blue_crown.png'), (640 - 350, 250 + 250))
            font = pygame.font.SysFont("comicsansms", 32)
            text1 = font.render(str(game_result[0]), True, (0, 0, 255))
            text2 = font.render(str(game_result[1]), True, (255, 0, 0))
            window.blit(text1, (620 - 350 - text1.get_width() // 2, 275 + 250 - text1.get_height() // 2))
            window.blit(text2, (620 - 350 - text2.get_width() // 2, 225 + 250 - text2.get_height() // 2))

        elif game_result[1]>game_result[0]:
            window.blit(pygame.image.load('images/Red_winner.png'),(0,0))
            window.blit(pygame.image.load('images/red_crown.png'), (635 - 350, 200 + 250))
            window.blit(pygame.image.load('images/blue_crown.png'), (640 - 350, 250 + 250))
            font = pygame.font.SysFont("comicsansms", 32)
            text1 = font.render(str(game_result[0]), True, (0, 0, 255))
            text2 = font.render(str(game_result[1]), True, (255, 0, 0))
            window.blit(text1, (620 - 350 - text1.get_width() // 2, 275 + 250 - text1.get_height() // 2))
            window.blit(text2, (620 - 350 - text2.get_width() // 2, 225 + 250 - text2.get_height() // 2))

        else:
            window.blit(pygame.image.load('images/Draw.png'),(0,0))

    pygame.display.update()


