import random
from Class_GameState import GameState
from Class_Item import alla_items
from Class_Item import Empty

class Player(): 
    def __init__ (self, Str, Hp, lvl, intelligence, gold):
       
        self.intelligence = intelligence
        self.Hp = Hp
        self.Str = Str
        self.lvl = lvl
        self.inv_full = False
        self.gold = gold

        self.inventory = [Empty, Empty ,Empty ,Empty ,Empty]
        self.value_inventory = []
        
        self.alla_items = alla_items
        self.current_item = "inget"

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
        
        if undvika_fällan < (self.intelligence - 100):
            self.dodge_trap = True
        
        game_state.state = "Trap_Scene"
            
    def Chest(self):
        
        guld_eller_item = random.randint(1,10)
        self.chest_gold = False
        
        if guld_eller_item <= 3:
            
            if self.alla_items[0] == "m":
                print("Det fanns inga items kvar så du får denna snygga babe ;) ")

            elif(self.alla_items[1] == "m"):
                self.inv_add(self.alla_items[0])
                self.current_item = self.alla_items[self.founditem]
                self.alla_items.pop(self.founditem)

            elif len(self.alla_items) == 2:
                
                self.founditem = random.randint(0, len(self.alla_items)-1)
                self.inv_add(self.alla_items[self.founditem])
                self.current_item = self.alla_items[self.founditem]
                self.alla_items.pop(self.founditem)
                self.alla_items.append("m")
                
            else:
                
                self.founditem = random.randint(0, len(self.alla_items)-1)
                self.inv_add(self.alla_items[self.founditem])
                self.current_item = self.alla_items[self.founditem]
                self.alla_items.pop(self.founditem)
        else:

            self.chest_gold = True
            self.current_item = random.randint(40,120)
            self.gold += self.current_item

        

    def str_add(self, AddedStr):
        self.Str = self.Str + AddedStr

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
            self.Hp = self.Hp - monster_str
            game_state.state = "Lose_Scene"
    
    def inv_add(self, item):
        
        from Game_State import game_state

        if self.inventory.count(Empty) == 0:
            
            
            self.inv_full = True
            
            game_state.state = "Chest_Scene_Open"
            

            
        else:
            
            game_state.state = "Chest_Scene_Open"
            self.inventory[5 - self.inventory.count(Empty)] = item
            self.str_add(item.Strength)
            self.value_inventory.append(item)
    
    def inv_change(self, change):

        item = self.current_item

        self.str_add(-1*(self.value_inventory[change - 1].Strength)) 
        self.inventory[change - 1] = item
        self.str_add(item.Strength)
               
    def  Show_Inv(self):
        from Game_State import game_state
        game_state.state = 'Show_Inv_Scene'
        
        for plats in self.inventory:
            print(plats)