import pygame
import time
import sys


from Class_Button import Button
from skärpning import draw_rect_alpha

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
class GameState():
    
    def __init__(self, spelare):
       
        self.state = 'Titlecard'
        self.screen_Width, self.screen_Height = pygame.display.get_surface().get_size()
        self.spelare = spelare
        self.scale = self.screen_Width / 1920

        self.Button_image = pygame.image.load("Bilder/Knapp.png").convert_alpha()
        self.Button1_image = pygame.image.load("Bilder/Knapp1.png").convert_alpha()


        pygame.display.set_caption("Davids Äventyr")
        pygame.mouse.set_visible(True)      
    
    def Titlecard(self):
         
        # TITLECARD
        
        
        font_color = (255, 255, 255)  
        font_obj = pygame.font.Font("Fonts/Font1.TTF",int(120*self.scale))
        text_obj = font_obj.render("Davids Äventyr",True,font_color)
        text_rect = text_obj.get_rect(center = (self.screen_Width//2, self.screen_Height//2))

        font_obj2 = pygame.font.Font("Fonts/Font1.TTF",int(31*self.scale))
        text_obj2 = font_obj2.render("Press spacebar to continue",True,font_color)
        text_rect2 = text_obj2.get_rect(center = (self.screen_Width//2, self.screen_Height-75*self.scale))

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
        pygame.draw.rect(screen, (255, 255, 255), 
        pygame.Rect((self.screen_Width/2-(500*self.scale)), (self.screen_Height/2-(75*self.scale)), int(1000*self.scale), int(150*self.scale)), int(5*self.scale))


        pygame.display.flip()

    def Difficulty_Scene(self):
        #Difficulty_Scene
 
        scale = 0.8

        font_color = (0,0,0)
        font_color2 = (255,255,255)
        font_obj3 = pygame.font.Font("Fonts/Font1.TTF", int(45*self.scale))
        font_obj4 = pygame.font.Font("Fonts/Font3.ttf", int(100*self.scale))
        font_obj5 = pygame.font.Font("Fonts/Font6.ttf", int(70*self.scale))
        text_obj3 = font_obj4.render("Choose Difficulty",True,font_color2)
        text_rect = text_obj3.get_rect(center = (self.screen_Width//2, self.screen_Height//2-200*self.scale))

        image_Width = self.Button1_image.get_width() * self.scale
        
        z = self.screen_Width-(image_Width*scale*3)
       
        L_button = Button((self.screen_Width-(image_Width*scale*3))/(4), 500*self.scale, self.Button1_image, scale)
        N_button = Button((2*(self.screen_Width-(image_Width*scale*3))/(4)+ scale*image_Width), 500*self.scale, self.Button1_image, scale)
        S_button = Button((3*(self.screen_Width-(image_Width*scale*3))/(4)+ 2 * scale*image_Width), 500*self.scale ,self.Button1_image, scale)
        
        text_obj4 = font_obj5.render("Easy", True, font_color)
        text_obj5 = font_obj5.render("Normal", True, font_color)
        text_obj6 = font_obj5.render("Hard", True, font_color)

        
        screen.fill((0, 0, 0))
        screen.blit(text_obj3,text_rect)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((self.screen_Width/2-(600*self.scale)), (self.screen_Height/2-(275*self.scale)), int(1200*self.scale), int(175*self.scale)), int(5*self.scale))

        S_button.draw(screen) 
        N_button.draw(screen)
        L_button.draw(screen)

        screen.blit(text_obj4,((z/(3+1)+image_Width*scale*0.1, 500*self.scale)))
        screen.blit(text_obj5,((2*(z)/(3+1)+image_Width*scale+image_Width*scale*0.1),500*self.scale))
        screen.blit(text_obj6,((3*(z)/(3+1)+2*image_Width*scale+image_Width*scale*0.1), 500*self.scale))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if pygame.mouse.get_pressed()[0] == 1:
            time.sleep(0.2)

        if L_button.draw(screen):
            self.spelare.Set_Difficulty(1)
            self.state = 'Choice_Scene'
        if N_button.draw(screen):
            self.spelare.Set_Difficulty(2)
            self.state = 'Choice_Scene'
        if S_button.draw(screen):
            self.spelare.Set_Difficulty(3)
            self.state = 'Choice_Scene'    
    
    def Choice_Scene(self):

        scale = 0.8
        #Choice_Scene
        font_color = (20,20,20)
        font_color2 = (100,100,100)        
        
        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        background_Width = bakgrund.get_width() * self.scale
        background_Height = bakgrund.get_height() * self.scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        font_obj5 = pygame.font.Font("Fonts/Font6.ttf", int(70 * self.scale))
        font_obj3 = pygame.font.Font("Fonts/Font1.TTF", int(100 * self.scale))

        text_obj3 = font_obj3.render("Choose Your Action",True,font_color2)
        text_rect = text_obj3.get_rect(center = (self.screen_Width//2, 150*self.scale))
        
        image_Width = self.Button_image.get_width() * self.scale
        image_Height = self.Button_image.get_height() * self.scale
       
        z = self.screen_Width-(image_Width*3)

        Äventyr_Button = Button(75*self.scale, (1*(self.screen_Height-(image_Height*scale*5))/(6)+2 * scale*image_Height), self.Button_image, scale)
        text_äventyr1 = font_obj5.render("Begin Exploring", True, font_color)
        text_äventyr2 = font_obj5.render("Keep Exploring", True, font_color)

        Inventory_Button = Button(75*self.scale, (2*(self.screen_Height-(image_Height*scale*5))/(6)+ 3* scale*image_Height), self.Button_image, scale)
        text_inventory = font_obj5.render("Show Inventory", True, font_color)

        Stats_Button = Button(75*self.scale, (3*(self.screen_Height-(image_Height*scale*5))/(6)+ 4 * scale*image_Height),self.Button_image, scale)
        text_stats = font_obj5.render("Show Stats", True, font_color)

        Exit_Button = Button(75*self.scale, (4*(self.screen_Height-(image_Height*scale*5))/(6)+ 5 * scale*image_Height), self.Button_image, scale)
        Exit_game = font_obj5.render("Exit Game", True, font_color)

           
        screen.blit(bakgrund, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (510*self.scale, 85*self.scale,900*self.scale, 120*self.scale,))
        Exit_Button.draw(screen)
        Stats_Button.draw(screen)
        Inventory_Button.draw(screen)
        Äventyr_Button.draw(screen)
        
        screen.blit(text_obj3,text_rect)
        screen.blit(text_äventyr1,((125*self.scale+image_Width*0.05), (1*(self.screen_Height-(image_Height*scale*5))/(6)+ 2 * scale*image_Height)))
        screen.blit(text_inventory,((125*self.scale+image_Width*0.05), (2*(self.screen_Height-(image_Height*scale*5))/(6)+ 3 * scale*image_Height)))
        screen.blit(text_stats,((125*self.scale+image_Width*0.05), (3*(self.screen_Height-(image_Height*scale*5))/(6)+ 4 * scale*image_Height)))
        screen.blit(Exit_game,((125*self.scale+image_Width*0.05), (4*(self.screen_Height-(image_Height*scale*5))/(6)+ 5 * scale*image_Height)))
        
        
        pygame.display.flip()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        if Exit_Button.draw(screen):
            pygame.quit()
            sys.exit()
        if Stats_Button.draw(screen):
            self.spelare.Choice(1)
        if Inventory_Button.draw(screen):
            self.spelare.Choice(2)
        if Äventyr_Button.draw(screen):
            self.state = 'Door_Choice_Scene' 

    def Show_Stats_Scene(self):

        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        background_Width = bakgrund.get_width() * self.scale
        background_Height = bakgrund.get_height() * self.scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        Character = pygame.image.load("renders/Färdigt/Character - oilpaint.png")
        background_Width = Character.get_width() * self.scale * 0.9
        background_Height = Character.get_height() * self.scale * 0.9
        Character = pygame.transform.scale(Character, (background_Width, background_Height))

        font_color = (120, 0, 0)  
        font_color1 = (139, 0, 139)  #lila
        font_color2 = (0, 120, 0)  #grönt 
        font_color3 = (255, 255, 0)  #gult ##### FINNS METOD ######
        font_color4 = (20,20,20)
        font_obj = pygame.font.Font("Fonts/Font1.TTF",int(70*self.scale))
        font_obj2 = pygame.font.Font("Fonts/Font6.ttf", int(70 * self.scale))

        text_obj = font_obj.render(f"Health : {self.spelare.Hp}",True,font_color)
        text_obj1 = font_obj.render(f"Strength : {self.spelare.Str}",True,font_color1)
        text_obj2 = font_obj.render(f"Level : {self.spelare.lvl}",True,font_color2)        
        text_obj3 = font_obj.render(f"Intelligence : {self.spelare.intelligence}",True,font_color3)

        text_obj4 = font_obj2.render("Go back", True, font_color4)
        Go_back = Button(730*self.scale, 850*self.scale, self.Button1_image, 0.8)

        screen.blit(bakgrund, (0,0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (150*self.scale, 90*self.scale,1620*self.scale, 900*self.scale,))
        Go_back.draw(screen)
        screen.blit(Character, (1200*self.scale, 125*self.scale))
        screen.blit(text_obj, (200*self.scale, 150*self.scale))
        screen.blit(text_obj1, (200*self.scale, 320*self.scale))
        screen.blit(text_obj2, (200*self.scale, 490*self.scale))
        screen.blit(text_obj3, (200*self.scale, 660*self.scale))
        screen.blit(text_obj4, (775*self.scale, 850*self.scale))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if Go_back.draw(screen):
            self.state = 'Choice_Scene'
        
    def Show_Inv_Scene(self):
        
        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        background_Width = bakgrund.get_width() * self.scale
        background_Height = bakgrund.get_height() * self.scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        font_color1 =(255, 255, 255)
        font_color2  =(120,0,0)
        font_color4 = (20,20,20)
        font_obj1 = pygame.font.Font("Fonts/Font6.ttf", int(70 * self.scale))
        font_obj2 = pygame.font.Font("Fonts/Font6.ttf", int(35 * self.scale))
        font_obj3 = pygame.font.Font("Fonts/Font6.ttf", int(25 * self.scale))
        text_obj4 = font_obj1.render("Go back", True, font_color4)
        Go_back = Button(730*self.scale, 880*self.scale, self.Button1_image, 0.8)
    
        inventory = self.spelare.inventory
        
        Item1_Bild = pygame.image.load(f"Bilder/{inventory[0].image}.png")
        Item1 = pygame.transform.scale(Item1_Bild, (120, 120))
        Item2_Bild = pygame.image.load(f"Bilder/{inventory[1].image}.png")
        Item2 = pygame.transform.scale(Item2_Bild, (120, 120))
        Item3_Bild = pygame.image.load(f"Bilder/{inventory[2].image}.png")
        Item3 = pygame.transform.scale(Item3_Bild, (120, 120))
        Item4_Bild = pygame.image.load(f"Bilder/{inventory[3].image}.png")
        Item4 = pygame.transform.scale(Item4_Bild, (120, 120))
        Item5_Bild = pygame.image.load(f"Bilder/{inventory[4].image}.png")
        Item5 = pygame.transform.scale(Item5_Bild, (120, 120))
        
        Item1_text = font_obj2.render(f" Name: {inventory[0].Name}, Description: {inventory[0].Description}",True,font_color1)
        Item2_text = font_obj2.render(f" Name: {inventory[1].Name}, Description: {inventory[1].Description}",True,font_color1)
        Item3_text = font_obj2.render(f" Name: {inventory[2].Name}, Description: {inventory[2].Description}",True,font_color1)
        Item4_text = font_obj2.render(f" Name: {inventory[3].Name}, Description: {inventory[3].Description}",True,font_color1)
        Item5_text = font_obj2.render(f" Name: {inventory[4].Name}, Description: {inventory[4].Description}",True,font_color1)
        
        Str_text1 = font_obj3.render(f" Strength: {inventory[0].Strength}",True,font_color2)
        Str_text2 = font_obj3.render(f" Strength: {inventory[1].Strength}",True,font_color2)
        Str_text3 = font_obj3.render(f" Strength: {inventory[2].Strength}",True,font_color2)
        Str_text4 = font_obj3.render(f" Strength: {inventory[3].Strength}",True,font_color2)
        Str_text5 = font_obj3.render(f" Strength: {inventory[4].Strength}",True,font_color2)
        
        screen.fill((0, 0, 0))
        screen.blit(bakgrund, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (50*self.scale, 50*self.scale,1820*self.scale, 980*self.scale,))
        Go_back.draw(screen)
        screen.blit(text_obj4, (775*self.scale, 880*self.scale))
        
        screen.blit(Item1, (100, 100))
        screen.blit(Item2, (100, 250))
        screen.blit(Item3, (100, 400))
        screen.blit(Item4, (100, 550))
        screen.blit(Item5, (100, 700))
        
        screen.blit(Item1_text, (250, 100))
        screen.blit(Item2_text, (250, 250))
        screen.blit(Item3_text, (250, 400))
        screen.blit(Item4_text, (250, 550))
        screen.blit(Item5_text, (250, 700))
        
        screen.blit(Str_text1, (250, 150))
        screen.blit(Str_text2, (250, 300))
        screen.blit(Str_text3, (250, 450))
        screen.blit(Str_text4, (250, 600))
        screen.blit(Str_text5, (250, 750))
       
           
        #Item1_Button.draw(screen)
        #Item2_Button.draw(screen)
        #Item3_Button.draw(screen)
        #Item4_Button.draw(screen)
        #Item5_Button.draw(screen) 
        
        pygame.display.flip()
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Go_back.draw(screen):
            self.state = 'Choice_Scene'
                  
    def Door_Choice_Scene(self):
        from Game_State import game_state
        font_color2 = (100,100,100)
        font_obj3 = pygame.font.Font("Fonts/Font1.TTF", int(100 * self.scale))
        text_obj3 = font_obj3.render("Where do you want to go? Pick a door!",True,font_color2)
        text_rect = text_obj3.get_rect(center = (self.screen_Width//2, 75*self.scale))
        
        Door1 = pygame.image.load("Bilder/dörrknapp1.png")
        Door2 = pygame.image.load("Bilder/dörrknapp2.png")
        door3 = pygame.image.load("Bilder/dörrknapp3.png")
        
        bakgrund = pygame.image.load("renders/Färdigt/Tre dörrar v3- oilpaint.png")
        background_Width = bakgrund.get_width() * self.scale
        background_Height = bakgrund.get_height() * self.scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        Door1_Button = Button(1458*self.scale, 235*self.scale, Door1, 1)   
        Door2_Button = Button(695*self.scale, 320*self.scale, Door2, 1) 
        Door3_Button = Button(145*self.scale, 270*self.scale, door3, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if Door1_Button.draw(screen):
            self.spelare.Choice(3)
        if Door2_Button.draw(screen):
            self.spelare.Choice(3)
        if Door3_Button.draw(screen):
            self.spelare.Choice(3)
        
        screen.blit(bakgrund,(0,0))
        
        Door1_Button.draw(screen)
        Door2_Button.draw(screen)
        Door3_Button.draw(screen)
        screen.blit(text_obj3, text_rect)
        
        pygame.display.flip()

    def Monster_Scene(self):
        
        
        Monster1 = pygame.image.load("renders/Färdigt/spindel - oilpaint.png")
        background_Width = Monster1.get_width() * self.scale
        background_Height = Monster1.get_height() * self.scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))

        
        screen.fill((0, 0, 0))
        screen.blit(Monster1, (0, 0))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        time.sleep(1.5)
        self.spelare.monster()

    def Win_Scene(self):
        Monster1 = pygame.image.load("renders/Färdigt/spindel - död - oilpaint.png")
        background_Width = Monster1.get_width() * self.scale
        background_Height = Monster1.get_height() * self.scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))

        image1 = pygame.image.load("Bilder/Knapp.png")
        Return_Button = Button(100, 400, image1, 0.1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Return_Button.draw(screen):
            self.state = 'Choice_Scene'
        
        screen.fill((0, 0, 0))
        screen.blit(Monster1, (0, 0))
        
        Return_Button.draw(screen)
        pygame.display.flip()

    def Lose_Scene(self):
        
        Monster1 = pygame.image.load("renders/Färdigt/spindel du dog - oilpaint.png")
        background_Width = Monster1.get_width() * self.scale
        background_Height = Monster1.get_height() * self.scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))
        
        image1 = pygame.image.load("Bilder/exit_btn.png")
        Return_Button = Button(100, 400, image1,0.1)
        
        screen.fill((0, 0, 0))
        screen.blit(Monster1, (0, 0))
        Return_Button.draw(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Return_Button.draw(screen):
            self.state = 'Choice_Scene'

    def Draw_Scene(self):
        
        Monster1 = pygame.image.load("renders/Färdigt/spindel - tie - oilpaint.png")
        background_Width = Monster1.get_width() * self.scale
        background_Height = Monster1.get_height() * self.scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))
        
        image1 = pygame.image.load("Bilder/Knapp.png")
        Return_Button = Button(100, 400, image1, 0.1)
         
        screen.fill((0, 0, 0))
        screen.blit(Monster1, (0, 0))
        
        background = pygame.image.load("Bilder/lika.png")
       
        screen.blit(background,(0,0))
        
        Return_Button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Return_Button.draw(screen):
            self.state = 'Choice_Scene'
       
    def Trap_Scene(self):
        
        Trap = pygame.image.load("renders/Färdigt/Trap1 - oilpaint.png")
        background_Width = Trap.get_width() * self.scale
        background_Height = Trap.get_height() * self.scale
        Trap = pygame.transform.scale(Trap, (background_Width, background_Height))
        
                
        screen.fill((0, 0, 0))
        screen.blit(Trap, (0,0))
        pygame.display.flip()
        
        time.sleep(1.5)
        if self.spelare.dodge_trap == True:
            self.state = 'Dodge_Trap_Scene'
        else:
            self.state = 'Fall_For_Trap_Scene' 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def Dodge_Trap_Scene(self):
        Trap = pygame.image.load("renders/Färdigt/Trap1 - dodge - oilpaint.png")
        background_Width = Trap.get_width() * self.scale
        background_Height = Trap.get_height() * self.scale
        Trap = pygame.transform.scale(Trap, (background_Width, background_Height))
        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(1000*self.scale, 800*self.scale, Continue_Button, 1)
        
        screen.fill((0, 0, 0))
        screen.blit(Trap, (0,0))
        Continue_Button.draw(screen)       
        pygame.display.flip()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def Fall_For_Trap_Scene(self):
        Trap = pygame.image.load("renders/Färdigt/Trap1 du dog - oilpaint.png")
        background_Width = Trap.get_width() * self.scale
        background_Height = Trap.get_height() * self.scale
        Trap = pygame.transform.scale(Trap, (background_Width, background_Height))    
         
        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(1000*self.scale, 800*self.scale, Continue_Button, 1)
        
        screen.fill((0,0,0))
        screen.blit(Trap, (0,0))
        Continue_Button.draw(screen)
        pygame.display.flip()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if Continue_Button.draw(screen):
            self.state = 'Choice_Scene'
         
    def Chest_Scene(self):
        font_color = (100,100,100) 

        font_obj3 = pygame.font.Font("Fonts/Font1.TTF", int(100 * self.scale))
        text_obj3 = font_obj3.render("Press the chest to open it",True,font_color)
        text_rect = text_obj3.get_rect(center = (self.screen_Width//2, 150*self.scale))

        Chest = pygame.image.load("renders/Färdigt/Kista - stängd - oilpaint.png")
        background_Width = Chest.get_width() * self.scale
        background_Height = Chest.get_height() * self.scale
        Chest = pygame.transform.scale(Chest, (background_Width, background_Height))

        Chest_Button = pygame.image.load("Bilder/kistknapp.png")
        Chest_Button = Button(700*self.scale, 440*self.scale, Chest_Button, 1)


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Chest_Button.draw(screen):
            
            self.spelare.Chest()
            self.found_item = self.spelare.current_item
            self.state = 'Chest_Scene_Open'


        screen.fill((0, 0, 0))
        screen.blit(Chest, (0, 0))
        Chest_Button.draw(screen)
        draw_rect_alpha(screen, (0, 0, 0, 100), (410*self.scale, 90*self.scale,1100*self.scale, 120*self.scale,))
        screen.blit(text_obj3,text_rect)
        pygame.display.flip()

    def Chest_Scene_Open(self):
        
        Open_Chest = pygame.image.load("renders/Färdigt/Kista - öppen - oilpaint.png")
        background_Width = Open_Chest.get_width() * self.scale
        background_Height = Open_Chest.get_height() * self.scale
        Open_Chest = pygame.transform.scale(Open_Chest, (background_Width, background_Height)) 

        font_color = (120,120,120) 
        
        font_obj3 = pygame.font.Font("Fonts/Font1.TTF", int(100 * self.scale))
        text_obj3 = font_obj3.render("You opened the chest and found:",True,font_color)
        text_rect = text_obj3.get_rect(center = (self.screen_Width//2, 170*self.scale))
        
        if self.spelare.chest_gold == True:

            font_obj4 = pygame.font.Font("Fonts/Font1.TTF", int(70 * self.scale))
            text_obj4 = font_obj4.render(f"{self.found_item} Gold",True,font_color)
            text_rect1 = text_obj4.get_rect(center = (self.screen_Width//2, 300*self.scale))

            item = pygame.image.load(f"Bilder/GULD.png")
            item_Width = item.get_width() * self.scale
            item_Height = item.get_height() * self.scale
            item = pygame.transform.scale(item, (item_Width, item_Height)) 

        else:
            font_obj4 = pygame.font.Font("Fonts/Font1.TTF", int(70 * self.scale))
            text_obj4 = font_obj4.render(self.found_item.Name,True,font_color)
            text_rect1 = text_obj4.get_rect(center = (self.screen_Width//2, 300*self.scale))

            item = pygame.image.load(f"Bilder/{self.found_item.image}.png")
            item_Width = item.get_width() * self.scale
            item_Height = item.get_height() * self.scale
            item = pygame.transform.scale(item, (item_Width, item_Height)) 

        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(910*self.scale, 800*self.scale, Continue_Button, 1)
        
        screen.fill((0, 0, 0))
        screen.blit(Open_Chest, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (310*self.scale, 90*self.scale,1300*self.scale, 900*self.scale,))
        screen.blit(text_obj3,text_rect)
        screen.blit(text_obj4,text_rect1)
        screen.blit(item, (self.screen_Width//2-item_Width/2, 500*self.scale))
        Continue_Button.draw(screen)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Continue_Button.draw(screen):
            
            if self.spelare.inv_full == True:
                self.state = 'Item_manager'
            else:
                self.state = "Choice_Scene"         
    
    def Item_manager(self):

        Open_Chest = pygame.image.load("renders/Färdigt/Kista - öppen - oilpaint.png")
        background_Width = Open_Chest.get_width() * self.scale
        background_Height = Open_Chest.get_height() * self.scale
        Open_Chest = pygame.transform.scale(Open_Chest, (background_Width, background_Height))

        screen.fill((0, 0, 0))
        screen.blit(Open_Chest, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (310*self.scale, 90*self.scale,1300*self.scale, 900*self.scale,))
        
        inventory = self.spelare.inventory

        
        Item1_Bild = pygame.image.load(f"renders/Default Renders/items{inventory[0].image}.png")
        Item2_Bild = pygame.image.load(f"renders/Default Renders/items{inventory[1].image}.png")
        Item3_Bild = pygame.image.load(f"renders/Default Renders/items{inventory[2].image}.png")
        Item4_Bild = pygame.image.load(f"renders/Default Renders/items{inventory[3].image}.png")
        Item5_Bild = pygame.image.load(f"renders/Default Renders/items{inventory[4].image}.png")

        Item1_Button = Button(910*self.scale, 800*self.scale, Item1_Bild, 1)
        Item2_Button = Button(910*self.scale, 800*self.scale, Item2_Bild, 1)
        Item3_Button = Button(910*self.scale, 800*self.scale, Item3_Bild, 1)
        Item4_Button = Button(910*self.scale, 800*self.scale, Item4_Bild, 1)
        Item5_Button = Button(910*self.scale, 800*self.scale, Item5_Bild, 1)

        Item1_Button.draw(screen)
        Item2_Button.draw(screen)
        Item3_Button.draw(screen)
        Item4_Button.draw(screen)
        Item5_Button.draw(screen)

        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(910*self.scale, 800*self.scale, Continue_Button, 1)
        Continue_Button.draw(screen)
        pygame.display.flip()

        if Item1_Button.draw(screen):
            self.inv_change = 1
            self.spelare.inv_change(1)
            
        if Item2_Button.draw(screen):
            self.inv_change = 2
            self.spelare.inv_change(2)

        if Item3_Button.draw(screen):
            self.inv_change = 3
            self.spelare.inv_change(3)

        if Item4_Button.draw(screen):
            self.inv_change = 4
            self.spelare.inv_change(4)

        if Item5_Button.draw(screen):
            self.inv_change = 5
            self.spelare.inv_change(5)

        if Continue_Button.draw(screen):
            self.state = 'Choice_Scene'

                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def Shop_Scene(self):
        from Class_Item import Shop_List
        
         
        Item1_Bild = pygame.image.load(f"Bilder/{Shop_List[0].image}.png")
        Item2_Bild = pygame.image.load(f"Bilder/{Shop_List[1].image}.png")
        Item3_Bild = pygame.image.load(f"Bilder/{Shop_List[2].image}.png")
        Item4_Bild = pygame.image.load(f"Bilder/{Shop_List[3].image}.png")
        Item5_Bild = pygame.image.load(f"Bilder/{Shop_List[4].image}.png")

        Item1_Button = Button(910*self.scale, 800*self.scale, Item1_Bild, 1)
        Item2_Button = Button(910*self.scale, 800*self.scale, Item2_Bild, 1)
        Item3_Button = Button(910*self.scale, 800*self.scale, Item3_Bild, 1)
        Item4_Button = Button(910*self.scale, 800*self.scale, Item4_Bild, 1)
        Item5_Button = Button(910*self.scale, 800*self.scale, Item5_Bild, 1)

        Item1_Button.draw(screen)
        Item2_Button.draw(screen)
        Item3_Button.draw(screen)
        Item4_Button.draw(screen)
        Item5_Button.draw(screen)

        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(910*self.scale, 800*self.scale, Continue_Button, 1)
        Continue_Button.draw(screen)
        pygame.display.flip()

        if Item1_Button.draw(screen):
            någonting = Shop_List[0]

            if self.gold > någonting.price:
                self.inv_add(någonting)
                self.gold -= någonting.price
            #else:
                #Du hade inte tillräckligt mycket guld

              
            
        if Item2_Button.draw(screen):
            någonting = Shop_List[1]

            if self.gold > någonting.price:
                self.inv_add(någonting)
                self.gold -= någonting.price
            #else:
                #Du hade inte tillräckligt mycket guld

        if Item3_Button.draw(screen):
            någonting = Shop_List[2]

            if self.gold > någonting.price:
                self.inv_add(någonting)
                self.gold -= någonting.price
            #else:
                #Du hade inte tillräckligt mycket guld

        if Item4_Button.draw(screen):
            någonting = Shop_List[3]

            if self.gold > någonting.price:
                self.inv_add(någonting)
                self.gold -= någonting.price
            #else:
                #Du hade inte tillräckligt mycket guld
        if Item5_Button.draw(screen):
            någonting = Shop_List[4]

            if self.gold > någonting.price:
                self.inv_add(någonting)
                self.gold -= någonting.price
            # else:
                #Du hade inte tillräckligt mycket guld  

    def Game_Over_Scene(self):
        from Class_Item import Empty
        self.spelare.Hp = 100
        self.spelare.Str = 200
        self.spelare.lvl = 1
        self.spelare.intelligence = 100
        self.spelare.inventory = [Empty, Empty, Empty, Empty, Empty]
        
        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(1000*self.scale, 800*self.scale, Continue_Button, 1)
        
        Exit = pygame.image.load("Bilder/exit_btn.png")
        Exit_Button = Button(710*self.scale, 800*self.scale, Exit, 1)
        

        font_color = (255, 255, 255)  
        font_obj = pygame.font.Font("Fonts/Font1.TTF",int(120*self.scale))
        text_obj = font_obj.render("Du är stendöd",True,font_color)
        text_rect = text_obj.get_rect(center = (self.screen_Width//2, self.screen_Height//2))

        screen.fill((0,0,0))
        Continue_Button.draw(screen)
        Exit_Button.draw(screen)
        screen.blit(text_obj, text_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Continue_Button.draw(screen):
            self.state = 'Titlecard'
        if Exit_Button.draw(screen):
            pygame.quit()
            sys.exit()

    def state_manager(self):
       
        if self.spelare.Hp < 1:
            self.state = "Game_Over_Scene"

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
        if self.state == "Chest_Scene_Open":
            self.Chest_Scene_Open()
        if self.state == 'Item_manager':
            self.Item_manager()
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
        if self.state == 'Dodge_Trap_Scene':
            self.Dodge_Trap_Scene()
        if self.state == 'Fall_For_Trap_Scene':
            self.Fall_For_Trap_Scene()
        if self.state == "Game_Over_Scene":
            self.Game_Over_Scene()       
        if self.state == 'Door_Choice_Scene':
            self.Door_Choice_Scene()       
        if self.state == "Shop_Scene":
            self.Shop_Scene()