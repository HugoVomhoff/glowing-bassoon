# Viktiga variabler och mattefunktioner importeras 
import random
from Class_Item import alla_items, Shop_List, Empty

class Player(): 
    
    # Player initieras med massor med olika variabler som rör spelaren. Variablerna är styrka (Str), 
    # Hälsa (Hp), Level (lvl), inteligens, (intelligence) och Guldmängd (gold)
    # En del andra standardvärden sätts även på variabler som ska användas i senare funktioner.
    def __init__ (self, Str, Hp, lvl, intelligence, gold):
       
        self.intelligence = intelligence
        self.Hp = Hp
        self.Str = Str
        self.lvl = lvl
        self.inv_full = False
        self.gold = gold
        self.Shop_List = Shop_List
        self.noitems = False
        self.can_afford = True
        self.win = False
        self.last = 10
        self.reset = False

        self.inventory = [Empty, Empty ,Empty ,Empty ,Empty]
        self.alla_items = alla_items

    def Show_Stats(self):
        # Sätter gamestate som är scenhanterar till att visa scenen "Show_Stats_Scene" som visar dina stats
        from Game_State import game_state
        game_state.state = 'Show_Stats_Scene'

    def Set_Difficulty(self, difficulty):
        
        # Baserat på vilken difficultyknapp du tryckt på så ändras monsternas maxstyrka för att ändra svårigheten på spelet
        if difficulty == 1:
            self.monstermaxstr = 100
        elif difficulty == 2:
            self.monstermaxstr = 200
        elif difficulty == 3:
            self.monstermaxstr = 400
    

    def Choice(self, Choice):
        
        # Vilken knapp du trycker på i "huvudrumet", du kan t.ex välja att gå till shoppen, 
        # kolla på ditt inventory eller fortsätta på ditt äventyr.
        
        from Game_State import game_state
        
        # Om du valt knappen show stats så sätts scnenen till "show_stats_scene" som visar dina stats
        if Choice == 1:
            self.Show_Stats()

        # Om du klickar på knappen show inventory så sätts scenen till "show_inv_scene" som visar ditt inventory
        elif Choice == 2:
            self.Show_Inv()   
        
            
        # Om du valt knappen som fortsätter på ditt äventyr så slumpas det fram var du kommer att hamna
        elif Choice == 3:
            utfall = random.randint(1,3)   
            
            # antingen så hamnar du hos ett monster
            if utfall == 1 and self.last != 1:
                game_state.state = "Monster_Scene"

            # eller så hamnar du i en fälla
            if utfall == 2 and self.last != 2:
                self.Trap()
            
            # eller så hamnar du vid en kista
            if utfall == 3 and self.last != 3:   
                game_state.state = 'Chest_Scene'
    
            self.last = utfall
    # och slutligen om du valde att klicka på shop knappen så sätts scenen till "shop_scene" och du hamnar istället vid shopmenyn
        elif Choice == 4:
            game_state.state = "Shop_Scene"
  
    def Trap(self):
        from Game_State import game_state
       
        # När du hamnar i en fälla så ska du ha en chans att undvika fällan baserat på din inteligens så vi slumpar mellan 1 till 100 och om
        # din intelligens - 100 är större än det slumpade talet så kommer du undvika fällan
        undvika_fällan = random.randint(1,100)
        self.dodge_trap = False
        
        if undvika_fällan < (self.intelligence - 100):
            self.dodge_trap = True
            game_state.state = "Trap_Scene"
        else:
            self.Hp = self.Hp - 3
            game_state.state = "Trap_Scene"
            
    def Chest(self):
        
        # Ett tal mellan 1 och 10 slumpas fram
        guld_eller_item = random.randint(1,10)
        self.chest_gold = False
        

        # Om det inte finns några items kvar att få eller du är level 15 så vinner du spelet och hittar automatiskt kronan
        if self.alla_items[0].name == ""  and self.Shop_List.count(Empty) == 4 or self.lvl >= 15:
            from Class_Item import Crown
            self.current_item = Crown
            self.win = True
        
        else:

            # När du öppnar en kista är det 20% chans att du får ett item medans det är 80% att du får guld
            if guld_eller_item < 3 and self.alla_items[0].Name != "":


                # Det sista itemet i itemlistan som vi hämta från är ett specialitem, om det itemet är det enda i listan så sätts "noitems" till True och
                # du kommer vinna spelet nästa gång du hamnar vid en kista
                if(self.alla_items[1].Name == ""):
                    self.shop = False
                    self.inv_add(self.alla_items[0])
                    self.current_item = self.alla_items[0]
                    self.alla_items.pop(0)
                    self.noitems = True
                
                # Om inget av de övre if-satserna "triggras" men du ska få ett item så får du ett item och det läggs till i inventoryt
                else:                
                    self.shop = False
                    self.inv_add(self.alla_items[0])
                    self.current_item = self.alla_items[0]
                    self.alla_items.pop(0)

            # Hur mycket guld du får slumpas fram mellan 40 och 120 och adderas på ditt nuvarande.
            elif self.win != True:

                self.chest_gold = True
                self.current_item = random.randint(40,120)
                self.gold += self.current_item

    # Adderar given mängd styrka ovanpå din tidigare styrka
    def str_add(self, AddedStr):
        self.Str += AddedStr
    
    # Adderar given mängd inteligens ovanpå din tidigare styrka
    def int_add(self, AddedInt):
        self.intelligence += AddedInt

    # Ändrar ditt tidigare Hp till ett nytt värde
    def ChangeHp(self, newHp):
        self.Hp = newHp

    # Levlar upp din spelare en level
    def LevelUp(self):
        self.lvl += 1
    

    def monster(self):
        
        # Monsternas styrka slumpas fram men blir också högre baserat på vilken level du är i
        from Game_State import game_state
        monster_str = random.randint((10*self.lvl),int(float(self.monstermaxstr) * (1 + self.lvl/20)))
        
        # Om du har mer styrka är monstret så vinner du och scenen ändras till "Win_Scene"
        if self.Str > monster_str:
            self.LevelUp()
            game_state.state = "Win_Scene"


        # Om ni har samma styrka blir det lika och scenen ändras till "Draw_Scene"
        elif self.Str == monster_str:
            game_state.state = "Draw_Scene"
            
        else:
            self.Hp -= (5 + (2 * self.lvl))
            
            # Om du hamnar under eller på 0 hp så förlorar du och scenen ändras till "Game_Over_Scene"
            if self.Hp <= 0:
                game_state.state = "Game_Over_Scene"

            # Om monstret har mer styrka så tappar du hp baserat på vilken level du är och scenen ändras till "Loose_Scene"
            else:
                game_state.state = "Lose_Scene"
    
    def inv_add(self, item):
        
        from Game_State import game_state
        
        # Om ditt inventory är fullt så sätts "inv_full" till True och du blir via shop_scene eller chest_scene kastad till item_managern där du får byta ut ett item

        if self.inventory.count(Empty) == 0:
            
            if self.shop == False:
            
                self.inv_full = True
            
                game_state.state = "Chest_Scene_Open"
            else:
                
                self.inv_full = True
            
                game_state.state = "Shop_Scene"

        else:
            # Om du är i shoppen så har du shopen som bakgrund om du är vid kistan så får du den som bakgrund. 
            # Sedan läggs itemet du fått till i inventoryt tillsammans med dess attribut
            if self.shop == False:
                game_state.state = "Chest_Scene_Open"
                self.inventory[5 - self.inventory.count(Empty)] = item
                self.str_add(item.Strength)
                self.int_add(item.intelligence)
            else: 
                game_state.state = "Shop_Scene"
                self.inventory[5 - self.inventory.count(Empty)] = item
                self.str_add(item.Strength)
                self.int_add(item.intelligence)
    
    def inv_change(self, change_index): 

        # När du byter ut ett item så måste de itemets effekter tas bort och det nya itemets adderas
        # Den gamla strenghten tas bort och den nya adderas osv, sker för alla attribut
        self.str_add(-1*(self.inventory[change_index].Strength)) 
        self.int_add(-1*(self.inventory[change_index].intelligence)) 
        self.inventory[change_index] = self.current_item
        self.str_add(self.current_item.Strength)
        self.int_add(self.current_item.intelligence)


        # Sätter scenen till "Show_Inv_Scene"
        from Game_State import game_state
        game_state.state = "Show_Inv_Scene"


    def Show_Inv(self):
        # Sätter scenen till "Show_Inv_Scene"
        from Game_State import game_state
        game_state.state = 'Show_Inv_Scene'


    def Buy_item(self, item, index):
        
        # Sätter att du har råd som standard
        self.can_afford = True
        
        # Om du har ett fullt inventory så sätts inv_full till True
        if self.inventory.count(Empty) == 0:
            self.inv_full = True
        
        # Om du har mer guld än vad itemet kostar så kan du köpa det
        if self.gold >= item.price:
            
            if self.inv_full == True:
                
                # Om det sista itemet i itemlistan är ett tomt item så sätts "noitems" till True och shoppen refillas inte
                if self.alla_items[0].Name == "":
                    self.shop = True
                    self.noitems = True
                    self.current_item = item
                    self.gold -= item.price
                    self.Shop_List[index] = Empty

                # Om det finns items kvar att hämta så fylls shoppen på med nya items
                else:
                    self.shop = True
                    self.current_item = item
                    self.gold -= item.price
                    self.Shop_List[index] = self.alla_items[0]
                    self.alla_items.pop(0)
                
                # Om inventoryt är fullt och du köper ett item så hamnar du på scenen "Item_Manager" där du kan byta ut ett av dina gamla items
                from Game_State import game_state
                game_state.state = "Item_manager"
                

            # Om inventoryt inte är fullt så addas bara ditt köpta item till ditt inventory
            else:
                # Om det inte finns några nya items så fylls inte shoppen på
                if self.alla_items[0].Name == "":
                    self.gold -= item.price
                    self.Shop_List[index] = Empty
                    self.shop = True
                    self.current_item = item
                    self.inv_add(item)
                # Om det finns items så fylls shoppen på med de nya
                else:
                    self.gold -= item.price
                    self.Shop_List[index] = self.alla_items[0]
                    self.alla_items.pop(0)
                    self.shop = True
                    self.current_item = item
                    self.inv_add(item)
        # Om du inte har mer pengar än vad itemet kostar så sätts "can_afford" till False
        else:
            self.can_afford = False