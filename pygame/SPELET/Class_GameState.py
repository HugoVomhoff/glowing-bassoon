import pygame
import time
import sys
from Class_Button import Button
from Variabler import draw_rect_alpha, fonts

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_Width, screen_Height = pygame.display.get_surface().get_size()
scale = screen_Width / 1920

# Fonts
font1, font2, Font1_30, Font1_70, Font1_100, Font1_120, Font6_20, Font6_25, Font6_35, Font6_55, Font6_70, Font6_80 = fonts

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
image_Height = Button1_image.get_height() * scale

image_Width1 = Button_image.get_width() *scale
image_Height1 = Button_image.get_height() * scale

class GameState(): 
    
    def __init__(self, spelare):
       
        self.state = 'Titlecard'
        self.spelare = spelare
        self.cannot_afford = False
        self.count = 0

    def Titlecard(self): #klar ish , behövs bakgrund
          
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
                  
    def Difficulty_Scene(self): #klar ish, behövs bakgrund

        text_obj3 = Font1_120.render("Choose Difficulty",True,White)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, screen_Height//2-190*scale))
       
        L_button = Button((1*(screen_Width-(image_Width*3))/(4)), 500*scale, Button1_image,1)
        N_button = Button((2*(screen_Width-(image_Width*3))/(4)+ image_Width), 500*scale, Button1_image, 1)
        S_button = Button((3*(screen_Width-(image_Width*3))/(4)+ 2* image_Width), 500*scale ,Button1_image,1)
        
        Easy = Font6_80.render("Easy", True, Dark_Grey)
        Normal = Font6_80.render("Normal", True, Dark_Grey)
        Hard = Font6_80.render("Hard", True, Dark_Grey)
        
        screen.fill((0, 0, 0))
        screen.blit(text_obj3,text_rect)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((screen_Width/2-(600*scale)), (screen_Height/2-(275*scale)), int(1200*scale), int(175*scale)), int(5*scale))

        S_button.draw(screen) 
        N_button.draw(screen)
        L_button.draw(screen)

        screen.blit(Easy,(1*(screen_Width-(image_Width*3))/(4)+ 40*scale, 500*scale))
        screen.blit(Normal,(2*(screen_Width-(image_Width*3))/(4) + image_Width + 40*scale ,500*scale))
        screen.blit(Hard,(3*(screen_Width-(image_Width*3))/(4) + 2* image_Width + 40*scale, 500*scale))
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
    
    def Choice_Scene(self): #klar

        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        bakgrund = pygame.transform.scale(bakgrund, (screen_Width, screen_Height))
        
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

    def Show_Stats_Scene(self): #klar

        bakgrund = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        bakgrund1 = pygame.transform.scale(bakgrund, (screen_Width, screen_Height))
        
        Character = pygame.image.load("renders/Färdigt/Character - oilpaint.png")
        background_Width = Character.get_width() * scale * 0.9
        background_Height = Character.get_height() * scale * 0.9
        Character = pygame.transform.scale(Character, (background_Width, background_Height))

        Health_text = Font1_70.render(f"Health : {self.spelare.Hp}",True,Red)
        Str_text = Font1_70.render(f"Strength : {self.spelare.Str}",True,Purple)
        Level_text = Font1_70.render(f"Level : {self.spelare.lvl}",True,Green)        
        Intelligence_text = Font1_70.render(f"Intelligence : {self.spelare.intelligence}",True,Yellow)
        Gold_text = Font1_70.render(f"Gold : {self.spelare.gold}", True, Gold)

        Return_text= Font6_70.render("Go back", True, Dark_Grey)
        Return_button = Button(730*scale, 850*scale, Button1_image, 0.8)

        screen.blit(bakgrund1, (0,0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (150*scale, 90*scale,1620*scale, 900*scale,))
        Return_button.draw(screen)
        screen.blit(Character, (1200*scale, 125*scale))
        screen.blit(Health_text, (200*scale, 150*scale))
        screen.blit(Str_text, (200*scale, 300*scale))
        screen.blit(Level_text, (200*scale, 450*scale))
        screen.blit(Intelligence_text, (200*scale, 600*scale))
        screen.blit(Gold_text, (200*scale, 750*scale))
        screen.blit(Return_text, (775*scale, 850*scale))
        
        pygame.display.flip()

        if Return_button.clicked():
            self.state = 'Choice_Scene'
            
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
    def Show_Inv_Scene(self): #klar
        
        backgrund_image = pygame.image.load("renders/Färdigt/Room1 v2 - oilpaint.png")
        backgrund = pygame.transform.scale(backgrund_image, (screen_Width, screen_Height))
        
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
        
        Item1_text = Font6_35.render(f" {inventory[0].Name},  {inventory[0].Description}",True,White)
        Item2_text = Font6_35.render(f" {inventory[1].Name},  {inventory[1].Description}",True,White)
        Item3_text = Font6_35.render(f" {inventory[2].Name},  {inventory[2].Description}",True,White)
        Item4_text = Font6_35.render(f" {inventory[3].Name},  {inventory[3].Description}",True,White)
        Item5_text = Font6_35.render(f" {inventory[4].Name},  {inventory[4].Description}",True,White)
        
        Str_text1 = Font6_25.render(f" Strength: {inventory[0].Strength}",True,Red)
        Str_text2 = Font6_25.render(f" Strength: {inventory[1].Strength}",True,Red)
        Str_text3 = Font6_25.render(f" Strength: {inventory[2].Strength}",True,Red)
        Str_text4 = Font6_25.render(f" Strength: {inventory[3].Strength}",True,Red)
        Str_text5 = Font6_25.render(f" Strength: {inventory[4].Strength}",True,Red)
        
        Int_text1 = Font6_25.render(f"Intelligence: {inventory[0].intelligence}",True,Yellow)
        Int_text2 = Font6_25.render(f"Intelligence: {inventory[1].intelligence}",True,Yellow)
        Int_text3 = Font6_25.render(f"Intelligence: {inventory[2].intelligence}",True,Yellow)
        Int_text4 = Font6_25.render(f"Intelligence: {inventory[3].intelligence}",True,Yellow)
        Int_text5 = Font6_25.render(f"Intelligence: {inventory[4].intelligence}",True,Yellow)
        
        screen.blit(backgrund, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (50*scale, 50*scale,1820*scale, 980*scale,))
        Go_back.draw(screen)
        screen.blit(text_obj4, (775*scale, 880*scale))
        
        screen.blit(Item1, (100*scale, 100*scale))
        screen.blit(Item2, (100*scale, 250*scale))
        screen.blit(Item3, (100*scale, 400*scale))
        screen.blit(Item4, (100*scale, 550*scale))
        screen.blit(Item5, (100*scale, 700*scale))
        
        if inventory[0].Name != "":
            screen.blit(Int_text1, (430*scale, 150*scale))
            screen.blit(Str_text1, (250*scale, 150*scale))
            screen.blit(Item1_text, (250*scale, 100*scale))
        if inventory[1].Name != "":
            screen.blit(Int_text2, (430*scale, 300*scale))
            screen.blit(Str_text2, (250*scale, 300*scale))
            screen.blit(Item2_text, (250*scale, 250*scale))
        if inventory[2].Name != "":
            screen.blit(Int_text3, (430*scale, 450*scale))
            screen.blit(Str_text3, (250*scale, 450*scale))
            screen.blit(Item3_text, (250*scale, 400*scale))
        if inventory[3].Name != "":
            screen.blit(Int_text4, (430*scale, 600*scale))
            screen.blit(Str_text4, (250*scale, 600*scale))
            screen.blit(Item4_text, (250*scale, 550*scale))
        if inventory[4].Name != "":
            screen.blit(Int_text5, (430*scale, 750*scale))
            screen.blit(Str_text5, (250*scale, 750*scale))
            screen.blit(Item5_text, (250*scale, 700*scale))
       
        pygame.display.flip()
                    
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Go_back.clicked():
            self.state = 'Choice_Scene'

    def Shop_Scene(self): # klar
        
        backgrund_image = pygame.image.load("renders/Färdigt/Shop - oilpaint.png")
        backgrund = pygame.transform.scale(backgrund_image, (screen_Width, screen_Height))       
       
        Item1_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[0].image}.png")
        Item2_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[1].image}.png")
        Item3_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[2].image}.png")
        Item4_Bild = pygame.image.load(f"Bilder/{self.spelare.Shop_List[3].image}.png")

        item1 = Button(300*scale, 400*scale, Item1_Bild, 0.46875)
        item2 = Button(650*scale, 400*scale, Item2_Bild, 0.46875)
        item3 = Button(1150*scale, 400*scale, Item3_Bild, 0.46875)
        item4 = Button(1480*scale, 400*scale, Item4_Bild, 0.46875)
        
        Go_back = Button(730*scale, 880*scale, Button1_image, 0.8)
        Go_back_text = Font6_70.render("Go back", True, Dark_Grey)
        
        Item1_text = Font6_35.render(f"{self.spelare.Shop_List[0].Name}",True,White)
        Item2_text = Font6_35.render(f"{self.spelare.Shop_List[1].Name}",True,White)
        Item3_text = Font6_35.render(f"{self.spelare.Shop_List[2].Name}",True,White)
        Item4_text = Font6_35.render(f"{self.spelare.Shop_List[3].Name}",True,White)
        
        Str_text1 = Font6_25.render(f"Strength: {self.spelare.Shop_List[0].Strength}",True,Red)
        Str_text2 = Font6_25.render(f"Strength: {self.spelare.Shop_List[1].Strength}",True,Red)
        Str_text3 = Font6_25.render(f"Strength: {self.spelare.Shop_List[2].Strength}",True,Red)
        Str_text4 = Font6_25.render(f"Strength: {self.spelare.Shop_List[3].Strength}",True,Red)

        Int_text1 = Font6_25.render(f"Intelligence: {self.spelare.Shop_List[0].intelligence}",True,Yellow)
        Int_text2 = Font6_25.render(f"Intelligence: {self.spelare.Shop_List[1].intelligence}",True,Yellow)
        Int_text3 = Font6_25.render(f"Intelligence: {self.spelare.Shop_List[2].intelligence}",True,Yellow)
        Int_text4 = Font6_25.render(f"Intelligence: {self.spelare.Shop_List[3].intelligence}",True,Yellow)

        Cost_text1 = Font6_25.render(f"Cost: {self.spelare.Shop_List[0].price}",True,Gold)
        Cost_text2 = Font6_25.render(f"Cost: {self.spelare.Shop_List[1].price}",True,Gold)
        Cost_text3 = Font6_25.render(f"Cost: {self.spelare.Shop_List[2].price}",True,Gold)
        Cost_text4 = Font6_25.render(f"Cost: {self.spelare.Shop_List[3].price}",True,Gold)
        
        Buy_text = Font6_25.render("Click to buy!", True, White)
        Cannot_afford_text = Font6_70.render("You don't have enough gold to buy this!", True, Gray)
        Cannot_afford_text_position = Cannot_afford_text.get_rect(center = (screen_Width/2, 300*scale))

        Title = Font1_100.render("Shop", True, Gray)
        Title_center = Title.get_rect(center = (screen_Width/2, 150*scale))

        gold_ammount = Font6_55.render(f"Gold: {self.spelare.gold} ", True, Gold)
        gold = pygame.image.load(f"Bilder/Guld.png")
        gold = pygame.transform.scale(gold, (70*scale, 70*scale))
        
        screen.blit(backgrund, (0, 0))
        screen.blit(Title, Title_center)
        draw_rect_alpha(screen, (0, 0, 0, 100), (760*scale, 85*scale,400*scale, 125*scale,))
        screen.blit(gold_ammount, (160*scale, 90*scale))
        screen.blit(gold, (70*scale, 90*scale))
        

        if item1.hover():
            draw_rect_alpha(screen, (0, 0, 0, 150), (130*scale, 400*scale,450*scale, 320*scale,))
            screen.blit(Item1_text, (200*scale, 520*scale))
            screen.blit(Str_text1, (180*scale, 580*scale))
            screen.blit(Int_text1, (350*scale, 580*scale))
            screen.blit(Cost_text1, (280*scale, 620*scale))
            screen.blit(Buy_text, (260*scale, 660*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (280*scale, 400*scale,160*scale, 160*scale,))  

        if item2.hover():
            draw_rect_alpha(screen, (0, 0, 0, 150), (480*scale, 400*scale,450*scale, 320*scale,))
            screen.blit(Item2_text, (575*scale, 520*scale))
            screen.blit(Str_text2, (525*scale, 580*scale))
            screen.blit(Int_text2, (695*scale, 580*scale))
            screen.blit(Cost_text2, (625*scale, 620*scale))
            screen.blit(Buy_text, (605*scale, 660*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (630*scale, 400*scale,160*scale, 160*scale,))

        if item3.hover(): 
            draw_rect_alpha(screen, (0, 0, 0, 150), (980*scale, 400*scale,450*scale, 320*scale,)) 
            screen.blit(Item3_text, (1080*scale, 520*scale))
            screen.blit(Str_text3, (1030*scale, 580*scale))
            screen.blit(Int_text3, (1200*scale, 580*scale))
            screen.blit(Cost_text3, (1130*scale, 620*scale))
            screen.blit(Buy_text, (1110*scale, 660*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (1130*scale, 400*scale,160*scale, 160*scale,))

        if item4.hover():
            draw_rect_alpha(screen, (0, 0, 0, 150), (1310*scale, 400*scale,450*scale, 320*scale,))
            screen.blit(Item4_text, (1455*scale, 520*scale))
            screen.blit(Str_text4, (1370*scale, 580*scale))
            screen.blit(Int_text4, (1540*scale, 580*scale))
            screen.blit(Cost_text4, (1470*scale, 620*scale))
            screen.blit(Buy_text, (1450*scale, 660*scale))
        else:
            draw_rect_alpha(screen, (0, 0, 0, 100), (1460*scale, 400*scale,160*scale, 160*scale,))

        if item1.clicked():   
            
            if self.spelare.Shop_List[0].Name != "":
                self.spelare.Buy_item(self.spelare.Shop_List[0], 0)
                self.count = 0
    
            if self.spelare.can_afford == False:
                self.cannot_afford = True

        if item2.clicked():   
            
            if self.spelare.Shop_List[1].Name != "":
                self.spelare.Buy_item(self.spelare.Shop_List[1], 1)
                self.count = 0

            if self.spelare.can_afford == False:
                self.cannot_afford = True
                
        if item3.clicked():   
            
            if self.spelare.Shop_List[2].Name != "":
                self.spelare.Buy_item(self.spelare.Shop_List[2], 2)
                self.count = 0

            if self.spelare.can_afford == False:
                self.cannot_afford = True

        if item4.clicked():   
            
            if self.spelare.Shop_List[3].Name != "":
                self.spelare.Buy_item(self.spelare.Shop_List[3], 3)
                self.count = 0

            if self.spelare.can_afford == False:
                self.cannot_afford = True
        
        if self.cannot_afford == True and self.count < 15:
                screen.blit(Cannot_afford_text,  Cannot_afford_text_position)      
                self.count += 1 
    
        if Go_back.clicked():
            self.state = "Choice_Scene"
        
        item1.draw(screen)
        item2.draw(screen)
        item3.draw(screen)
        item4.draw(screen)
        Go_back.draw(screen)
        screen.blit(Go_back_text,(740*scale, 880*scale))
    
        pygame.display.flip()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def Item_manager(self): # klar
        inventory = self.spelare.inventory

        Description = Font1_70.render("Your inventory is full,",True,Gray)
        Description2 = Font1_70.render("click on one of the",True,Gray)
        Description3 = Font1_70.render("items below to switch",True,Gray)
        Description4 = Font1_70.render("or press continue to",True,Gray)
        Description5 = Font1_70.render("throw away the bought item",True,Gray)
        Description_Bought_Item = Font1_70.render("The item you bought:", True, Gray)

        Item0_text = Font6_35.render(f"{self.spelare.current_item.Name}",True,White)
        Item1_text = Font6_35.render(f"{inventory[0].Name}",True,White)
        Item2_text = Font6_35.render(f"{inventory[1].Name}",True,White)
        Item3_text = Font6_35.render(f"{inventory[2].Name}",True,White)
        Item4_text = Font6_35.render(f"{inventory[3].Name}",True,White)
        Item5_text = Font6_35.render(f"{inventory[4].Name}",True,White)
        
        Str_text0 = Font6_25.render(f"Strength: {self.spelare.current_item.Strength}",True,Red)
        Str_text1 = Font6_25.render(f"Strength: {inventory[0].Strength}",True,Red)
        Str_text2 = Font6_25.render(f"Strength: {inventory[1].Strength}",True,Red)
        Str_text3 = Font6_25.render(f"Strength: {inventory[2].Strength}",True,Red)
        Str_text4 = Font6_25.render(f"Strength: {inventory[3].Strength}",True,Red)
        Str_text5 = Font6_25.render(f"Strength: {inventory[4].Strength}",True,Red)

        Int_text0 = Font6_25.render(f"Intelligence: {self.spelare.current_item.intelligence}", True, Yellow)
        Int_text1 = Font6_25.render(f"Intelligence: {inventory[0].intelligence}",True,Yellow)
        Int_text2 = Font6_25.render(f"Intelligence: {inventory[1].intelligence}",True,Yellow)
        Int_text3 = Font6_25.render(f"Intelligence: {inventory[2].intelligence}",True,Yellow)
        Int_text4 = Font6_25.render(f"Intelligence: {inventory[3].intelligence}",True,Yellow)
        Int_text5 = Font6_25.render(f"Intelligence: {inventory[4].intelligence}",True,Yellow)
        
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
        
        Item0 = pygame.image.load(f"renders/Default Renders/items/{self.spelare.current_item.image}.png")
        Item0_Bild = pygame.transform.scale(Item0, (179*scale, 179*scale))

        Continue_Button = Button(800*scale, 940*scale, Button1_image, 0.6)
        Continue_text = Font6_55.render("Continue", True, Dark_Grey)

        draw_rect_alpha(screen, (0, 0, 0, 100), (100*scale, 40*scale,1720*scale, 1000*scale,))

        screen.blit(Description, (200*scale,130*scale))
        screen.blit(Description2, (200*scale,210*scale))
        screen.blit(Description3, (200*scale,290*scale))
        screen.blit(Description4, (200*scale,370*scale))
        screen.blit(Description5, (200*scale,450*scale))
        screen.blit(Description_Bought_Item, (1100*scale,190*scale))

        Item1_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[0].image}.png")
        Item2_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[1].image}.png")
        Item3_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[2].image}.png")
        Item4_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[3].image}.png")
        Item5_Bild = pygame.image.load(f"renders/Default Renders/items/{inventory[4].image}.png")
        
        screen.blit(Item0_Bild, (1200*scale, 290*scale))
        Item1_Button = Button(150*scale, 600*scale, Item1_Bild, 0.7)
        Item2_Button = Button(510*scale, 600*scale, Item2_Bild, 0.7)
        Item3_Button = Button(870*scale, 600*scale, Item3_Bild, 0.7)
        Item4_Button = Button(1231*scale, 600*scale, Item4_Bild, 0.7)
        Item5_Button = Button(1591*scale, 600*scale, Item5_Bild, 0.7)
        
        screen.blit(Item0_text, (1400*scale, 300*scale))
        screen.blit(Item1_text, (125*scale, 790*scale))
        screen.blit(Item2_text, (500*scale, 790*scale))
        screen.blit(Item3_text, (880*scale, 790*scale))
        screen.blit(Item4_text, (1200*scale, 790*scale))
        screen.blit(Item5_text, (1581*scale, 790*scale))

        screen.blit(Str_text0, (1400*scale, 350*scale))
        screen.blit(Str_text1, (170*scale, 840*scale))       
        screen.blit(Str_text2, (510*scale, 840*scale))
        screen.blit(Str_text3, (870*scale, 840*scale))  
        screen.blit(Str_text4, (1230*scale, 840*scale))
        screen.blit(Str_text5, (1590*scale, 840*scale))

        screen.blit(Int_text0, (1400*scale, 390*scale))
        screen.blit(Int_text1, (170*scale, 880*scale))
        screen.blit(Int_text2, (510*scale, 880*scale))
        screen.blit(Int_text3, (870*scale, 880*scale))
        screen.blit(Int_text4, (1230*scale, 880*scale))
        screen.blit(Int_text5, (1590*scale, 880*scale))

        Item1_Button.draw(screen)
        Item2_Button.draw(screen)
        Item3_Button.draw(screen)
        Item4_Button.draw(screen)
        Item5_Button.draw(screen)
        Continue_Button.draw(screen)
        screen.blit(Continue_text, (820*scale, 940*scale))

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

    def Door_Choice_Scene(self): #klar
        from Game_State import game_state
                        
        Background_image = pygame.image.load("renders/Färdigt/Tre dörrar v3- oilpaint.png")
        Background = pygame.transform.scale(Background_image, (screen_Width, screen_Height))
        
        Door1 = pygame.image.load("Bilder/dörrknapp1.png")
        Door2 = pygame.image.load("Bilder/dörrknapp2.png")
        door3 = pygame.image.load("Bilder/dörrknapp3.png")

        Door1_Button = Button(1458*scale, 235*scale, Door1, 1)   
        Door2_Button = Button(695*scale, 320*scale, Door2, 1) 
        Door3_Button = Button(145*scale, 270*scale, door3, 1)
        
        text_obj3 = Font1_100.render("Where do you want to go? Pick a door!",True,Gray)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, 75*scale))
        
        screen.blit(Background,(0,0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (100*scale, 20*scale,1720*scale, 120*scale,))
        Door1_Button.draw(screen)
        Door2_Button.draw(screen)
        Door3_Button.draw(screen)
        screen.blit(text_obj3, text_rect)
        
        pygame.display.flip()

        if Door1_Button.clicked():
            self.spelare.Choice(3)
        if Door2_Button.clicked():
            self.spelare.Choice(3)
        if Door3_Button.clicked():
            self.spelare.Choice(3)
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def Chest_Scene(self): #klar

        font_obj3 = pygame.font.Font("Fonts/Font1.TTF", int(100 *scale))
        text_obj3 = font_obj3.render("Press the chest to open it",True,Gray)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, 150*scale))

        Chest = pygame.image.load("renders/Färdigt/Kista - stängd - oilpaint.png")
        Chest = pygame.transform.scale(Chest, (screen_Width, screen_Height))

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

    def Chest_Scene_Open(self): #klar
        
        Open_Chest = pygame.image.load("renders/Färdigt/Kista - öppen - oilpaint.png")
        Open_Chest = pygame.transform.scale(Open_Chest, (screen_Width, screen_Height)) 
        
        text_obj3 = Font1_100.render("You opened the chest and found:",True,Gray)
        text_rect = text_obj3.get_rect(center = (screen_Width//2, 170*scale))
        
        if self.spelare.chest_gold == True:

            text_obj4 = Font1_70.render(f"{self.found_item} Gold",True,Gray)
            text_rect1 = text_obj4.get_rect(center = (screen_Width//2, 300*scale))

            item = pygame.image.load(f"Bilder/GULD.png")
            item_Width = item.get_width() *scale
            item_Height = item.get_height() *scale
            item = pygame.transform.scale(item, (item_Width, item_Height))

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
                   
    def Monster_Scene(self): #klar
        
        Monster1 = pygame.image.load("renders/Färdigt/spindel - oilpaint.png")
        Bakground = pygame.transform.scale(Monster1, (screen_Width,screen_Height))

        Attack = Font6_70.render("Attack", True, Dark_Grey)
        Attack_Button = Button(800, 900 , Button1_image, 0.7)  

        screen.blit(Bakground, (0, 0))
        Attack_Button.draw(screen)
        screen.blit(Attack, (820*scale, 900*scale))
        pygame.display.flip()
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if Attack_Button.clicked():
            self.spelare.monster()

    def Win_Scene(self): #klar?
        Monster1 = pygame.image.load("renders/Färdigt/spindel - död - oilpaint.png")
        Bakground = pygame.transform.scale(Monster1, (screen_Width, screen_Height))
        
        text_obj = Font1_100.render("You slaughtered the spider",True,Gray)
        text_rect1 = text_obj.get_rect(center = (screen_Width/2, 200*scale))

        text_obj2 = Font1_100.render("and leveled up",True,Gray)
        text_rect2 = text_obj2.get_rect(center = (screen_Width/2, 325*scale))

        text_obj3 = Font1_100.render("Press the button to continue",True,Gray)
        text_rect3 = text_obj3.get_rect(center = (screen_Width/2, 450*scale))
        
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Return_Button = Button(800, 900 , Button1_image, 0.7)  
        
        screen.blit(Bakground, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 75), (50*scale, 50*scale,1820*scale, 980*scale,))
        
        Return_Button.draw(screen)
        screen.blit(text_obj, text_rect1)
        screen.blit(text_obj2, text_rect2)
        screen.blit(text_obj3, text_rect3)
        screen.blit(Continue_text, (820*scale, 900*scale))

        pygame.display.flip()

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Return_Button.clicked():
            self.state = 'Choice_Scene'
            
    def Lose_Scene(self): #klar
        
        Monster1_image = pygame.image.load("renders/Färdigt/spindel du dog - oilpaint.png")
        Monster1 = pygame.transform.scale(Monster1_image, (screen_Width, screen_Height))
        
        text_obj = Font1_100.render("You were hurt by the spider ",True,Gray)
        text_rect1 = text_obj.get_rect(center = (screen_Width/2, 200*scale))

        text_obj2 = Font1_100.render("and ran away",True,Gray)
        text_rect2 = text_obj2.get_rect(center = (screen_Width/2, 325*scale))

        text_obj3 = Font1_100.render("Press the button to continue",True,Gray)
        text_rect3 = text_obj3.get_rect(center = (screen_Width/2, 450*scale))
        
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Return_Button = Button(800, 900 , Button1_image, 0.7)  
            
        screen.blit(Monster1, (0, 0))
        Return_Button.draw(screen)
        screen.blit(text_obj, text_rect1)
        screen.blit(text_obj2, text_rect2)
        screen.blit(text_obj3, text_rect3)
        screen.blit(Continue_text, (820*scale, 900*scale))
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
        
        Return_Button = Button(100, 400, Button_image, 0.8)
         
        screen.blit(Monster1, (0, 0))
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
        Trap = pygame.transform.scale(Trap, (screen_Width, screen_Height))

        Dodge_text = Font6_70.render("Dodge", True, Dark_Grey)
        Dodge_button = Button(800, 900 , Button1_image, 0.7)  

        screen.blit(Trap, (0,0))
        Dodge_button.draw(screen)
        screen.blit(Dodge_text, (820*scale, 900*scale ))
        pygame.display.flip()
        
        if Dodge_button.clicked():
            if self.spelare.dodge_trap == True:
                self.state = 'Dodge_Trap_Scene'
            else:
                self.state = 'Fall_For_Trap_Scene' 
        
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def Dodge_Trap_Scene(self):
        Trap_image = pygame.image.load("renders/Färdigt/Trap1 - dodge - oilpaint.png")
        Trap = pygame.transform.scale(Trap, (screen_Width, screen_Height))
        
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
        Trap = pygame.transform.scale(Trap, (screen_Width, screen_Height))    
         
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
         
    def Game_Over_Scene(self):
        from Class_Item import Empty
        self.spelare.Hp = 100
        self.spelare.Str = 200
        self.spelare.lvl = 1
        self.spelare.intelligence = 100
        self.spelare.gold = 0
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
                       