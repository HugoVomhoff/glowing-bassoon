# importerar pygame och andra viktiga funktioner och variabler, exempelvis Class_Button
import pygame
import sys
from Class_Button import Button
from Variables import draw_rect_alpha, fonts, Scendetaljer

# Gör skärmen till Fullscreen, och hämtar skärmens resolution, alltså hur många pixlar skärmen har i x-led och y-led
# Gör även en variabel "Scale" som gör att man kan anpassa spelet till olika storlekar av skärmar
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_Width, screen_Height = pygame.display.get_surface().get_size()
scale = screen_Width / 1920

# Hämtar alla fonter
Font1_30, Font1_70, Font1_100, Font1_120, Font6_25, Font6_35, Font6_55, Font6_70, Font6_80 = fonts

# Font colors
Gray = (100, 100, 100)
Black = (0,0,0)
White = (255, 255, 255)
Gold = (255, 192, 0)
Dark_Grey = (10, 10, 10)
Purple = (139, 0, 139)
Yellow = (255, 255, 0)
Red = (120, 0, 0)
Green = (0, 120, 0)

# Vi imoportar bilderna som ska visas som knappar
Button_image = pygame.image.load("Bilder/Knappar/Knapp.png").convert_alpha()
Button1_image = pygame.image.load("Bilder/Knappar/Knapp1.png").convert_alpha()

# Listar ut hur stora bilderna är och anpassar de till hur stor skärmen är
image_Width = Button1_image.get_width() *scale
image_Height = Button1_image.get_height() * scale

image_Width1 = Button_image.get_width() *scale
image_Height1 = Button_image.get_height() * scale

# Sätter alla scenbakgrundrunder och detaljer
Bakgrund, Bakgrund1, Bakgrund2, Bakgrund3, Bakgrund4, Bakgrund5, Bakgrund6, Bakgrund7, Bakgrund8, Bakgrund9, Bakgrund10, Bakgrund11, Character, Character1, GULD, GULD1 = Scendetaljer


