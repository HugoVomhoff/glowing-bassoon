class Item():   
    def __init__ (self, Name, Strength, Description, intelligence, image, price):
        self.price = price
        self.intelligence = intelligence
        self.Name = Name
        self.Strength = Strength
        self.Description = Description
        self.image = image 


Empty = Item("no", 0, "no", 0, "Empty", 0) 

Crossbow = Item("A Crossow", 40, "A bow with alot of arrows!", 10, "crossbow", 300)
Holy_Bible = Item("Holy Bible", 0, "The original Holy Bible!", 40, "placeholder", 200)
Spiked_Club = Item("Spiked Mace Club", 40, "A heavy mace club filled with rusty spikes!", 0, "Spiked_Mace_Club", 275)
Gandalf_Staff = Item("Gandalf's staff", 30, "Giant staff previously owned by Gandalf The Gray!", 20, "magical_staff", 375)
Eternal_Flame = Item("Eternal Flame", 30, "A spectacular torch that burns for all Eternity!", 5, "torch", 300)
Excalibur = Item("Excalibur", 70, "The legendary sword of King Arthur", 5, "Excalibur", 500)
Axe = Item("Axe", 35, "A stupid ass looking axe", 0, "Axe", 175)
Twosided_Axe = Item("Two-sided Axe", 40, "davids ansvarsområde", 0, "axe_twosided", 225)
Spearaxe = Item("Spear-Axe", 50, "Powerfull axe that can also be used as a spear!", 0, "axe_spear", 300)
Dagger = Item("Long Dagger", 20, "A long dagger -_-", 0, "daggerish", 150)
Mjölnir = Item("Mjölnir", 60, "Thor something something", 5, "Mjolnir", 450)


alla_items = [Crossbow, Axe, Twosided_Axe, Spearaxe, Dagger, Mjölnir, Holy_Bible, Empty]
Shop_List = [Spiked_Club, Gandalf_Staff, Eternal_Flame, Excalibur]