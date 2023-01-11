# Viktiga variabler och mattefunktioner importeras 
import random
from Class_Item import alla_items, Shop_List, Empty


# Player initieras med massor med olika variabler som örr spelaren. Variablerna är styrka (Str), 
# Hälsa (Hp), Level (lvl), inteligens, (intelligence) och Guldmängd (gold)
# En del andra standardvärden sätts även på variabler som ska användas i senare funktioner.

class Player(): 
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

        self.inventory = [Empty, Empty ,Empty ,Empty ,Empty]
        self.alla_items = alla_items

    # Funktionen ändrar scen till statvisarscenen som visar all spelarens olika värden
    def Show_Stats(self):
        from Game_State import game_state
        game_state.state = 'Show_Stats_Scene'

    # Sätter svårighetsgraden på spelet genom att ändra den maximala styrkan monster kan ha
    def Set_Difficulty(self, difficulty):
        if difficulty == 1:
            self.monstermaxstr = 100
        elif difficulty == 2:
            self.monstermaxstr = 200
        elif difficulty == 3:
            self.monstermaxstr = 400
    
    # Vilken knapp du trycker på i "huvudrumet", du kan t.ex välja att gå till affären, 
    # kolla på ditt inventory eller fortsätta på ditt äventyr. Den knapp du trycker på bestämmer 
    # då var du kommer hamna.

    def Choice(self, Choice):
        from Game_State import game_state
        if Choice == 1:
            self.Show_Stats()
        elif Choice == 2:
            self.Show_Inv()   
        elif Choice == 3:
            utfall = random.randint(1,3)   
            
            if utfall == 1:
                game_state.state = "Monster_Scene"

            if utfall == 2:
                self.Trap()
                
            if utfall == 3:   
                game_state.state = 'Chest_Scene'

        elif Choice == 4:
            game_state.state = "Shop_Scene"

    # När du hamnar i en fälla så ska du ha en chans att undvika fällan baserat på din inteligens,
    # om du dodgar trapen så sätter vi att du dodgar till True och skickar det vidare.
    # Om du inte dodgar så försvinner lite av ditt Hp och vi ändrar till scenen där du skadas av fällan.    
    def Trap(self):
        from Game_State import game_state
        
        self.slumpadfälla = random.randint(1,3)
        undvika_fällan = random.randint(1,100)
        self.dodge_trap = False
        
        self.Hp = self.Hp - 5
        
        if undvika_fällan < (self.intelligence - 100):
            self.dodge_trap = True
        
        game_state.state = "Trap_Scene"

    # När du öppnar en chista är det 30% chans att du får ett item medans det är 70% att du får guld
    # Hur mycket guld du får slumpas fram mellan 40 och 120. Det finns failsafes för om du redan har tagit
    # slut på alla items och då ska du bara kunna få guld.
    # Den fungerar genom att om ditt enda item är strängen "" så sätts att det inte finns någr items till True
    # och du får guld istället.
            
    def Chest(self):
        
        guld_eller_item = random.randint(1,10)
        
        
        self.chest_gold = False
        
        if guld_eller_item <= 3 and self.alla_items[0].Name != "":
            
            if self.alla_items[0].Name == "":
                self.noitems = True

            elif(self.alla_items[1].Name == ""):
                self.shop = False
                self.inv_add(self.alla_items[0])
                self.current_item = self.alla_items[0]
                self.alla_items.pop(0)
                
            else:
                
                self.shop = False
                self.inv_add(self.alla_items[0])
                self.current_item = self.alla_items[0]
                self.alla_items.pop(0)
        else:

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
    
    # Monsternas styrka slumpas baserat på vilken level din spelare är och om din styrka är högre än 
    # monstrets styrka så vinner du annars tar du damage baserat på skillnaden i styrka

    def monster(self):
        from Game_State import game_state
        monster_str = random.randint((10*self.lvl),int(float(self.monstermaxstr) * (1 + self.lvl/20)))
        
        if self.Str > monster_str:
            self.LevelUp()
            game_state.state = "Win_Scene"

        elif self.Str == monster_str:
            game_state.state = "Draw_Scene"
            
        else:
            self.Hp -= (monster_str - self.Str)
            game_state.state = "Lose_Scene"
    
    # Om ditt inventory är fullt så får du välja om du vill byta ut ett av dina nuvarande items
    # mot det nya annars adderas bara det nya itemet i din iventorylista
    def inv_add(self, item):
        
        from Game_State import game_state

        if self.inventory.count(Empty) == 0:
            
            if self.shop == False:
            
                self.inv_full = True
            
                game_state.state = "Chest_Scene_Open"
            else:
                
                self.inv_full = True
            
                game_state.state = "Shop_Scene"
        # Om du är i shopen så har du shopen som bakgrund när du får byta ut dina items annars om du är
        # vid kistan så får du den som bakgrund.
        else:
            
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
    
    # När du byter ut ett item så måste de itemets effekter tas bort och det nya itemets adderas så det händer här:
    def inv_change(self, change_index): 

        self.str_add(-1*(self.inventory[change_index].Strength)) 
        self.int_add(-1*(self.inventory[change_index].intelligence)) 
        self.inventory[change_index] = self.current_item
        self.str_add(self.current_item.Strength)
        self.int_add(self.current_item.intelligence)

        from Game_State import game_state
        game_state.state = "Show_Inv_Scene"

    # Tar dig till scenen där inventoryt visas         
    def Show_Inv(self):

        from Game_State import game_state
        game_state.state = 'Show_Inv_Scene'

    # Aktiveras när du klickar på ett item i shopen och den kollar om du har råd med itemet och isåfall
    # köper det annars köper det inte. När du köpt ett item tas det även bort från shopen och ett nytt hamnar där
    # om det inte finns några items kvar så blir den shopplatsen tom.
    def Buy_item(self, item, index):
        
        self.can_afford = True
        
        if self.inventory.count(Empty) == 0:
            self.inv_full = True
        
        if self.gold >= item.price:
            
            if self.inv_full == True:
                
                if self.alla_items[0].Name == "":
                    self.shop = True
                    self.noitems = True
                    self.current_item = item
                    self.gold -= item.price
                    self.Shop_List[index] = Empty

                else:
                    self.shop = True
                    self.current_item = item
                    self.gold -= item.price
                    self.Shop_List[index] = self.alla_items[0]
                    self.alla_items.pop(0)
                
                from Game_State import game_state
                game_state.state = "Item_manager"
                

            
            else:
                if self.alla_items[0].Name == "":
                    self.gold -= item.price
                    self.Shop_List[index] = Empty
                    self.shop = True
                    self.current_item = item
                    self.inv_add(item)

                else:
                    self.gold -= item.price
                    self.Shop_List[index] = self.alla_items[0]
                    self.alla_items.pop(0)
                    self.shop = True
                    self.current_item = item
                    self.inv_add(item)

        else:
            self.can_afford = False