class GameState(): 
    
    def __init__(self, spelare):
        # Sätter första scenen till Titlecard och håller kvar den passade spelaren som en variabel i gamestaten
        # Sätter även variabler som ska ha ett startvärde
        
        self.state = 'Titlecard'
        self.spelare = spelare
        self.cannot_afford = False
        self.count = 0

    def Titlecard(self):
      
        # Texten sparas i variabler och ges en position
        Text1 = Font1_120.render("Dungeon Danger ",True,White)
        Text1_pos = Text1.get_rect(center = (screen_Width//2, screen_Height/2))

        Text2 = Font1_30.render("Press spacebar to continue", True, White)
        Text2_pos = Text2.get_rect(center = (screen_Width//2, screen_Height-75*scale))

        # Skärmen/bakgrunden blir svart
        screen.fill((0,0,0))
        
        # Texten ritas ut
        screen.blit(Text1, Text1_pos)
        screen.blit(Text2, Text2_pos)

        # En ram ritas ut
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((screen_Width/2-(500*scale)), (screen_Height/2-(75*scale)), int(1000*scale), int(150*scale)), int(5*scale))
        
        # Ifall man trycker på mellanslag så går man vidare till nästa scen
        if pygame.key.get_pressed()[pygame.K_SPACE] == True:
            self.state = 'Difficulty_Scene'
                  
    def Difficulty_Scene(self):
        
        # Knappar skapas med storlek baserat på given bild eller med "skalinputen"
        # Knapparna får också en position på skärmen
        L_button = Button((1*(screen_Width-(image_Width*3))/(4)), 500*scale, Button1_image,1)
        N_button = Button((2*(screen_Width-(image_Width*3))/(4)+ image_Width), 500*scale, Button1_image, 1)
        S_button = Button((3*(screen_Width-(image_Width*3))/(4)+ 2* image_Width), 500*scale ,Button1_image,1)
        
        # Text tillsammans med en font och färg sätts i en variabel
        Easy = Font6_80.render("Easy", True, Dark_Grey)
        Normal = Font6_80.render("Normal", True, Dark_Grey)
        Hard = Font6_80.render("Hard", True, Dark_Grey)

        text_obj = Font1_120.render("Choose Difficulty",True,White)
        text_rect = text_obj.get_rect(center = (screen_Width//2, screen_Height//2-190*scale))
        
        # Bakgrundsfärgen görs till svart. Texten och en ram printas ut på skärmen 
        screen.fill((0, 0, 0))
        screen.blit(text_obj,text_rect)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((screen_Width/2-(600*scale)), (screen_Height/2-(275*scale)), int(1200*scale), int(175*scale)), int(5*scale))

        # Knapparna ritas ut
        S_button.draw(screen) 
        N_button.draw(screen)
        L_button.draw(screen)

        # Texten ritas ut ovanpå de olika svårighetsgradsknapparna
        screen.blit(Easy,(1*(screen_Width-(image_Width*3))/(4)+ 40*scale, 500*scale))
        screen.blit(Normal,(2*(screen_Width-(image_Width*3))/(4) + image_Width + 40*scale ,500*scale))
        screen.blit(Hard,(3*(screen_Width-(image_Width*3))/(4) + 2* image_Width + 40*scale, 500*scale))
        
        # Ifall en av knapparna trycks ned blir svårighetsgraden satt och scenen byts
        if L_button.clicked():
            self.spelare.Set_Difficulty(1)
            self.state = 'Choice_Scene'

        if N_button.clicked():
            self.spelare.Set_Difficulty(2)
            self.state = 'Choice_Scene'

        if S_button.clicked():
            self.spelare.Set_Difficulty(3)
            self.state = 'Choice_Scene'    
    
    def Choice_Scene(self): 

        # Text tillsammans med en font och färg sätts i en variabel
        text_obj = Font1_100.render("Choose Your Action",True,Gray)
        text_rect = text_obj.get_rect(center = (screen_Width/2, 150*scale))

        # Knappar skapas med en bild och mer textvariabler skapas på samma sätt som ovan
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
        
        # Bakgrunden och en semitransparent rektangel ritas ut
        screen.blit(Bakgrund, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (510*scale, 85*scale,900*scale, 120*scale,))
        
        # Knapparnas bilder och texter ritas ut
        Exit_Button.draw(screen)
        Stats_Button.draw(screen)
        Inventory_Button.draw(screen)
        Äventyr_Button.draw(screen)
        Shop_button.draw(screen)       
        screen.blit(text_obj,text_rect)
        screen.blit(text_äventyr1,((125*scale+image_Width*0.05), (1*(screen_Height-(image_Height*6.5))/(7.5)+ 2 * image_Height)))
        screen.blit(text_inventory,((125*scale+image_Width*0.05), (2*(screen_Height-(image_Height*6.5))/(7.5)+ 3 * image_Height)))
        screen.blit(text_stats,((125*scale+image_Width*0.05), (3*(screen_Height-(image_Height*6.5))/(7.5)+ 4 * image_Height)))
        screen.blit(text_shop,((125*scale+image_Width*0.05), (4*(screen_Height-(image_Height*6.5))/(7.5)+ 5 * image_Height)))
        screen.blit(Exit_game,((125*scale+image_Width*0.05), (5*(screen_Height-(image_Height*6.5))/(7.5)+ 6 * image_Height)))
        
        # Baserat på vilken knapp man klickar på så blir man kastad till olika scener
        # T.ex om man klickar på shopknappen så hamnar man i shopscenen
        if Stats_Button.clicked():
            self.spelare.Choice(1)

        if Inventory_Button.clicked():
            self.spelare.Choice(2)

        if Äventyr_Button.clicked():
            self.state = 'Door_Choice_Scene' 

        if Shop_button.clicked():
            self.state = 'Shop_Scene'
        
        # Ifall knappen trycks ned avslutas spelet
        if Exit_Button.clicked():
            pygame.quit()
            sys.exit()

    def Show_Stats_Scene(self):

        # Texter sätts i variabler 
        Health_text = Font1_70.render(f"Health : {self.spelare.Hp}",True,Red)
        Str_text = Font1_70.render(f"Strength : {self.spelare.Str}",True,Purple)
        Level_text = Font1_70.render(f"Level : {self.spelare.lvl}",True,Green)        
        Intelligence_text = Font1_70.render(f"Intelligence : {self.spelare.intelligence}",True,Yellow)
        Gold_text = Font1_70.render(f"Gold : {self.spelare.gold}", True, Gold)

        # En knapp skapas med en tillhörande text
        Return_text = Font6_70.render("Go back", True, Dark_Grey)
        Return_button = Button(730*scale, 850*scale, Button1_image, 0.8)

        # Bakgrunden sätts till en bild, en svart transparent ruta skapas och allting ritas ut på skärmen
        screen.blit(Bakgrund, (0,0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (150*scale, 90*scale,1620*scale, 900*scale,))
        Return_button.draw(screen)
        screen.blit(Character1, (1200*scale, 125*scale))
        screen.blit(Health_text, (200*scale, 150*scale))
        screen.blit(Str_text, (200*scale, 300*scale))
        screen.blit(Level_text, (200*scale, 450*scale))
        screen.blit(Intelligence_text, (200*scale, 600*scale))
        screen.blit(Gold_text, (200*scale, 750*scale))
        screen.blit(Return_text, (775*scale, 850*scale))
        
        
        # Om du klickar på knappen så hamnar du på scenen innan (choicescenen)
        if Return_button.clicked():
            self.state = 'Choice_Scene'
        
        # Om du klickar på escape hamnar du också på scenen innan (choicescenen)
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
            self.state = 'Choice_Scene'
        
    def Show_Inv_Scene(self):
        
        # En text sätts
        text_obj4 = Font6_70.render("Go back", True, Dark_Grey)
        
        # En gå tillbakaknapp skapas
        Go_back = Button(730*scale, 880*scale, Button1_image, 0.8)
        
        # Spelarens inventory sparas i en ny variabel bara för att korta ner raderna lite
        inventory = self.spelare.inventory
        
        # Bilder laddas in baserat på vad man har i inventoriet
        Item1_Bild = pygame.image.load(inventory[0].image)
        Item1 = pygame.transform.scale(Item1_Bild, (120*scale, 120*scale))
        Item2_Bild = pygame.image.load(inventory[1].image)
        Item2 = pygame.transform.scale(Item2_Bild, (120*scale, 120*scale))
        Item3_Bild = pygame.image.load(inventory[2].image)
        Item3 = pygame.transform.scale(Item3_Bild, (120*scale, 120*scale))
        Item4_Bild = pygame.image.load(inventory[3].image)
        Item4 = pygame.transform.scale(Item4_Bild, (120*scale, 120*scale))
        Item5_Bild = pygame.image.load(inventory[4].image)
        Item5 = pygame.transform.scale(Item5_Bild, (120*scale, 120*scale))
        
        # Texter sätts med itemnamnen och deras beskrivning
        Item1_text = Font6_35.render(f" {inventory[0].Name},  {inventory[0].Description}",True,White)
        Item2_text = Font6_35.render(f" {inventory[1].Name},  {inventory[1].Description}",True,White)
        Item3_text = Font6_35.render(f" {inventory[2].Name},  {inventory[2].Description}",True,White)
        Item4_text = Font6_35.render(f" {inventory[3].Name},  {inventory[3].Description}",True,White)
        Item5_text = Font6_35.render(f" {inventory[4].Name},  {inventory[4].Description}",True,White)
        
        # Texter sätts med itemstyrkan
        Str_text1 = Font6_25.render(f" Strength: {inventory[0].Strength}",True,Red)
        Str_text2 = Font6_25.render(f" Strength: {inventory[1].Strength}",True,Red)
        Str_text3 = Font6_25.render(f" Strength: {inventory[2].Strength}",True,Red)
        Str_text4 = Font6_25.render(f" Strength: {inventory[3].Strength}",True,Red)
        Str_text5 = Font6_25.render(f" Strength: {inventory[4].Strength}",True,Red)
        
        #Texter sätts med itemintelligensen
        Int_text1 = Font6_25.render(f"Intelligence: {inventory[0].intelligence}",True,Yellow)
        Int_text2 = Font6_25.render(f"Intelligence: {inventory[1].intelligence}",True,Yellow)
        Int_text3 = Font6_25.render(f"Intelligence: {inventory[2].intelligence}",True,Yellow)
        Int_text4 = Font6_25.render(f"Intelligence: {inventory[3].intelligence}",True,Yellow)
        Int_text5 = Font6_25.render(f"Intelligence: {inventory[4].intelligence}",True,Yellow)
        
        # Bakgrundsbilden målas ut, en halvtransparent svart ruta målas ovanpå det, knappar målas ut
        # och slutligen målas texter ut ovanpå dem
        screen.blit(Bakgrund, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 100), (50*scale, 50*scale,1820*scale, 980*scale,))
        Go_back.draw(screen)
        screen.blit(text_obj4, (775*scale, 880*scale))
        
        screen.blit(Item1, (100*scale, 100*scale))
        screen.blit(Item2, (100*scale, 250*scale))
        screen.blit(Item3, (100*scale, 400*scale))
        screen.blit(Item4, (100*scale, 550*scale))
        screen.blit(Item5, (100*scale, 700*scale))
        
        # Om har ett item på given plats i inventoriet så ritas egenskaperna ut, om du inte har ett item 
        # på den platsen så ritas inte egenskaperna ut
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


        # Precis som innan så kan du backa till scenen innan (choicescenen) om man klickar antingen på
        # knappen på skärmen eller escape
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
            self.state = 'Choice_Scene'

        if Go_back.clicked():
            self.state = 'Choice_Scene'

    def Shop_Scene(self):  
       
        # De olika itemsen som ska gå att köpa i shopens bilder laddas in och sätts i variabler
        Item1_Bild = pygame.image.load(self.spelare.Shop_List[0].image)
        Item2_Bild = pygame.image.load(self.spelare.Shop_List[1].image)
        Item3_Bild = pygame.image.load(self.spelare.Shop_List[2].image)
        Item4_Bild = pygame.image.load(self.spelare.Shop_List[3].image)

        # Knappar med bilder på itemsen sätts
        item1 = Button(300*scale, 400*scale, Item1_Bild, 0.46875)
        item2 = Button(650*scale, 400*scale, Item2_Bild, 0.46875)
        item3 = Button(1150*scale, 400*scale, Item3_Bild, 0.46875)
        item4 = Button(1480*scale, 400*scale, Item4_Bild, 0.46875)
        
        # "Gå tillbakaknappen" sätts med tillhörande text
        Go_back = Button(730*scale, 880*scale, Button1_image, 0.8)
        Go_back_text = Font6_70.render("Go back", True, Dark_Grey)

        # Itemsens namn, styrka, intelligens och kostnad sätts som text        
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
        Cannot_afford_text = Font6_70.render("fYou don't have enough gold to buy this!", True, Gray)
        Cannot_afford_text_position = Cannot_afford_text.get_rect(center = (screen_Width/2, 300*scale))

        # Scentiteln sätts som en text och positioneras
        Title = Font1_100.render("Shop", True, Gray)
        Title_center = Title.get_rect(center = (screen_Width/2, 150*scale))

        # Mängden guld sätts som en text och går en icon
        gold_ammount = Font6_55.render(f"Gold: {self.spelare.gold} ", True, Gold)
        gold = pygame.transform.scale(GULD, (70*scale, 70*scale))
        
        # Bakgrunden sätts till bild och positioneras, en semitransperent rektangel, guldiconen och alla texter ritas ut på skärmen 
        screen.blit(Bakgrund1, (0, 0))
        screen.blit(Title, Title_center)
        draw_rect_alpha(screen, (0, 0, 0, 100), (760*scale, 85*scale,400*scale, 125*scale,))
        screen.blit(gold_ammount, (160*scale, 90*scale))
        screen.blit(gold, (70*scale, 90*scale))
        
        # När man håller musen över itemet får man se dess namn, styrka, intelligens och kostnad
        # annars är det bara en semitransperant runt som syns bakom itemet
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

        # Om man klickar på ett item köps det och läggs i ditt inventory
        # ifall man inte har råd med itemet kommer en text upp som varnar spelaren om att man inte har råd
        # ifall inventoryt är fullt när man klcikar på ett item tar man sig till "item_maneger" scenen
        if item1.clicked():   
            
            # tittar först ifall det finns ett item i den "slotten"
            if self.spelare.Shop_List[0].Name != "":
                self.spelare.Buy_item(self.spelare.Shop_List[0], 0)
                self.count = 0

            # ifall spelaren inte har råd med itemet, sätts "self.cannot_afford" till True
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
        
        # Gör så att man hinner se texten som handlar om att man inte har råd
        if self.cannot_afford == True and self.count < 15:
                screen.blit(Cannot_afford_text,  Cannot_afford_text_position)      
                self.count += 1 

        # Knappar med bilder på itemsen, gå tillbakaknappen och gå tillbaka texten ritas ut på skärmen
        item1.draw(screen)
        item2.draw(screen)
        item3.draw(screen)
        item4.draw(screen)
        Go_back.draw(screen)
        screen.blit(Go_back_text,(740*scale, 880*scale))

        # Precis som innan så kan du backa till scenen innan (choicescenen) om man klickar antingen på
        # knappen på skärmen eller escape
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
            self.state = 'Choice_Scene'

        if Go_back.clicked():
            self.state = "Choice_Scene"

    def Item_manager(self):
        # Item manager 
        inventory = self.spelare.inventory
        
        # Texter som beskriver vad som händer sätts i variabler 
        Description = Font1_70.render("Your inventory is full,",True,Gray)
        Description2 = Font1_70.render("click on one of the",True,Gray)
        Description3 = Font1_70.render("items below to switch",True,Gray)
        Description4 = Font1_70.render("or press continue to",True,Gray)
        Description5 = Font1_70.render("throw away the bought item",True,Gray)
        Description_Bought_Item = Font1_70.render("The item you bought:", True, Gray)

        # Itemsens namn, styrka och intelligens sätts som text   
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
        
        # bakgrunden baseras på varifrån man kom ifrån 
        if self.spelare.shop == False:
            screen.blit(Bakgrund3, (0, 0))
        else:
            screen.blit(Bakgrund1, (0, 0))

        # "Continue"Knappen sätts med tillhörande text
        Continue_Button = Button(800*scale, 940*scale, Button1_image, 0.6)
        Continue_text = Font6_55.render("Continue", True, Dark_Grey)

        # Semitransperent rektangel ritus ut med hjälp av en defenition
        draw_rect_alpha(screen, (0, 0, 0, 100), (100*scale, 40*scale,1720*scale, 1000*scale,))

        # beskrivningstexterna ritas ut
        screen.blit(Description, (200*scale,130*scale))
        screen.blit(Description2, (200*scale,210*scale))
        screen.blit(Description3, (200*scale,290*scale))
        screen.blit(Description4, (200*scale,370*scale))
        screen.blit(Description5, (200*scale,450*scale))
        screen.blit(Description_Bought_Item, (1100*scale,190*scale))

        # Det köpta itemet bild och alla items från inventoryt bilder sätts i variiabler
        Item0 = pygame.image.load(self.spelare.current_item.image)
        Item0_Bild = pygame.transform.scale(Item0, (179*scale, 179*scale))

        Item1_Bild = pygame.image.load(inventory[0].image)
        Item2_Bild = pygame.image.load(inventory[1].image)
        Item3_Bild = pygame.image.load(inventory[2].image)
        Item4_Bild = pygame.image.load(inventory[3].image)
        Item5_Bild = pygame.image.load(inventory[4].image)

        # Inventoryts items bilder görs till knappar
        Item1_Button = Button(150*scale, 600*scale, Item1_Bild, 0.7)
        Item2_Button = Button(510*scale, 600*scale, Item2_Bild, 0.7)
        Item3_Button = Button(870*scale, 600*scale, Item3_Bild, 0.7)
        Item4_Button = Button(1231*scale, 600*scale, Item4_Bild, 0.7)
        Item5_Button = Button(1591*scale, 600*scale, Item5_Bild, 0.7)
        
        # Alla items namn, styrka och intelligens skrivs ut på skärmen på en en vald position
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

        # Alla item bilder och item knappar ritas ut
        screen.blit(Item0_Bild, (1200*scale, 290*scale))
        Item1_Button.draw(screen)
        Item2_Button.draw(screen)
        Item3_Button.draw(screen)
        Item4_Button.draw(screen)
        Item5_Button.draw(screen)

        # Ritar ut "continue" knappen och tillhörande text
        Continue_Button.draw(screen)
        screen.blit(Continue_text, (820*scale, 940*scale))

        # Ifall man klickar på en av itemknapparna byts det köpta itemet ut med itemet man klickade på
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
        
        # Ifall man klickar på continueknappen så slänger man iväg det köpta itemet och scenen ändras
        if Continue_Button.clicked():
            self.state = 'Choice_Scene'

    def Door_Choice_Scene(self):

        # Dörrbilder görs till 3 olika knappar                   
        Door1 = pygame.image.load("Bilder/Knappar/dörrknapp1.png")
        Door2 = pygame.image.load("Bilder/Knappar/dörrknapp2.png")
        door3 = pygame.image.load("Bilder/Knappar/dörrknapp3.png")

        Door1_Button = Button(1458*scale, 235*scale, Door1, 1)   
        Door2_Button = Button(695*scale, 320*scale, Door2, 1) 
        Door3_Button = Button(145*scale, 270*scale, door3, 1)
        
        # Bakgrund sätts till en bild med en vald position
        screen.blit(Bakgrund4,(0,0))

        # Scentitle med vald position och med tillhörande semitransperent rektangel ritas ut
        text_obj = Font1_100.render("Where do you want to go? Pick a door!",True,Gray)
        text_rect = text_obj.get_rect(center = (screen_Width//2, 75*scale))
        draw_rect_alpha(screen, (0, 0, 0, 100), (100*scale, 20*scale,1720*scale, 120*scale,))
        screen.blit(text_obj, text_rect)

        # Dörrknapparna ritas ut
        Door1_Button.draw(screen)
        Door2_Button.draw(screen)
        Door3_Button.draw(screen)
        
        # När man klickar på en av knappar startas Choice funktion i klassen Player
        if Door1_Button.clicked():
            self.spelare.Choice(3)
        if Door2_Button.clicked():
            self.spelare.Choice(3)
        if Door3_Button.clicked():
            self.spelare.Choice(3)

        # Backa till scenen innan (choice scene) genom att trycka på escapeknappen
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
            self.state = 'Choice_Scene'

    def Chest_Scene(self):

        # Kistknapp skapes med hjälp av en bild på en kista
        Chest_Button = pygame.image.load("Bilder/Knappar/kistknapp.png")
        Chest_Button = Button(700*scale, 440*scale, Chest_Button, 1)
        
        # Bakgrunden sätts till en vald bild och postition och ritas ut. Kistknappen ritas också ut
        screen.blit(Bakgrund2, (0, 0))
        Chest_Button.draw(screen)

        # Beskrivning med vald position sätts i variabler och ritas ut med en tillhörande semitransperent rektangel
        text_obj = Font1_100.render("Press the chest to open it",True,Gray)
        text_rect = text_obj.get_rect(center = (screen_Width//2, 150*scale))
        draw_rect_alpha(screen, (0, 0, 0, 100), (410*scale, 90*scale,1100*scale, 120*scale,))
        screen.blit(text_obj ,text_rect)
        
        # Ifall man klickar på kistknappen(kistan) startas funktionen "chest" i klassen player och scenen byts
        if Chest_Button.clicked():
            
            self.spelare.Chest()
            self.found_item = self.spelare.current_item
            self.state = 'Chest_Scene_Open'

    def Chest_Scene_Open(self):

        # Bakgrunden är en vald bils som ritas ut på vald position
        screen.blit(Bakgrund3, (0, 0))

        # text och textens position sätts i variabler och ritas sedan ut med en tillhörande semi transperent rektangel
        text_obj = Font1_100.render("You opened the chest and found:",True,Gray)
        text_rect = text_obj.get_rect(center = (screen_Width//2, 170*scale))
        draw_rect_alpha(screen, (0, 0, 0, 100), (310*scale, 90*scale,1300*scale, 900*scale,))
        screen.blit(text_obj,text_rect)

        # En forsättnings knapp med tillhörande text sätts i variabler och ritas ut
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Continue_Button = Button(800, 900 , Button1_image, 0.7)
        Continue_Button.draw(screen)
        screen.blit(Continue_text, (820*scale, 900*scale))

        # Ifall man får guld från kistan 
        if self.spelare.chest_gold == True:
            
            # Text baserad på hur mycket guld man får sätts i en variable
            # Guldiconen ritas också ut
            text_obj1 = Font1_70.render(f"{self.found_item} Gold",True,Gray)
            text_rect1 = text_obj1.get_rect(center = (screen_Width//2, 300*scale))
            screen.blit(GULD1, (screen_Width//2-(GULD.get_width()*scale)/2, 500*scale))

        else:
           
            # Text baserad på vilket item man får sätts i en variabel och får även en position
            text_obj1 = Font1_70.render(self.found_item.Name,True,Gray)
            text_rect1 = text_obj1.get_rect(center = (screen_Width//2, 300*scale))

            # Bilden på det funna itemet laddas in och ritas ut på en vald position
            item = pygame.image.load(self.found_item.image)
            item = pygame.transform.scale(item, (item.get_width() *scale, item.get_height() *scale)) 
            screen.blit(item, (screen_Width//2-(item.get_width() *scale)/2, 500*scale))

        # Texten om vad man får skrivs ut på skärmen
        screen.blit(text_obj1,text_rect1)
    
        # Ifall man klickar på continue knappen går man till 'You_Won_Scene' scenen
        # annars går man till "item manager" eller tillbaka till "choice" scenen beroende på
        if Continue_Button.clicked():
            if self.spelare.win == True:
                self.state = 'You_Won_Scene'

            elif self.spelare.inv_full == True and self.spelare.chest_gold == False:
                self.state = 'Item_manager'

            else:
                self.state = "Choice_Scene"        
                   
    def Monster_Scene(self):
        # Text med tillhörande knapp för att attackera monstret sätts i en variabel
        Attack = Font6_70.render("Attack", True, Dark_Grey)
        Attack_Button = Button(800, 900 , Button1_image, 0.7)  

        # beskrivande text om vad som händer sätts i en variabel
        text_obj = Font1_100.render("You encountered a spider!",True,Gray)
        text_rect = text_obj.get_rect(center = (screen_Width//2, 75*scale))

        # Bakgrunden ritas ut på vald position
        screen.blit(Bakgrund5, (0, 0))

        # Beskrivande texten med tillhörande semi transperent rektangel ritas ut
        screen.blit(text_obj, text_rect)
        draw_rect_alpha(screen, (0, 0, 0, 100), (350*scale, 20*scale,1220*scale, 120*scale,))
        
        # Knappen med tillhörande texten ritas ut
        Attack_Button.draw(screen)
        screen.blit(Attack, (820*scale, 900*scale))
        
        # Ifal man klickar på knappen attackerar man monstret och en defenition i klasses Player startas
        if Attack_Button.clicked():
            self.spelare.monster()

    def Win_Scene(self):
        
        # Beskrivande text med position sätts i variabler
        text_obj = Font1_100.render("You slaughtered the spider",True,Gray)
        text_rect1 = text_obj.get_rect(center = (screen_Width/2, 200*scale))

        text_obj2 = Font1_100.render("and leveled up",True,Gray)
        text_rect2 = text_obj2.get_rect(center = (screen_Width/2, 325*scale))

        text_obj3 = Font1_100.render("Press the button to continue",True,Gray)
        text_rect3 = text_obj3.get_rect(center = (screen_Width/2, 450*scale))
        
        # Knapp med tillhörande text sätts 
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Return_Button = Button(800, 900 , Button1_image, 0.7)  
        
        # Bakgrunden, Semi transperenta rektangeln, alla text och knappar ritas ut på skärmen
        screen.blit(Bakgrund7, (0, 0))
        draw_rect_alpha(screen, (0, 0, 0, 75), (50*scale, 50*scale,1820*scale, 980*scale,))
        Return_Button.draw(screen)
        screen.blit(text_obj, text_rect1)
        screen.blit(text_obj2, text_rect2)
        screen.blit(text_obj3, text_rect3)
        screen.blit(Continue_text, (820*scale, 900*scale))

        # Ifall knappen trycks ned ändras scen till "choice_scene"
        if Return_Button.clicked():
            self.state = 'Choice_Scene'
            
    def Lose_Scene(self):
        # Beskrivande texter med vald position sätts i variabler
        text_obj = Font1_100.render("You were hurt by the spider ",True,Gray)
        text_rect1 = text_obj.get_rect(center = (screen_Width/2, 200*scale))

        text_obj2 = Font1_100.render("and ran away",True,Gray)
        text_rect2 = text_obj2.get_rect(center = (screen_Width/2, 325*scale))

        text_obj3 = Font1_100.render(f"You took {self.spelare.lvl*2+5} damage!",True,Gray)
        text_rect3 = text_obj3.get_rect(center = (screen_Width/2, 450*scale))
        
        # Knapp med tillhörande text sätts
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Return_Button = Button(800, 900 , Button1_image, 0.7)  
        
        # Bakgrunden, knappen och alla texter ritas ut
        screen.blit(Bakgrund6, (0, 0))
        Return_Button.draw(screen)
        screen.blit(text_obj, text_rect1)
        screen.blit(text_obj2, text_rect2)
        screen.blit(text_obj3, text_rect3)
        screen.blit(Continue_text, (820*scale, 900*scale))
        
        # Ifall man trycker på knappen ändras scen till "choice_scene"
        if Return_Button.clicked():
            self.state = 'Choice_Scene'

    def Draw_Scene(self):
        # Beskrivande texter med vald position sätts i variabler
        text_obj = Font1_100.render("The fight was a fight",True,Gray)
        text_rect1 = text_obj.get_rect(center = (screen_Width/2, 200*scale))

        text_obj2 = Font1_100.render("and you ran away",True,Gray)
        text_rect2 = text_obj2.get_rect(center = (screen_Width/2, 325*scale))

        text_obj3 = Font1_100.render("Press the button to continue",True,Gray)
        text_rect3 = text_obj3.get_rect(center = (screen_Width/2, 450*scale))
        
        # Knapp med tillhörande text sätts
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Return_Button = Button(800, 900 , Button1_image, 0.7)  
        
        # Bakgrunden, knappen och alla texter ritas ut
        screen.blit(Bakgrund8, (0, 0))
        Return_Button.draw(screen)
        screen.blit(text_obj, text_rect1)
        screen.blit(text_obj2, text_rect2)
        screen.blit(text_obj3, text_rect3)
        screen.blit(Continue_text, (820*scale, 900*scale))

        # Ifall man trycker på knappen ändras scen till "choice_scene"
        if Return_Button.clicked():
            self.state = 'Choice_Scene'
       
    def Trap_Scene(self):
        # Knapp med tillhörande text sätts  
        Dodge_text = Font6_70.render("Dodge", True, Dark_Grey)
        Dodge_button = Button(800, 900 , Button1_image, 0.7)
        
        # Beskrivande text med vald position sätts i variabler
        SceneTitle =  Font1_100.render("You encountered a rolling boulder, try to dodge!",True,Gray)
        text_rect = SceneTitle.get_rect(center = (screen_Width//2, 155*scale))  

        # Bakgrunden, knappen, semi transperanterenta och alla texter ritas ut
        screen.blit(Bakgrund9, (0,0))
        Dodge_button.draw(screen)
        draw_rect_alpha(screen, (0, 0, 0, 100), (50*scale, 80*scale,1820*scale, 120*scale,))
        screen.blit(SceneTitle, text_rect)
        screen.blit(Dodge_text, (820*scale, 900*scale ))
        
        # När knappen trycks ned byter spelet scen beroende på ifall spelaren lyckas dodga
        if Dodge_button.clicked():
            if self.spelare.dodge_trap == True:
                self.state = 'Dodge_Trap_Scene'
            else:
                self.state = 'Fall_For_Trap_Scene' 
                
    def Dodge_Trap_Scene(self):
        # Knapp med tillhörande text sätts
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Continue_Button = Button(800, 900 , Button1_image, 0.7)
        
        # Beskrivande text med vald position sätts i variabler
        SceneTitle =  Font1_100.render("You succeeded to dodge the boulder!",True,Gray)
        text_rect = SceneTitle.get_rect(center = (screen_Width//2, 155*scale)) 
        
        # Bakgrunden, knappen, semi transperanterenta och alla texter ritas ut
        screen.blit(Bakgrund10, (0,0))
        Continue_Button.draw(screen)
        draw_rect_alpha(screen, (0, 0, 0, 100), (150*scale, 100*scale,1620*scale, 120*scale,))
        screen.blit(SceneTitle, text_rect) 
        screen.blit(Continue_text, (820*scale, 900*scale ))
        
        # När knappen trycks ned byts scenen till "choice_scene"
        if Continue_Button.clicked():
            self.state = "Choice_Scene"
                
    def Fall_For_Trap_Scene(self):
        # Knapp med tillhörande text sätts  
        Continue_text = Font6_70.render("Continue", True, Dark_Grey)
        Continue_Button = Button(800, 900 , Button1_image, 0.7)

        # Beskrivande text med vald position sätts i variabler
        SceneTitle =  Font1_100.render("You failed to dodge the boulder!",True,Gray)
        text_rect = SceneTitle.get_rect(center = (screen_Width//2, 155*scale))
        
        text_obj = Font1_100.render(f"You took 2 damage!",True,Gray)
        text_rect2 = text_obj.get_rect(center = (screen_Width/2, 300*scale))
        
        # Bakgrunden, knappen, semi transperanterenta och alla texter ritas ut
        screen.blit(Bakgrund11, (0,0))
        Continue_Button.draw(screen)
        draw_rect_alpha(screen, (0, 0, 0, 100), (150*scale, 100*scale,1620*scale, 120*scale,))
        screen.blit(SceneTitle, text_rect) 
        screen.blit(text_obj, text_rect2)
        screen.blit(Continue_text, (820*scale, 900*scale ))

        # När knappen trycks ned byts scenen till "choice_scene"
        if Continue_Button.clicked():
            self.state = 'Choice_Scene'
         
    def Game_Over_Scene(self):
        from Class_Player import Player
        # in
        self.spelare = Player(100, 100, 1, 100, 0)

        # Beskrivande text med vald position sätts i variabler
        Text1 = Font1_120.render("You died",True,White)
        Text_pos = Text1.get_rect(center = (screen_Width//2, screen_Height//2))

        # Knappar med tillhörande text sätts
        Exit_text = Font6_70.render("Exit", True, Dark_Grey)
        Exit_Button = Button(1070*scale, 757*scale , Button1_image, 0.7)       

        Restart_text = Font6_70.render("Restart", True, Dark_Grey)
        Restart_Button = Button(430*scale, 757*scale, Button1_image, 0.7)

        # Spelets bakgrund blir svart. Alla texter och knappar ritas ut
        screen.fill((0,0,0))
        screen.blit(Text1, Text_pos)
        Exit_Button.draw(screen)
        Restart_Button.draw(screen)
        screen.blit(Exit_text, (1090*scale, 757*scale))
        screen.blit(Restart_text, (450*scale, 757*scale))
        
        # Restartar spelet från början
        if Restart_Button.clicked():
            self.state = 'Titlecard'

        # Stänger av spelet
        if Exit_Button.clicked():
            pygame.quit()
            sys.exit()
    
    def You_Won_Scene(self):
        print("hello")

    def state_manager(self):
        # Scenhanterare

        # Beroende på vad "self.state" sätts byter programmet till rätt scen
        # Varje defenition är sin egna scen
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
        if self.state == 'You_Won_Scene':
            self.You_Won_Scene()