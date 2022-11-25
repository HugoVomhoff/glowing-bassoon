import random
from Class_GameState import GameState
from Class_Item import alla_items
from Class_Item import Empty

class Player(): 
    def __init__ (self, Str, Hp, lvl, intelligence, gold):
        self.intelligence = intelligence
        self.inventory = [Empty, Empty ,Empty ,Empty ,Empty]
        self.value_inventory = []
        self.Hp = Hp
        self.Str = Str
        self.lvl = lvl
        self.inv_full = False
        self.gold = gold
        
        
        self.alla_items = alla_items
        self.current_item = "inget"

    def Show_Stats(self):
        from Game_State import game_state
        game_state.state = 'Show_Stats_Scene'

    def Set_Difficulty(self, difficulty):
       # self.difficulty = input(f" {'':_<101} \n|{'':<101}|\n|{'':<39}{'':_<23}{'':<39}|\n|{'':<38}| Välj svårighetsgraden |{'':<38}|\n|{'':38}|{'':_<23}|{'':<38}|\n|{'':<101}|\n|{'':<3} {'':_<29}{'':<2} {'':_<29}{'':<2} {'':_<29} {'':<3}|\n|{'':<3}|{'':<12}Lätt{'':<13}| |{'':<11} Normal{'':<11}| |{'':<12}Svår{'':<13}|{'':<3}|\n|{'':<3}|{'':_<29}| |{'':_<29}| |{'':_<29}|{'':<3}|\n|{'':<101}|\n|{'':_<101}|\n")
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
            utfall = 3
            #utfall = random.randint(1,3)
            
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
        if guld_eller_item <= 3:
            if self.alla_items[0] == "m":
                print("Det fanns inga items kvar så du får denna snygga babe ;) ")

            elif(self.alla_items[1] == "m"):
                print(f"Du hittade {self.alla_items[0].Name}! {self.alla_items[0].Description}")
                self.inv_add(self.alla_items[0])
                self.current_item = self.alla_items[self.founditem]
                self.alla_items.pop(self.founditem)

            elif len(self.alla_items) == 2:
                
                self.founditem = random.randint(0, len(self.alla_items)-1)
                print(f"Du hittade {self.alla_items[self.founditem].Name}! {self.alla_items[self.founditem].Description}")
                self.inv_add(self.alla_items[self.founditem])
                self.current_item = self.alla_items[self.founditem]
                self.alla_items.pop(self.founditem)
                self.alla_items.append("m")
                
            else:
                
                self.founditem = random.randint(0, len(self.alla_items)-1)
                print(f"Du hittade {self.alla_items[self.founditem].Name}! {self.alla_items[self.founditem].Description}")
                self.inv_add(self.alla_items[self.founditem])
                self.current_item = self.alla_items[self.founditem]
                self.alla_items.pop(self.founditem)
        else:
            self.gold += random.randint(40,120)
            #Du hittade x guld
        

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