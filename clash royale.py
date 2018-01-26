import pygame,time,random,sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
#heros infornarions
class Hero :
    def __init__(self,damage,hit_point,hit_speed,range,area_damage,hero_cost,hero_type,target):
        self.damage=damage
        self.hit_point=hit_point
        self.hit_speed=hit_speed
        self.range=range
        self.area_damage=area_damage
        self.hero_cost=hero_cost
        self.type=hero_type
        self.target=target

class Wizard(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,228,598,1.4,8,True,5,"ground",("air","ground","building"))
        self.position = position
        self.id=id

        #each list includes 4 image of the hero : [up1 , up2 , down1 , down2]

        self.move_image=[pygame.image.load('images/wizard_move_up1.png'),pygame.image.load('images/wizard_move_up2.png')
            ,pygame.image.load('images/wizard_move_down1.png'),pygame.image.load('images/wizard_move_down2.png')]
        self.attack_image=[pygame.image.load('images/wizard_attack_up1.png'),pygame.image.load('images/wizard_attack_up2.png')
            ,pygame.image.load('images/wizard_attack_down1.png'),pygame.image.load('images/wizard_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/Wizard_fire.png") , self.position]

class Balloon(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,798,1396,3,2,False,5,"air",("building"))
        self.position=position
        self.id=id
        self.move_image = [pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')
            ,pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')]
        self.attack_image=[pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')
            ,pygame.image.load('images/balloon1.png'),pygame.image.load('images/balloon1.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]


class Pekka(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,598,1059,1.8,2,False,4,"ground",("ground","building"))
        self.position=position
        self.id=id
        self.move_image = [pygame.image.load('images/pekka_move_up1.png'),pygame.image.load('images/pekka_move_up2.png')
            ,pygame.image.load('images/pekka_move_down1.png'),pygame.image.load('images/pekka_move_down2.png')]
        self.attack_image=[pygame.image.load('images/pekka_attack_up1.png'),pygame.image.load('images/pekka_attack_up2.png')
            ,pygame.image.load('images/pekka_attack_down1.png'),pygame.image.load('images/pekka_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]


class Archer(Hero):
    def __init__(self,position,id):
        Hero.__init__(self,86,254,1.2,4,True,2,"ground",("air","ground","building"))
        self.position=position
        self.id=id
        self.move_image =[pygame.image.load('images/archer_move_up1.png'),pygame.image.load('images/archer_move_up2.png')
            ,pygame.image.load('images/archer_move_down1.png'),pygame.image.load('images/archer_move_down2.png')]
        self.attack_image=[pygame.image.load('images/archer_attack_up1.png'),pygame.image.load('images/archer_attack_up2.png')
            ,pygame.image.load('images/archer_attack_down1.png'),pygame.image.load('images/archer_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/Archer_arrow.png") , self.position]

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
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]


class Giant(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 211, 3344, 1.5, 2 , False, 5, "ground", ("building"))
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/giant_move_up1.png'),pygame.image.load('images/giant_move_up2.png')
            ,pygame.image.load('images/giant_move_down1.png'),pygame.image.load('images/giant_move_down2.png')]
        self.attack_image=[pygame.image.load('images/giant_attack_up1.png'),pygame.image.load('images/giant_attack_up2.png')
            ,pygame.image.load('images/giant_attack_down1.png'),pygame.image.load('images/giant_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]

class Knight(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 159, 1399, 1.2, 2, False, 3, "ground", ("ground", "building"))
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/knight_move_up1.png'),pygame.image.load('images/knight_move_up2.png')
            ,pygame.image.load('images/knight_move_down1.png'),pygame.image.load('images/knight_move_down2.png')]
        self.attack_image=[pygame.image.load('images/knight_attack_up1.png'),pygame.image.load('images/knight_attack_up2.png')
            ,pygame.image.load('images/knight_attack_down1.png'),pygame.image.load('images/knight_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]


class Mega_minion(Hero):
    def __init__(self, position,id):
        Hero.__init__(self, 258, 695, 1.5, 4, True, 3, "air", ("air","ground", "building"))
        self.position = position
        self.id=id
        self.move_image = [pygame.image.load('images/mega_minion_move_up1.png'),pygame.image.load('images/mega_minion_move_up2.png')
            ,pygame.image.load('images/mega_minion_move_down1.png'),pygame.image.load('images/mega_minion_move_down2.png')]
        self.attack_image=[pygame.image.load('images/mega_minion_attack_up1.png'),pygame.image.load('images/mega_minion_attack_up2.png')
            ,pygame.image.load('images/mega_minion_attack_down1.png'),pygame.image.load('images/mega_minion_attack_down2.png')]
        self.weapon_image = [pygame.image.load ("images/weapon.png") , self.position]

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
        Building.__init__(self,90,4500,1,7,"building",('air','ground','building'))
        self.position=position
        self.image=[image,image,image,image]
        self.attack_image=[image,image,image,image]
        self.weapon_image = [pygame.image.load ("images/Archer_arrow.png") , self.position]
        self.id=id


class Princess_tower (Building):
    def __init__(self,position,id,image):
        Building.__init__(self,100,2800,0.8,7.5,"building",('air','ground','building'))
        self.position=position
        self.image=[image,image,image,image]
        self.attack_image=[image,image,image,image]
        self.weapon_image = [pygame.image.load ("images/Archer_arrow.png") , self.position]
        self.id=id



#functions
def draw_map():
    '''draw map of the game at the first of the main while loop'''
    global window
    map_picture = pygame.image.load('images/field_2.jpg')
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
                attacking_heros_in_game.append(False)
                target_heros_in_game.append([])
                random_select_troop()
            else :
                trooplist_position[card_selected[1]]=(605,window_height-(card_selected[1]+1)*trooplist[card_selected[1]].get_size()[1])
                card_selected[0]=False
    for i in range(4):
        window.blit(trooplist[i],trooplist_position[i])



def move():

    global heros_in_game
    for i in heros_in_game:
       # print(i.weapon_image[1])

        if attacking_heros_in_game[heros_in_game.index(i)]==False :
            X0 = i.position[0]
            Y0 = i.position[1]
            X = X0
            Y = Y0
            if i.id == 1:
                if i.position[1] > 420 :
                    if X > 300:
                        if X > 510 :
                            if X > 520 or X < 500:
                                X -= 5
                            try:
                                Y -= abs((bridge_down_right_position[1] - i.position[1]) / (
                                        bridge_down_right_position[0] - i.position[0])) * 5
                            except ZeroDivisionError:
                                Y = Y0 - 5
                            if abs(Y - Y0) > 5.5 :
                                Y = Y0 - 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 - 1
                        else:
                            if X > 520 or X < 500:
                                X += 5
                            try:
                                Y -= abs((bridge_down_right_position[1] - i.position[1]) / (
                                        bridge_down_right_position[0] - i.position[0])) * 5
                            except:
                                Y = Y0 - 5
                            if abs(Y - Y0) > 5.5 :
                                Y = Y0 - 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 - 1
                    elif X > 90:
                        if X > 100 or X < 80:
                            X -= 5
                        try:
                            Y -= abs((bridge_down_left_position[1] - i.position[1]) / (
                                    bridge_down_left_position[0] - i.position[0])) * 5
                        except:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 - 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 - 1
                    else:
                        if X > 100 or X < 80:
                            X += 5
                        try:
                            Y -= abs((bridge_down_left_position[1] - i.position[1]) / (
                                    bridge_down_left_position[0] - i.position[0])) * 5
                        except:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 - 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 - 1


                else:
                    if X > 300 :
                        if X > 510:
                            if X > 520 or X < 500 :
                                X -= 5
                            try:
                                Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                        QueenTower_up_right_position[0] - i.position[0]))*5
                            except:
                                Y = Y0 - 5
                            if abs(Y - Y0) > 5.5:
                                Y = Y0 - 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 - 1
                        else:
                            if X > 520 or X < 500:
                                X += 5
                            try:
                                Y -= abs((QueenTower_up_right_position[1] - i.position[1]) / (
                                        QueenTower_up_right_position[0] - i.position[0]))*5
                            except:
                                Y = Y0 - 5
                            if abs(Y - Y0) > 5.5:
                                Y = Y0 - 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 - 1
                    elif X > 90:
                        if X > 100 or X < 80:
                            X -= 5
                        try:
                            Y -= abs((QueenTower_up_lef_position[1] - i.position[1]) / (
                                    QueenTower_up_lef_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 - 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 - 1
                    else:
                        if X > 100 or X < 80:
                            X += 5
                        try:
                            Y -= abs((QueenTower_up_lef_position[1] - i.position[1]) / (
                                    QueenTower_up_lef_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 - 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 - 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 - 1
                i.position = (X, Y)


            elif i.id == 2 :
                X0 = i.position[0]
                Y0 = i.position[1]
                X = X0
                Y = Y0
                if i.position[1] < 370 :
                    if X > 300:
                        if X > 510:
                            if X > 520 or X < 500:
                                X -= 5
                            try:
                                Y += abs((bridge_up_right_position[1] - i.position[1]) / (
                                        bridge_up_right_position[0] - i.position[0])) * 5
                            except ZeroDivisionError:
                                Y = Y0 + 5
                            if abs(Y - Y0) > 5.5:
                                Y = Y0 + 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 + 1
                        else:
                            if X > 520 or X < 500:
                                X += 5
                            try:
                                Y += abs((bridge_up_right_position[1] - i.position[1]) / (
                                        bridge_up_right_position[0] - i.position[0])) * 5
                            except:
                                Y = Y0 + 5
                            if abs(Y - Y0) > 5.5:
                                Y = Y0 + 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 + 1
                    elif X > 90:
                        if X > 100 or X < 80:
                            X -= 5
                        try:
                            Y += abs((bridge_up_left_position[1] - i.position[1]) / (
                                    bridge_up_left_position[0] - i.position[0])) * 5
                        except:
                            Y = Y0 + 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 + 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 + 1
                    else:
                        if X > 100 or X < 80:
                            X += 5
                        try:
                            Y += abs((bridge_up_left_position[1] - i.position[1]) / (
                                    bridge_up_left_position[0] - i.position[0])) * 5
                        except:
                            Y = Y0 + 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 + 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 + 1


                else:
                    if X > 300:
                        if X > 510:
                            if X > 520 or X < 500:
                                X -= 5
                            try:
                                Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                        QueenTower_down_right_position[0] - i.position[0]))*5
                            except:
                                Y = Y0 + 5
                            if abs(Y - Y0) > 5.5:
                                Y = Y0 + 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 + 1

                        else:
                            if X > 520 or X < 500:
                                X += 5
                            try:
                                Y += abs((QueenTower_down_right_position[1] - i.position[1]) / (
                                        QueenTower_down_right_position[0] - i.position[0]))*5
                            except:
                                Y = Y0 + 5
                            if abs(Y - Y0) > 5.5:
                                Y = Y0 + 5
                            if abs(Y - Y0) < 1 :
                                Y = Y0 + 1

                    elif X > 90:
                        if X > 100 or X < 80:
                            X -= 5
                        try:
                            Y += abs((QueenTower_down_lef_position[1] - i.position[1]) / (
                                    QueenTower_down_lef_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 + 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 + 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 + 1
                    else:
                        if X > 100 or X < 80:
                            X += 5
                        try:
                            Y += abs((QueenTower_down_lef_position[1] - i.position[1]) / (
                                    QueenTower_down_lef_position[0] - i.position[0]))*5
                        except:
                            Y = Y0 + 5
                        if abs(Y - Y0) > 5.5:
                            Y = Y0 + 5
                        if abs(Y - Y0) < 1:
                            Y = Y0 + 1

            i.position = (X, Y)




def show_heros_in_game (image_counter):
    for hero in heros_in_game :
        if attacking_heros_in_game[heros_in_game.index(hero)]==False :
            if hero.id==1 :
                if image_counter % 20 < 10:
                    pos = (hero.position[0] - hero.move_image[0].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[0].get_size()[1] / 2)
                    window.blit(hero.move_image[0],pos)
                else :
                    pos = (hero.position[0] - hero.move_image[1].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[1].get_size()[1] / 2)
                    window.blit(hero.move_image[1],pos)
            if hero.id==2 :
                if image_counter % 20 < 10:
                    pos = (hero.position[0] - hero.move_image[2].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[2].get_size()[1] / 2)
                    window.blit(hero.move_image[2],pos)
                else :
                    pos = (hero.position[0] - hero.move_image[3].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[3].get_size()[1] / 2)
                    window.blit(hero.move_image[3],pos)
        else :
            if hero.id==1 :
                if image_counter % 80 < 40:
                    pos = (hero.position[0] - hero.move_image[0].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[0].get_size()[1] / 2)
                    window.blit(hero.attack_image[0],pos)
                else :
                    pos = (hero.position[0] - hero.move_image[1].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[1].get_size()[1] / 2)
                    window.blit(hero.attack_image[1],pos)
            if hero.id==2 :
                if image_counter % 80 < 40:
                    pos = (hero.position[0] - hero.move_image[2].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[2].get_size()[1] / 2)
                    window.blit(hero.attack_image[2],pos)
                else :
                    pos = (hero.position[0] - hero.move_image[3].get_size()[0] / 2,
                           hero.position[1] - hero.move_image[3].get_size()[1] / 2)
                    window.blit(hero.attack_image[3],pos)

def fire() :
    for hero1 in heros_in_game :
        for hero2 in heros_in_game :
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
                        window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                    else:
                        attacking_heros_in_game[heros_in_game.index(hero1)] = True
                        target_heros_in_game[heros_in_game.index(hero2)].append(hero1)
                        shoot(hero2.position, hero1.weapon_image, hero1, hero2)
                        window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                else :
                    if attacking_heros_in_game[heros_in_game.index(hero1)]==True:
                        if hero1 in target_heros_in_game[heros_in_game.index(hero2)]:
                            attacking_heros_in_game[heros_in_game.index(hero1)]= False
                            del target_heros_in_game[heros_in_game.index(hero2)][target_heros_in_game[heros_in_game.index(hero2)].index(hero1)]


        for tower in towers_in_game :
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
                        window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,
                                                            hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                    else:
                        attacking_heros_in_game[heros_in_game.index(hero1)] = True
                        target_towers_in_game[towers_in_game.index(tower)].append(hero1)
                        shoot(tower.position, hero1.weapon_image, hero1, tower)
                        window.blit(hero1.weapon_image[0], (hero1.weapon_image[1][0] - hero1.weapon_image[0].get_size()[0]/2 ,
                                                            hero1.weapon_image[1][1] - hero1.weapon_image[0].get_size()[1]/2))
                else:
                    if attacking_heros_in_game[heros_in_game.index(hero1)] == True:
                        if hero1 in target_towers_in_game[towers_in_game.index(tower)]:
                            attacking_heros_in_game[heros_in_game.index(hero1)] = False
                            del target_towers_in_game[towers_in_game.index(tower)][target_towers_in_game[towers_in_game.index(tower)].index(hero1)]

    for tower in towers_in_game :
        for hero in heros_in_game :
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
                        target_towers_in_game[heros_in_game.index(hero)].append(tower)
                        shoot2(hero.position, tower.weapon_image, tower, hero)
                        window.blit(tower.weapon_image[0], (
                        tower.weapon_image[1][0] - tower.weapon_image[0].get_size()[0] / 2,
                        tower.weapon_image[1][1] - tower.weapon_image[0].get_size()[1] / 2))
                    else:
                        attacking_towers_in_game[towers_in_game.index(tower)] = True
                        target_towers_in_game[heros_in_game.index(hero)].append(tower)
                        shoot2(hero.position, tower.weapon_image, tower, hero)
                        window.blit(tower.weapon_image[0], (
                        tower.weapon_image[1][0] - tower.weapon_image[0].get_size()[0] / 2,
                        tower.weapon_image[1][1] - tower.weapon_image[0].get_size()[1] / 2))
                else:
                    if attacking_towers_in_game[towers_in_game.index(tower)] == True:
                        if tower in target_heros_in_game[heros_in_game.index(hero)]:
                            attacking_towers_in_game[towers_in_game.index(tower)] = False
                            del target_heros_in_game[heros_in_game.index(hero)][
                                target_heros_in_game[heros_in_game.index(hero)].index(tower)]


    for hero in heros_in_game:
        if hero.hit_point <= 0 :
            k=heros_in_game.index(hero)
            for i in target_heros_in_game[k]:
                if i in heros_in_game :
                    attacking_heros_in_game[heros_in_game.index(i)]=False
                if i in towers_in_game :
                    attacking_towers_in_game[towers_in_game.index(i)]=False
            del heros_in_game[k]
            del attacking_heros_in_game[k]
    for tower in towers_in_game :
        if tower.hit_point <= 0 :
            k=towers_in_game.index(tower)
            for i in target_towers_in_game[k]:
                if i in heros_in_game :
                    attacking_heros_in_game[heros_in_game.index(i)]=False
            destroyed_towers.append(towers_in_game[k])
            del towers_in_game[k]
            del attacking_towers_in_game[k]






def shoot2(target_position , weapon_image , tower , hero):
    if target_position[0] - 15 < weapon_image[1][0]  and target_position[0] +15 > weapon_image[1][0] :
        if target_position[1] -20 < weapon_image[1][1]  and target_position[1] +20 > weapon_image[1][1]  :
            hero.hit_point -= tower.damage
            attacking_towers_in_game[towers_in_game.index(tower)] = False
            weapon_image[1] = tower.position

    x1 = weapon_image[1][0]
    y1 = weapon_image[1][1]
    if x1 > target_position[0]:
        if y1 > target_position[1] :
            x1 -= 1
            try :
                y1 -= abs((target_position[1] - y1) / (target_position[0] - x1))
            except :
                y1 = weapon_image[1][1] - 10
            if abs(weapon_image[1][1] - y1) > 10 :
                y1 = weapon_image[1][1] - 10
        else:
            x1 -= 1
            try :
                y1 += abs((target_position[1] - y1) / (target_position[0] - x1))
            except :
                y1 = weapon_image[1][1] + 10
            if abs(weapon_image[1][1] - y1) > 10 :
                y1 = weapon_image[1][1] + 10
    elif y1 < target_position[1] :
        x1 += 1
        try:
            y1 += abs((target_position[1] - y1) / (target_position[0] - x1))
        except:
            y1 = weapon_image[1][1] + 10
        if abs(weapon_image[1][1] - y1) > 10:
            y1 = weapon_image[1][1] + 10
    else :
        x1 += 1
        try:
            y1 -= abs((target_position[1] - y1) / (target_position[0] - x1))
        except:
            y1 = weapon_image[1][1] - 10
        if abs(weapon_image[1][1] - y1) > 10:
            y1 = weapon_image[1][1] - 10
    weapon_image[1] = (x1 , y1)


def shoot(target_position , weapon_image , hero1 , hero2):
    if target_position[0] - 15 < weapon_image[1][0]  and target_position[0] +15 > weapon_image[1][0] :
        if target_position[1] -20 < weapon_image[1][1]  and target_position[1] +20 > weapon_image[1][1]  :
            hero2.hit_point -= hero1.damage
            attacking_heros_in_game[heros_in_game.index(hero1)] = False
            weapon_image[1] = hero1.position

    x1 = weapon_image[1][0]
    y1 = weapon_image[1][1]
    if x1 > target_position[0]:
        if y1 > target_position[1] :
            x1 -= 1
            try :
                y1 -= abs((target_position[1] - y1) / (target_position[0] - x1))
            except :
                y1 = weapon_image[1][1] - 10
            if abs(weapon_image[1][1] - y1) > 10 :
                y1 = weapon_image[1][1] - 10
        else:
            x1 -= 1
            try :
                y1 += abs((target_position[1] - y1) / (target_position[0] - x1))
            except :
                y1 = weapon_image[1][1] + 10
            if abs(weapon_image[1][1] - y1) > 10 :
                y1 = weapon_image[1][1] + 10
    elif y1 < target_position[1] :
        x1 += 1
        try:
            y1 += abs((target_position[1] - y1) / (target_position[0] - x1))
        except:
            y1 = weapon_image[1][1] + 10
        if abs(weapon_image[1][1] - y1) > 10:
            y1 = weapon_image[1][1] + 10
    else :
        x1 += 1
        try:
            y1 -= abs((target_position[1] - y1) / (target_position[0] - x1))
        except:
            y1 = weapon_image[1][1] - 10
        if abs(weapon_image[1][1] - y1) > 10:
            y1 = weapon_image[1][1] - 10
    weapon_image[1] = (x1 , y1)




def show_towers():
    for i in towers_in_game :
        window.blit(i.image[1],(i.position[0]-i.image[1].get_size()[0]/2,i.position[1]-i.image[1].get_size()[1]/2))
    for i in destroyed_towers :
        window.blit(i.destroyed_image,(i.position[0]-i.destroyed_image.get_size()[0]/2,i.position[1]-i.destroyed_image.get_size()[1]/2))




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
heros_in_game=[Wizard((0,0),2),Knight((350,310),2)]
attacking_heros_in_game=[False,False]
target_heros_in_game=[[],[]]
towers_in_game=[Princess_tower((10+75,20+75),2,pygame.image.load('images\Queen_tower_up.png')),Princess_tower((430+75,20+75),2,pygame.image.load('images\Queen_tower_up.png')),
                Princess_tower((10+75, 650+75), 1, pygame.image.load('images\Queen_tower_down.png')),Princess_tower((430+75,650+75),1,pygame.image.load('images\Queen_tower_down.png')),
                King_tower((225+75,0+75),2,pygame.image.load('images\King_tower_up.png')),King_tower((225+75,650+75),1,pygame.image.load('images\King_tower_down.png'))]
attacking_towers_in_game=[False,False,False,False,False,False]
target_towers_in_game=[[],[],[],[],[],[]]
destroyed_towers=[]
trooplist = []
trooplist_position=[]
trooplist_name=[]
window_width=700
window_height=800


bridge_up_left_position = (90 , 370)
bridge_down_left_position = (90 , 420)
bridge_up_right_position = (510 , 370)
bridge_down_right_position = (510 , 420)

QueenTower_up_lef_position = (90 , 85)
QueenTower_up_right_position = (510 , 85)
QueenTower_down_lef_position = (90 , 700)
QueenTower_down_right_position = (510 , 700)

#main()
pygame.init()
window=pygame.display.set_mode((window_width,window_height))
image_counter=0

while True :

    draw_map()
    image_counter+=1
    drop_card()
    if image_counter % 3 == 0:
        fire()
    if image_counter % 6 == 0 :
        move()
    show_towers()
    show_heros_in_game(image_counter)
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quit_game()
    pygame.display.update()


