class Item():   
    def __init__ (self, Name, Strength, Description, intelligence, image, price):
        self.price = price
        self.intelligence = intelligence
        self.Name = Name
        self.Strength = Strength
        self.Description = Description
        self.image = image 


Empty = Item("", 0, "", 0, "renders/Färdigt/Items/Empty.png", 0) 

Crossbow = Item("A Crossow", 40, "A bow with alot of arrows!", 10, "renders/Färdigt/Items/crossbow.png", 300)
Holy_Bible = Item("Holy Bible", 0, "The original Holy Bible!", 40, "renders/Färdigt/Items/Holy Bible.png", 200)
Spiked_Club = Item("Spiked Mace Club", 40, "A heavy mace club filled with rusty spikes!", 0, "renders/Färdigt/Items/Spiked_Mace_Club.png", 275)
Gandalf_Staff = Item("Gandalf's staff", 30, "Giant staff previously owned by Gandalf The Gray!", 20, "renders/Färdigt/Items/magical_staff.png", 375)
Eternal_Flame = Item("Eternal Flame", 30, "A spectacular torch that burns for all Eternity!", 5, "renders/Färdigt/Items/torch.png", 300)
Excalibur = Item("Excalibur", 70, "The legendary sword of King Arthur", 5, "renders/Färdigt/Items/Excalibur.png", 500)
Axe = Item("Axe", 35, "A stupid ass looking axe", 0, "renders/Färdigt/Items/Axe.png", 175)
Twosided_Axe = Item("Two-sided Axe", 40, "davids ansvarsområde", 0, "renders/Färdigt/Items/axe_twosided.png", 225)
Spearaxe = Item("Spear-Axe", 50, "Powerfull axe that can also be used as a spear!", 0, "renders/Färdigt/Items/axe_spear.png", 300)
Dagger = Item("Long Dagger", 20, "A long dagger -_-", 0, "renders/Färdigt/Items/daggerish.png", 150)
Mjölnir = Item("Mjölnir", 60, "Thor something something", 5, "renders/Färdigt/Items/Mjolnir.png", 450)


alla_items = [Crossbow, Axe, Twosided_Axe, Spearaxe, Dagger, Mjölnir, Holy_Bible, Empty]
Shop_List = [Spiked_Club, Gandalf_Staff, Eternal_Flame, Excalibur]