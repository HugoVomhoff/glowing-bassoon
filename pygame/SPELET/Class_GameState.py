import pygame
import time
import sys
from Class_Button import Button
from Variabler import draw_rect_alpha, fonts

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_Width, screen_Height = pygame.display.get_surface().get_size()
scale = screen_Width / 1920

# Fonts
font1, font2, Font1_30, Font1_70, Font1_100, Font1_120, Font6_25, Font6_35, Font6_70 = fonts

# Font colors
Gray = (100, 100, 100)
Black = (0,0,0)
White = (255, 255, 255)
Gold = (255, 192, 0)
Dark_Grey = (20, 20, 20)
Purple = (139, 0, 139)
Yellow = (255, 255, 0)
Red = (120, 0, 0)
Green = (0, 120, 0)
  
# Default images
Button_image = pygame.image.load("Bilder/Knapp.png").convert_alpha()
Button1_image = pygame.image.load("Bilder/Knapp1.png").convert_alpha()

image_Width = Button1_image.get_width() *scale
image_Height = Button_image.get_height() * scale

class GameState(): ### hoppas att ni förstår vår kod :))))) ####
    
    def __init__(self, spelare):
       
        self.state = 'Titlecard'
        self.spelare = spelare

    def Titlecard(self):
          
        text_obj = Font1_120.render("Davids Äventyr",True,White)
        text_rect = text_obj.get_rect(center = (screen_Width//2, screen_Height/2))

        text_obj2 = Font1_30.render("Press spacebar to continue", True, White)
        text_rect2 = text_obj2.get_rect(center = (screen_Width//2, screen_Height-75*scale))

        screen.fill((0,0,0))
        screen.blit(text_obj, text_rect)
        screen.blit(text_obj2, text_rect2)
        pygame.draw.rect(screen, (255, 255, 255), 
        pygame.Rect((screen_Width/2-(500*scale)), (screen_Height/2-(75*scale)), int(1000*scale), int(150*scale)), int(5*scale))

        pygame.display.flip()
        
        
        if pygame.key.get_pressed()[pygame.K_SPACE] == True:
            self.state = 'Difficulty_Scene'

        for event in pygame.event.get(pygame.QUIT):  
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                  
    def Difficulty_Scene(self): 

        text_obj3 = Font1_120.render("Choose Difficulty",True,White)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, screen_Height//2-190*scale))
       
        L_button = Button((screen_Width-(image_Width*scale*3))/(4), 500*scale, Button1_image, 0.8)
        N_button = Button((2*(screen_Width-(image_Width*scale*3))/(4)+ scale*image_Width), 500*scale, Button1_image, 0.8)
        S_button = Button((3*(screen_Width-(image_Width*scale*3))/(4)+ 2 * scale*image_Width), 500*scale ,Button1_image, 0.8)
        
        Easy = Font6_70.render("Easy", True, White)
        Normal = Font6_70.render("Normal", True, White)
        Hard = Font6_70.render("Hard", True, White)

        
        screen.fill((0, 0, 0))
        screen.blit(text_obj3,text_rect)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((screen_Width/2-(600*scale)), (screen_Height/2-(275*scale)), int(1200*scale), int(175*scale)), int(5*scale))

        S_button.draw(screen) 
        N_button.draw(screen)
        L_button.draw(screen)

        screen.blit(Easy,((screen_Width-(image_Width*3)/(3+1), 500*scale)))
        screen.blit(Normal,((2*(screen_Width-(image_Width*3))/(3+1)+image_Width*0.8),500*scale))
        screen.blit(Hard,((3*(screen_Width-(image_Width*3))/(3+1)+2*image_Width*0.8), 500*scale))
        pygame.display.flip()

        if L_button.clicked():
            self.spelare.Set_Difficulty(1)
            self.state = 'Choice_Scene'

        if N_button.clicked():
            self.spelare.Set_Difficulty(2)
            self.state = 'Choice_Scene'

        if S_button.clicked():
            self.spelare.Set_Difficulty(3)
            self.state = 'Choice_Scene'    

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def Choice_Scene(self):

        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        background_Width = bakgrund.get_width() *scale
        background_Height = bakgrund.get_height() *scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        text_obj3 = Font1_100.render("Choose Your Action",True,Gray)
        text_rect = text_obj3.get_rect(center = (screen_Width/2, 150*scale))

        Äventyr_Button = Button(75*scale, (1*(screen_Height-(image_Height*6.5))/(7.5)+2 * image_Height), Button_image, 0.8)
        text_äventyr1 = Font6_70.render("Begin Exploring", True, Dark_Grey)
    
        Inventory_Button = Button(75*scale, (2*(screen_Height-(image_Height*6.5))/(7.5)+ 3* image_Height), Button_image, 0.8)
        text_inventory = Font6_70.render("Show Inventory", True, Dark_Grey)

        Stats_Button = Button(75*scale, (3*(screen_Height-(image_Height*6.5))/(7.5)+ 4 * image_Height),Button_image, 0.8)
        text_stats = Font6_70.render("Show Stats", True, Dark_Grey)
        
        Shop_button = Button(75*scale, (4*(screen_Height-(image_Height*6.5))/(7.5)+5 * image_Height), Button_image, 0.8)
        text_shop = Font6_70.render("Shop", True, Dark_Grey)

        Exit_Button = Button(75*scale, (5*(screen_Height-(image_Height*6.5))/(7.5)+ 6 * image_Height), Button_image, 0.8)
        Exit_game = Font6_70.render("Exit Game", True, Dark_Grey)

           
        screen.blit(bakgrund, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (510*scale, 85*scale,900*scale, 120*scale,))
        Exit_Button.draw(screen)
        Stats_Button.draw(screen)
        Inventory_Button.draw(screen)
        Äventyr_Button.draw(screen)
        Shop_button.draw(screen)
                
        screen.blit(text_obj3,text_rect)
        screen.blit(text_äventyr1,((125*scale+image_Width*0.05), (1*(screen_Height-(image_Height*6.5))/(7.5)+ 2 * image_Height)))
        screen.blit(text_inventory,((125*scale+image_Width*0.05), (2*(screen_Height-(image_Height*6.5))/(7.5)+ 3 * image_Height)))
        screen.blit(text_stats,((125*scale+image_Width*0.05), (3*(screen_Height-(image_Height*6.5))/(7.5)+ 4 * image_Height)))
        screen.blit(text_shop,((125*scale+image_Width*0.05), (4*(screen_Height-(image_Height*6.5))/(7.5)+ 5 * image_Height)))
        screen.blit(Exit_game,((125*scale+image_Width*0.05), (5*(screen_Height-(image_Height*6.5))/(7.5)+ 6 * image_Height)))
        
        
        pygame.display.flip()
    
        
        if Stats_Button.clicked():
            self.spelare.Choice(1)

        if Inventory_Button.clicked():
            self.spelare.Choice(2)

        if Äventyr_Button.clicked():
            self.state = 'Door_Choice_Scene' 

        if Shop_button.clicked():
            self.state = 'Shop_Scene'
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        if Exit_Button.clicked():
            pygame.quit()
            sys.exit()

    def Show_Stats_Scene(self):

        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        background_Width = bakgrund.get_width() * scale
        background_Height = bakgrund.get_height() * scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        Character = pygame.image.load("renders/Färdigt/Character - oilpaint.png")
        background_Width = Character.get_width() * scale * 0.9
        background_Height = Character.get_height() * scale * 0.9
        Character = pygame.transform.scale(Character, (background_Width, background_Height))

        text_obj = Font1_70.render(f"Health : {self.spelare.Hp}",True,Red)
        text_obj1 = Font1_70.render(f"Strength : {self.spelare.Str}",True,Purple)
        text_obj2 = Font1_70.render(f"Level : {self.spelare.lvl}",True,Green)        
        text_obj3 = Font1_70.render(f"Intelligence : {self.spelare.intelligence}",True,Yellow)

        text_obj4 = Font6_70.render("Go back", True, Dark_Grey)
        Go_back = Button(730*scale, 850*scale, Button1_image, 0.8)

        screen.blit(bakgrund, (0,0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (150*scale, 90*scale,1620*scale, 900*scale,))
        Go_back.draw(screen)
        screen.blit(Character, (1200*scale, 125*scale))
        screen.blit(text_obj, (200*scale, 150*scale))
        screen.blit(text_obj1, (200*scale, 320*scale))
        screen.blit(text_obj2, (200*scale, 490*scale))
        screen.blit(text_obj3, (200*scale, 660*scale))
        screen.blit(text_obj4, (775*scale, 850*scale))
        
        pygame.display.flip()

        if Go_back.clicked():
            self.state = 'Choice_Scene'
            
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
    def Show_Inv_Scene(self):
        
        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        background_Width = bakgrund.get_width() *scale
        background_Height = bakgrund.get_height() *scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        text_obj4 = Font6_70.render("Go back", True, Dark_Grey)
        
        Go_back = Button(730*scale, 880*scale, Button1_image, 0.8)
    
        inventory = self.spelare.inventory
        
        Item1_Bild = pygame.image.load(f"Bilder/{inventory[0].image}.png")
        Item1 = pygame.transform.scale(Item1_Bild, (120*scale, 120*scale))
        Item2_Bild = pygame.image.load(f"Bilder/{inventory[1].image}.png")
        Item2 = pygame.transform.scale(Item2_Bild, (120*scale, 120*scale))
        Item3_Bild = pygame.image.load(f"Bilder/{inventory[2].image}.png")
        Item3 = pygame.transform.scale(Item3_Bild, (120*scale, 120*scale))
        Item4_Bild = pygame.image.load(f"Bilder/{inventory[3].image}.png")
        Item4 = pygame.transform.scale(Item4_Bild, (120*scale, 120*scale))
        Item5_Bild = pygame.image.load(f"Bilder/{inventory[4].image}.png")
        Item5 = pygame.transform.scale(Item5_Bild, (120*scale, 120*scale))
        
        Item1_text = Font6_35.render(f" Name: {inventory[0].Name}, Description: {inventory[0].Description}",True,White)
        Item2_text = Font6_35.render(f" Name: {inventory[1].Name}, Description: {inventory[1].Description}",True,White)
        Item3_text = Font6_35.render(f" Name: {inventory[2].Name}, Description: {inventory[2].Description}",True,White)
        Item4_text = Font6_35.render(f" Name: {inventory[3].Name}, Description: {inventory[3].Description}",True,White)
        Item5_text = Font6_35.render(f" Name: {inventory[4].Name}, Description: {inventory[4].Description}",True,White)
        
        Str_text1 = Font6_25.render(f" Strength: {inventory[0].Strength}",True,Red)
        Str_text2 = Font6_25.render(f" Strength: {inventory[1].Strength}",True,Red)
        Str_text3 = Font6_25.render(f" Strength: {inventory[2].Strength}",True,Red)
        Str_text4 = Font6_25.render(f" Strength: {inventory[3].Strength}",True,Red)
        Str_text5 = Font6_25.render(f" Strength: {inventory[4].Strength}",True,Red)
        
        
        screen.blit(bakgrund, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (50*scale, 50*scale,1820*scale, 980*scale,))
        Go_back.draw(screen)
        screen.blit(text_obj4, (775*scale, 880*scale))
        
        screen.blit(Item1, (100*scale, 100*scale))
        screen.blit(Item2, (100*scale, 250*scale))
        screen.blit(Item3, (100*scale, 400*scale))
        screen.blit(Item4, (100*scale, 550*scale))
        screen.blit(Item5, (100*scale, 700*scale))
        
        screen.blit(Item1_text, (250*scale, 100*scale))
        screen.blit(Item2_text, (250*scale, 250*scale))
        screen.blit(Item3_text, (250*scale, 400*scale))
        screen.blit(Item4_text, (250*scale, 550*scale))
        screen.blit(Item5_text, (250*scale, 700*scale))
        
        screen.blit(Str_text1, (250*scale, 150*scale))
        screen.blit(Str_text2, (250*scale, 300*scale))
        screen.blit(Str_text3, (250*scale, 450*scale))
        screen.blit(Str_text4, (250*scale, 600*scale))
        screen.blit(Str_text5, (250*scale, 750*scale))
       
           
        #Item1_Button.draw(screen)
        #Item2_Button.draw(screen)
        #Item3_Button.draw(screen)
        #Item4_Button.draw(screen)
        #Item5_Button.draw(screen) 
        
        pygame.display.flip()
                    
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Go_back.clicked():
            self.state = 'Choice_Scene'
                  
    def Door_Choice_Scene(self):
        from Game_State import game_state
                        
        Background = pygame.image.load("renders/Färdigt/Tre dörrar v3- oilpaint.png")
        background_Width = Background.get_width() *scale
        background_Height = Background.get_height() *scale
        Background = pygame.transform.scale(Background, (background_Width, background_Height))
        
        Door1 = pygame.image.load("Bilder/dörrknapp1.png")
        Door2 = pygame.image.load("Bilder/dörrknapp2.png")
        door3 = pygame.image.load("Bilder/dörrknapp3.png")

        Door1_Button = Button(1458*scale, 235*scale, Door1, 1)   
        Door2_Button = Button(695*scale, 320*scale, Door2, 1) 
        Door3_Button = Button(145*scale, 270*scale, door3, 1)
        
        text_obj3 = Font1_100.render("Where do you want to go? Pick a door!",True,Dark_Grey)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, 75*scale))
            
        if Door1_Button.clicked():
            self.spelare.Choice(3)
        if Door2_Button.clicked():
            self.spelare.Choice(3)
        if Door3_Button.clicked():
            self.spelare.Choice(3)
        
        screen.blit(Background,(0,0))
        
        Door1_Button.draw(screen)
        Door2_Button.draw(screen)
        Door3_Button.draw(screen)
        screen.blit(text_obj3, text_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def Monster_Scene(self):
        
        Monster1 = pygame.image.load("renders/Färdigt/spindel - oilpaint.png")
        background_Width = Monster1.get_width() *scale
        background_Height = Monster1.get_height() *scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))

        screen.blit(Monster1, (0, 0))
        pygame.display.flip()
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        time.sleep(1.5)
        self.spelare.monster()

    def Win_Scene(self):
        Monster1 = pygame.image.load("renders/Färdigt/spindel - död - oilpaint.png")
        background_Width = Monster1.get_width() *scale
        background_Height = Monster1.get_height() *scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))

        image1 = pygame.image.load("Bilder/Knapp.png")
        Return_Button = Button(100, 400, image1, 0.1)  
        
        screen.blit(Monster1, (0, 0))
        
        Return_Button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Return_Button.clicked():
            self.state = 'Choice_Scene'
            
    def Lose_Scene(self):
        
        Monster1 = pygame.image.load("renders/Färdigt/spindel du dog - oilpaint.png")
        background_Width = Monster1.get_width() *scale
        background_Height = Monster1.get_height() *scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))
        
        image1 = pygame.image.load("Bilder/continue.png")
        Return_Button = Button(100, 400, image1,0.1)
            
        screen.blit(Monster1, (0, 0))
        Return_Button.draw(screen)
        pygame.display.flip()
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Return_Button.clicked():
            self.state = 'Choice_Scene'

    def Draw_Scene(self):
        
        Monster1 = pygame.image.load("renders/Färdigt/spindel - tie - oilpaint.png")
        background_Width = Monster1.get_width() *scale
        background_Height = Monster1.get_height() *scale
        Monster1 = pygame.transform.scale(Monster1, (background_Width, background_Height))
        
        background = pygame.image.load("Bilder/lika.png")
        image1 = pygame.image.load("Bilder/Knapp.png")
        Return_Button = Button(100, 400, image1, 0.1)
         
        screen.blit(Monster1, (0, 0))
        screen.blit(background,(0,0))
        Return_Button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Return_Button.clicked():
            self.state = 'Choice_Scene'
       
    def Trap_Scene(self):
        
        Trap = pygame.image.load("renders/Färdigt/Trap1 - oilpaint.png")
        background_Width = Trap.get_width() *scale
        background_Height = Trap.get_height() *scale
        Trap = pygame.transform.scale(Trap, (background_Width, background_Height))
        
        screen.blit(Trap, (0,0))
        pygame.display.flip()
        
        time.sleep(1.5)
        if self.spelare.dodge_trap == True:
            self.state = 'Dodge_Trap_Scene'
        else:
            self.state = 'Fall_For_Trap_Scene' 
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def Dodge_Trap_Scene(self):
        Trap = pygame.image.load("renders/Färdigt/Trap1 - dodge - oilpaint.png")
        background_Width = Trap.get_width() *scale
        background_Height = Trap.get_height() *scale
        Trap = pygame.transform.scale(Trap, (background_Width, background_Height))
        
        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(1000*scale, 800*scale, Continue_Button, 1)
        
        screen.blit(Trap, (0,0))
        Continue_Button.draw(screen)       
        pygame.display.flip()
            
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def Fall_For_Trap_Scene(self):
        Trap = pygame.image.load("renders/Färdigt/Trap1 du dog - oilpaint.png")
        background_Width = Trap.get_width() *scale
        background_Height = Trap.get_height() *scale
        Trap = pygame.transform.scale(Trap, (background_Width, background_Height))    
         
        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(1000*scale, 800*scale, Continue_Button, 1)
        
        screen.blit(Trap, (0,0))
        Continue_Button.draw(screen)
        pygame.display.flip()
       
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if Continue_Button.clicked():
            self.state = 'Choice_Scene'
         
    def Chest_Scene(self):

        font_obj3 = pygame.font.Font("Fonts/Font1.TTF", int(100 *scale))
        text_obj3 = font_obj3.render("Press the chest to open it",True,Gray)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, 150*scale))

        Chest = pygame.image.load("renders/Färdigt/Kista - stängd - oilpaint.png")
        background_Width = Chest.get_width() *scale
        background_Height = Chest.get_height() *scale
        Chest = pygame.transform.scale(Chest, (background_Width, background_Height))

        Chest_Button = pygame.image.load("Bilder/kistknapp.png")
        Chest_Button = Button(700*scale, 440*scale, Chest_Button, 1)
        
        screen.blit(Chest, (0, 0))
        Chest_Button.draw(screen)
        draw_rect_alpha(screen, (0, 0, 0, 100), (410*scale, 90*scale,1100*scale, 120*scale,))
        screen.blit(text_obj3,text_rect)
        pygame.display.flip()
        
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Chest_Button.clicked():
            
            self.spelare.Chest()
            self.found_item = self.spelare.current_item
            self.state = 'Chest_Scene_Open'

    def Chest_Scene_Open(self):
        
        Open_Chest = pygame.image.load("renders/Färdigt/Kista - öppen - oilpaint.png")
        background_Width = Open_Chest.get_width() *scale
        background_Height = Open_Chest.get_height() *scale
        Open_Chest = pygame.transform.scale(Open_Chest, (background_Width, background_Height)) 
        
        text_obj3 = Font1_100.render("You opened the chest and found:",True,Gray)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, 170*scale))
        
        if self.spelare.chest_gold == True:

            text_obj4 = Font1_70.render(f"{self.found_item} Gold",True,Gray)
            text_rect1 = text_obj4.get_rect(center = (screen_Width//2, 300*scale))

            item = pygame.image.load(f"Bilder/GULD.png")
            item_Width = item.get_width() *scale
            item_Height = item.get_height() *scale
            item = pygame.transform.scale(item, (item_Width, item_Height))
            print (self.spelare.gold)

        else:
           
            text_obj4 = Font1_70.render(self.found_item.Name,True,Gray)
            text_rect1 = text_obj4.get_rect(center = (screen_Width//2, 300*scale))

            item = pygame.image.load(f"Bilder/{self.found_item.image}.png")
            item_Width = item.get_width() *scale
            item_Height = item.get_height() *scale
            item = pygame.transform.scale(item, (item_Width, item_Height)) 

        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(910*scale, 800*scale, Continue_Button, 1)
        
        
        screen.blit(Open_Chest, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (310*scale, 90*scale,1300*scale, 900*scale,))
        screen.blit(text_obj3,text_rect)
        screen.blit(text_obj4,text_rect1)
        screen.blit(item, (screen_Width//2-item_Width/2, 500*scale))
        Continue_Button.draw(screen)
        
        pygame.display.flip()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Continue_Button.clicked():
            
            if self.spelare.inv_full == True and self.spelare.chest_gold == False:
                self.state = 'Item_manager'
            else:
                self.state = "Choice_Scene"         
    
    def Item_manager(self):

        
        if self.spelare.shop == False:
            Open_Chest = pygame.image.load("renders/Färdigt/Kista - öppen - oilpaint.png")
            background_Width = Open_Chest.get_width() *scale
            background_Height = Open_Chest.get_height() *scale
            Open_Chest = pygame.transform.scale(Open_Chest, (background_Width, background_Height))
            screen.blit(Open_Chest, (0, 0))
        else:
            Shop = pygame.image.load("renders/Färdigt/Shop - oilpaint.png")
            background_Width = Shop.get_width() *scale
            background_Height = Shop.get_height() *scale
            Shop = pygame.transform.scale(Shop, (background_Width, background_Height))
            screen.blit(Shop, (0, 0))
        
        draw_rect_alpha(screen, (0, 0, 0, 100), (310*scale, 90*scale,1300*scale, 900*scale,))
        
        inventory = self.spelare.inventory

        Item1_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[0].image}.png")
        Item2_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[1].image}.png")
        Item3_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[2].image}.png")
        Item4_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[3].image}.png")
        Item5_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[4].image}.png")

        Item1_Button = Button(100*scale, 800*scale, Item1_Bild, 1)
        Item2_Button = Button(500*scale, 800*scale, Item2_Bild, 1)
        Item3_Button = Button(900*scale, 800*scale, Item3_Bild, 1)
        Item4_Button = Button(1300*scale, 800*scale, Item4_Bild, 1)
        Item5_Button = Button(1700*scale, 800*scale, Item5_Bild, 1)

        Item1_Button.draw(screen)
        Item2_Button.draw(screen)
        Item3_Button.draw(screen)
        Item4_Button.draw(screen)
        Item5_Button.draw(screen)

        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(910*scale, 300*scale, Continue_Button, 1)
        Continue_Button.draw(screen)

        pygame.display.flip()

        if Item1_Button.clicked():
            self.spelare.inv_change(0)
            
        if Item2_Button.clicked():
            self.spelare.inv_change(1)

        if Item3_Button.clicked():
            self.spelare.inv_change(2)

        if Item4_Button.clicked():
            self.spelare.inv_change(3)

        if Item5_Button.clicked():
            self.spelare.inv_change(4)

        if Continue_Button.clicked():
            self.state = 'Choice_Scene'
        
        

                    
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def Shop_Scene(self):
        
        bakgrund = pygame.image.load("renders/Färdigt/Shop - oilpaint.png")
        background_Width = bakgrund.get_width() *scale
        background_Height = bakgrund.get_height() *scale
        bakgrund = pygame.transform.scale(bakgrund, (background_Width, background_Height))
        
        font_obj = pygame.font.Font("Fonts/Font1.ttf", int(100*scale))
        font_obj1 = pygame.font.Font("Fonts/Font6.ttf", int(70 *scale))
        font_obj2 = pygame.font.Font("Fonts/Font6.ttf", int(35 *scale))
        font_obj3 = pygame.font.Font("Fonts/Font6.ttf", int(25 *scale))
       
        Item1_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[0].image}.png")
        Item1 = pygame.transform.scale(Item1_Bild, (120*scale, 120*scale))

        Item2_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[1].image}.png")
        Item2 = pygame.transform.scale(Item2_Bild, (120*scale, 120*scale))

        Item3_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[2].image}.png")
        Item3 = pygame.transform.scale(Item3_Bild, (120*scale, 120*scale))

        Item4_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[3].image}.png")
        Item4 = pygame.transform.scale(Item4_Bild, (120*scale, 120*scale))

        item1 = Button(300*scale, 400*scale, Item1, 1)
        item2 = Button(650*scale, 400*scale, Item2, 1)
        item3 = Button(1150*scale, 400*scale, Item3, 1)
        item4 = Button(1480*scale, 400*scale, Item4, 1)
        
        Go_back = Button(730*scale, 880*scale, Button1_image, 0.8)
        
        Item1_text = font_obj3.render(f" Name: {self.spelare.Shop_List[0].Name}, Description: {self.spelare.Shop_List[0].Description}",True,White)
        Item2_text = font_obj3.render(f" Name: {self.spelare.Shop_List[1].Name}, Description: {self.spelare.Shop_List[1].Description}",True,White)
        Item3_text = font_obj3.render(f" Name: {self.spelare.Shop_List[2].Name}, Description: {self.spelare.Shop_List[2].Description}",True,White)
        Item4_text = font_obj3.render(f" Name: {self.spelare.Shop_List[3].Name}, Description: {self.spelare.Shop_List[3].Description}",True,White)
        
        Str_text1 = font_obj3.render(f" Strength: {self.spelare.Shop_List[0].Strength}",True,Red)
        Str_text2 = font_obj3.render(f" Strength: {self.spelare.Shop_List[1].Strength}",True,Red)
        Str_text3 = font_obj3.render(f" Strength: {self.spelare.Shop_List[2].Strength}",True,Red)
        Str_text4 = font_obj3.render(f" Strength: {self.spelare.Shop_List[3].Strength}",True,Red)

        Title = font_obj.render("Shop", True, Gray)
        Title_center = Title.get_rect(center = (screen_Width/2, 150*scale))

        gold_ammount = font_obj2.render("Gold: ", True, Gold)
        
        screen.blit(bakgrund, (0, 0))
        screen.blit(Title, Title_center)
        draw_rect_alpha(screen, (0, 0, 0, 100), (760*scale, 85*scale,400*scale, 125*scale,))

        if item1.hover():
            draw_rect_alpha(screen, (0, 0, 0, 150), (130*scale, 400*scale,450*scale, 300*scale,))
            screen.blit(Item1_text, (250*scale, 100*scale))
            screen.blit(Str_text1, (250*scale, 150*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (280*scale, 400*scale,160*scale, 160*scale,))  

        if item2.hover():
            draw_rect_alpha(screen, (0, 0, 0, 150), (480*scale, 400*scale,450*scale, 300*scale,))
            screen.blit(Item2_text, (250*scale, 250*scale))
            screen.blit(Str_text2, (250*scale, 300*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (630*scale, 400*scale,160*scale, 160*scale,))

        if item3.hover(): 
            draw_rect_alpha(screen, (0, 0, 0, 150), (980*scale, 400*scale,450*scale, 300*scale,)) 
            screen.blit(Item3_text, (250*scale, 400*scale))
            screen.blit(Str_text3, (250*scale, 450*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (1130*scale, 400*scale,160*scale, 160*scale,))

        if item4.hover():
            draw_rect_alpha(screen, (0, 0, 0, 150), (1310*scale, 400*scale,450*scale, 300*scale,))
            screen.blit(Item4_text, (250*scale, 550*scale))
            screen.blit(Str_text4, (250*scale, 600*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (1460*scale, 400*scale,160*scale, 160*scale,))


        
        if item1.clicked():   
            
            if self.spelare.Shop_List[0].Name != "no":
                self.spelare.Buy_item(self.spelare.Shop_List[0], 0)
            
            if self.spelare.can_afford == False:
                print("du har inte tillräckligt med pengar") # adda nån text då obviously

        if item2.clicked():   
            
            if self.spelare.Shop_List[1].Name != "no":
                self.spelare.Buy_item(self.spelare.Shop_List[1], 1)
            
            if self.spelare.can_afford == False:
                print("du har inte tillräckligt med pengar")# adda nån text då obviously
                
        if item3.clicked():   
            
            if self.spelare.Shop_List[2].Name != "no":
                self.spelare.Buy_item(self.spelare.Shop_List[2], 2)
            
            if self.spelare.can_afford == False:
                print("du har inte tillräckligt med pengar")# adda nån text då obviously

        if item4.clicked():   
            
            if self.spelare.Shop_List[3].Name != "no":
                self.spelare.Buy_item(self.spelare.Shop_List[3], 3)
            
            if self.spelare.can_afford == False:
                print("du har inte tillräckligt med pengar")# adda nån text då obviously

        if Go_back.clicked():
            self.state = "Choice_Scene"
        
        item1.draw(screen)
        item2.draw(screen)
        item3.draw(screen)
        item4.draw(screen)
        Go_back.draw(screen)
    
        pygame.display.flip()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #if Continue_Button.clicked():
            self.state = 'Choice_Scene'  
                   
    def Game_Over_Scene(self):
        from Class_Item import Empty
        self.spelare.Hp = 100
        self.spelare.Str = 200
        self.spelare.lvl = 1
        self.spelare.intelligence = 100
        self.spelare.inventory = [Empty, Empty, Empty, Empty, Empty]
        
        Continue_Button = pygame.image.load("Bilder/continue.png")
        Continue_Button = Button(1000*scale, 800*scale, Continue_Button, 1)
        
        Exit = pygame.image.load("Bilder/continue.png")
        Exit_Button = Button(710*scale, 800*scale, Exit, 1)
        

        font_color = (255, 255, 255)  
        font_obj = pygame.font.Font("Fonts/Font1.TTF",int(120*scale))
        text_obj = font_obj.render("Du är stendöd",True,font_color)
        text_rect = text_obj.get_rect(center = (screen_Width//2, screen_Height//2))

        screen.fill((0,0,0))
        Continue_Button.draw(screen)
        Exit_Button.draw(screen)
        screen.blit(text_obj, text_rect)
        pygame.display.flip()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if Continue_Button.clicked():
            self.state = 'Titlecard'
        if Exit_Button.clicked():
            pygame.quit()
            sys.exit()

    def state_manager(self):
       
        for event in pygame.event.get(pygame.QUIT):  
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
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
                       