import random
from Class_GameState import GameState
from Class_Item import alla_items, Shop_List, Empty

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

    def Show_Stats(self):
        from Game_State import game_state
        game_state.state = 'Show_Stats_Scene'

    def Set_Difficulty(self, difficulty):
        if difficulty == 1:
            self.monstermaxstr = 100
        elif difficulty == 2:
            self.monstermaxstr = 200
        elif difficulty == 3:
            self.monstermaxstr = 400
        
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
           
    def Trap(self):
        from Game_State import game_state
        
        self.slumpadfälla = random.randint(1,3)
        undvika_fällan = random.randint(1,100)
        self.dodge_trap = False
        
        self.Hp = self.Hp - 3
        
        if undvika_fällan < (self.intelligence - 100):
            self.dodge_trap = True
        
        game_state.state = "Trap_Scene"
            
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

    def str_add(self, AddedStr):
        self.Str += AddedStr
    
    def int_add(self, AddedInt):
        self.intelligence += AddedInt

    def ChangeHp(self, newHp):
        self.Hp = newHp

    def LevelUp(self):
        self.lvl += 1
        
    def monster(self):
        from Game_State import game_state
        monster_str = random.randint((10*self.lvl),int(float(self.monstermaxstr) * (1 + self.lvl/20)))
        
        if self.Str > monster_str:
            self.LevelUp()
            game_state.state = "Win_Scene"

        elif self.Str == monster_str:
            game_state.state = "Draw_Scene"
            
        else:
            self.Hp -= (5 + (self.lvl * 2))
            game_state.state = "Lose_Scene"
    
    def inv_add(self, item):
        
        from Game_State import game_state

        if self.inventory.count(Empty) == 0:
            
            if self.shop == False:
            
                self.inv_full = True
            
                game_state.state = "Chest_Scene_Open"
            else:
                
                self.inv_full = True
            
                game_state.state = "Shop_Scene"

            

            
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
     
    def inv_change(self, change_index): 

        self.str_add(-1*(self.inventory[change_index].Strength)) 
        self.int_add(-1*(self.inventory[change_index].intelligence)) 
        self.inventory[change_index] = self.current_item
        self.str_add(self.current_item.Strength)
        self.int_add(self.current_item.intelligence)

        from Game_State import game_state
        game_state.state = "Show_Inv_Scene"
                   
    def Show_Inv(self):

        from Game_State import game_state
        game_state.state = 'Show_Inv_Scene'

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
