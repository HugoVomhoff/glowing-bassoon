import random
import pygame
import sys
import time
import math

class Button():
	def __init__(self, x, y, image, scale):
		width = Screen_Widht
		height = Screen_Height
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

class Frogg(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('Bilder/1_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/2_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/3_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/4_frog.png'))
		self.sprites.append(pygame.image.load('Bilder/5_frog.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

class Player(): 
    def __init__ (self, Str, Hp, lvl):
        self.inventory = ["Empty", "Empty", "Empty", "Empty", "Empty"]
        self.value_inventory = []
        self.Hp = Hp
        self.Str = Str
        self.lvl = lvl
    
    def Show_Stats(self):
        
        print(self.Hp)
        print(self.Str)
        print(self.lvl)

    def Set_Difficulty(self, difficulty):
       # self.difficulty = input(f" {'':_<101} \n|{'':<101}|\n|{'':<39}{'':_<23}{'':<39}|\n|{'':<38}| Välj svårighetsgraden |{'':<38}|\n|{'':38}|{'':_<23}|{'':<38}|\n|{'':<101}|\n|{'':<3} {'':_<29}{'':<2} {'':_<29}{'':<2} {'':_<29} {'':<3}|\n|{'':<3}|{'':<12}Lätt{'':<13}| |{'':<11} Normal{'':<11}| |{'':<12}Svår{'':<13}|{'':<3}|\n|{'':<3}|{'':_<29}| |{'':_<29}| |{'':_<29}|{'':<3}|\n|{'':<101}|\n|{'':_<101}|\n")
        if difficulty == 1:
            self.monstermaxstr = 100
        elif difficulty == 2:
            self.monstermaxstr = 200
        elif difficulty == 3:
            self.monstermaxstr = 400
        
    def Choice(self, Choice):

        if Choice == 1:
            self.Show_Stats()
        elif Choice == 2:
            self.Show_Inv()   
        elif Choice == 3:
            utfall = 1
            #random.randint(3,3)
            
            if utfall == 1:
                game_state.state = "Monster_Scene"

            if utfall == 2:
                
                GameState.state = 'Trap_Scene'
                self.Trap()
                
            if utfall == 3:
                
                GameState.state = 'Chest_Scene'
                self.Chest()
                
    def Trap(self):
        slumpadfälle = random.randint(1,5)
        print("Du ramlade ner i en Trap men vi hade glömt aktivera den så inget hända :)")

    def Chest(self):
        global alla_items
        failsafe_Chest = 0
        if failsafe_Chest == 1:
            print("grattis du fick jord igen")
        
        elif len(alla_items) == 2:
            founditem = random.randint(0, len(alla_items)-1)
            print(f"Du hittade {alla_items[founditem].Name}! {alla_items[founditem].Description}")
            self.inv_add(alla_items[founditem])
            failsafe_Chest = 1

        else:
            founditem = random.randint(0, len(alla_items)-1)
            print(f"Du hittade {alla_items[founditem].Name}! {alla_items[founditem].Description}")
            self.inv_add(alla_items[founditem])

    def str_add(self, AddedStr):
        self.Str = self.Str + AddedStr

    def ChangeHp(self, newHp):
        self.Hp = newHp

    def LevelUp(self):
        self.lvl += 1
        
    def monster(self):
        
        monster_str = random.randint((10*self.lvl),int(float(self.monstermaxstr) * (1 + self.lvl/20)))
        
        if self.Str > monster_str:
            self.LevelUp()
            game_state.state = "Win_Scene"

        elif self.Str == monster_str:
            game_state.state = "Draw_Scene"
            
        else:
            self.Hp = self.Hp - monster_str
            game_state.state = "Lose_Scene"

    def inv_add(self, item):
        if self.inventory.count("Empty") == 0:
            self.Show_Inv
            change = input("Vlken vill du ta bort? ->")
            if int(change) < 6:
                
                self.str_add(-1*(self.value_inventory[int(change) - 1].Strength)) 
                self.inventory[int(change) - 1] = item.Name
                self.str_add(item.Strength)
                self.value_inventory[int(change)-1] = item
        else:
            self.inventory[5 - self.inventory.count("Empty")] = item.Name
            self.str_add(item.Strength)
            self.value_inventory.append(item)
            
    def Show_Inv(self):
        for plats in self.inventory:
            print(plats)

class Item():   
    def __init__ (self, Name, Strength, Description):
        self.Name = Name
        self.Strength = Strength
        self.Description = Description

class GameState():
    def __init__(self):
        self.state = 'Titlecard'
    
    def Titlecard(self):
        
        # TITLECARD
        font_color = (255,255,255)
            
        font_obj = pygame.font.Font("Fonts/Font1.TTF",50)
        text_obj = font_obj.render("Davids Äventyr",True,font_color)
        text_rect = text_obj.get_rect(center = (Screen_Widht//2, Screen_Height//2-50))

        font_obj2 = pygame.font.Font("Fonts/Font1.TTF",25)
        text_obj2 = font_obj2.render("Press spacebar to continue",True,font_color)
        text_rect2 = text_obj2.get_rect(center = (Screen_Widht//2, Screen_Height-100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'Difficulty_Scene'

        
        screen.fill((0,0,0))

        screen.blit(text_obj, text_rect)
        screen.blit(text_obj2, text_rect2)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(Screen_Widht/2-300, Screen_Height/2+50, 500, 75), 5)
        
        screen.blit(text_obj2,(325,450)) 
        frogg.attack()
        moving_sprites.draw(screen)
        moving_sprites.update(0.15)

        pygame.display.flip()

    def Difficulty_Scene(self):
        #Difficulty_Scene
        font_color = (255,255,255)
        font_obj3 = pygame.font.Font("Fonts/Font1.TTF",45)
        text_obj3 = font_obj3.render("Välj svårighetsgrad!",True,font_color)

        image1 = pygame.image.load("Bilder/Lätt.png").convert_alpha()
        image2 = pygame.image.load("Bilder/normal.png").convert_alpha()
        image3 = pygame.image.load("Bilder/svår.png").convert_alpha()
        
        global Screen_Widht
        
        L_button = Button((Screen_Widht-(200*3))/(3+1), 200, image1, 0.1)
        N_button = Button((2*(Screen_Widht-(200*3))/(3+1)+200), 200, image2, 0.1)
        S_button = Button((3*(Screen_Widht-(200*3))/(3+1)+2*200), 200, image3, 0.1) 
        
        knapparnas_bredd = []
        knappbredden = 200
       
        
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if L_button.draw(screen):
                spelare.Set_Difficulty(1)
                self.state = 'Choice_Scene'
            if N_button.draw(screen):
                spelare.Set_Difficulty(2)
                self.state = 'Choice_Scene'
            if S_button.draw(screen):
                spelare.Set_Difficulty(3)
                self.state = 'Choice_Scene'    
        
        screen.fill((0, 0, 0))
        screen.blit(text_obj3,(325,125))
        S_button.draw(screen)
        N_button.draw(screen)
        L_button.draw(screen)
        pygame.display.flip()
    
    def Choice_Scene(self):
        #Choice_Scene
        font_color = (255,255,255)
        font_obj3 = pygame.font.Font("Fonts/Font1.TTF",45)
        text_obj3 = font_obj3.render("Välj svårighetsgrad!",True,font_color)

        image1 = pygame.image.load("Bilder/äventyr.png").convert_alpha()
        image2 = pygame.image.load("Bilder/inventory.png").convert_alpha()
        image3 = pygame.image.load("Bilder/stats.png").convert_alpha()
        image = pygame.image.load("Bilder/exit_btn.png").convert_alpha()
        
        
        Äventyr_Button = Button(((Screen_Widht-(200*3))/(3+1)), ((Screen_Height-(100*3))/(3+1)), image1, 0.1)
        Inventory_Button = Button((2*(Screen_Widht-(200*3))/(3+1)+1*200),((Screen_Height-(100*3))/(3+1)), image2, 0.1)
        Stats_Button = Button((3*(Screen_Widht-(200*3))/(3+1)+2*200), ((Screen_Height-(100*3))/(3+1)),image3, 0.1)
        Exit_Button = Button((3*(Screen_Widht-(200*3))/(3+1)+2*200), (3*(Screen_Height-(100*3))/(3+1)+2*100), image, 0.1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Exit_Button.draw(screen):
                pygame.quit()
                sys.exit()
                
            if Stats_Button.draw(screen):
                spelare.Choice(1)
                self.state = 'Show_Stats_Scene'
            if Inventory_Button.draw(screen):
                spelare.Choice(2)
                self.state = 'Show_Inv_Scene'
            if Äventyr_Button.draw(screen):
                self.state = 'Door_Choice_Scene'    
        
        screen.fill((0, 0, 0))      
        Exit_Button.draw(screen)
        Stats_Button.draw(screen)
        Inventory_Button.draw(screen)
        Äventyr_Button.draw(screen)

        pygame.display.flip()

    def Show_Stats_Scene(self):
        
        image1 = pygame.image.load("Bilder/exit_btn.png")
        Return_Button = Button(100, 400, image1, 0.1)
        
        screen.fill((0, 0, 0))
        Return_Button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Return_Button.draw(screen):
                self.state = 'Choice_Scene'
        
    def Show_Inv_Scene(self):
        
        image1 = pygame.image.load("Bilder/exit_btn.png")
        Return_Button = Button(100, 400, image1, 1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Return_Button.draw(screen):
                self.state = 'Choice_Scene'
        
        screen.fill((0, 0, 0))
        Return_Button.draw(screen)
        pygame.display.flip()
                
    def Door_Choice_Scene(self):
        
        Door1 = pygame.image.load("Bilder/dörr_1.png")
        Door2 = pygame.image.load("Bilder/dörr_2.png")
        Door3 = pygame.image.load("Bilder/dörr_3.png")

        Door1_Button = Button(100, 200, Door1, 0.1)
        Door2_Button = Button(450, 200, Door2, 0.1)
        Door3_Button = Button(700, 200, Door3, 0.1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if Door1_Button.draw(screen):
                spelare.Choice(3)
            if Door2_Button.draw(screen):
                spelare.Choice(3)
            if Door3_Button.draw(screen):
                spelare.Choice(3)
        
        screen.fill((0, 0, 0))
        
        Door1_Button.draw(screen)
        Door2_Button.draw(screen)
        Door3_Button.draw(screen)
        
        pygame.display.flip()

    def Monster_Scene(self):
        
        screen.fill((0, 0, 0))

        Monster1 = pygame.image.load("Bilder/monster.png")
        Monster1_Button = Button(100, 200, Monster1, 0.1)
        Monster1_Button.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        time.sleep(3)
        spelare.monster()

    def Win_Scene(self):
       
        image1 = pygame.image.load("Bilder/exit_btn.png")
        Return_Button = Button(100, 400, image1, 0.1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Return_Button.draw(screen):
                self.state = 'Choice_Scene'
        
        
        background = pygame.image.load("Bilder/Win.png")
       
        screen.blit(background,(0,0))
        
        Return_Button.draw(screen)
        pygame.display.flip()

    def Lose_Scene(self):
       
        image1 = pygame.image.load("Bilder/exit_btn.png")
        Return_Button = Button(100, 400, image1,0.1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Return_Button.draw(screen):
                self.state = 'Choice_Scene'
        
        
        background = pygame.image.load("Bilder/Lose.png")
       
        screen.blit(background,(0,0))
        
        Return_Button.draw(screen)
        pygame.display.flip()

    def Draw_Scene(self):
        
        image1 = pygame.image.load("Bilder/exit_btn.png")
        Return_Button = Button(100, 400, image1, 0.1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if Return_Button.draw(screen):
                self.state = 'Choice_Scene'
        
        
        background = pygame.image.load("Bilder/lika.png")
       
        screen.blit(background,(0,0))
        
        Return_Button.draw(screen)
        pygame.display.flip()

    def Trap_Scene(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def Chest_Scene(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def Main_Game_Scene(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'Door_Choice_Scene'  

        screen.fill((0,0,0))
        pygame.display.flip()
    
    def state_manager(self):
        
        
        if self.state == 'Titlecard':
            self.Titlecard()
        if self.state == 'Difficulty_Scene':
            self.Difficulty_Scene()
        if self.state == 'Choice_Scene':
            self.Choice_Scene()
        if self.state == "Show_Stats_Scene":
            self.Show_Stats_Scene()
        if self.state == "Show_Inv_Scene":
            self.Show_Inv_Scene()
        if self.state == "Door_Choice_Scene":
            self.Door_Choice_Scene()
        if self.state == "Chest_Scene":
            self.Chest_Scene()
        if self.state == "Monster_Scene":
            self.Monster_Scene()
        if self.state == "Win_Scene":
            self.Win_Scene()
        if self.state == "Lose_Scene":
            self.Lose_Scene()
        if self.state == "Draw_Scene":
            self.Draw_Scene()

        if self.state == "Trap_Scene":
            self.Trap_Scene()
        
        
        
        
        if self.state == 'Door_Choice_Scene':
            self.Door_Choice_Scene()

pygame.init()
Clock = pygame.time.Clock()
game_state = GameState()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
Screen_Widht, Screen_Height = pygame.display.get_surface().get_size()

pygame.display.set_caption("Davids Äventyr")
pygame.mouse.set_visible(True)

#Frogg
moving_sprites = pygame.sprite.Group()
frogg = Frogg(450,153)
moving_sprites.add(frogg)

#items
Fury_Of_The_Fallen = Item("FuryOfTheFallen", 20, "This charm is powered by the fury of the fallen and it gives it's wearer +20 strengt")
Longnail = Item("Longnail", 25, "It's a very long nail. +50 strength") 
Blade_of_the_Ruined_King = Item("Blade of the Ruined King", 30, "OYEEEE")
Voiti_consumed_by_hatred = Item("Voiti consumed by hatred", 80, "Arg pappa")

alla_items = [Longnail, Fury_Of_The_Fallen, Blade_of_the_Ruined_King, Voiti_consumed_by_hatred]

spelare = Player(100, 2000, 1)

while True:
    game_state.state_manager()
    Clock.tick(60)   
