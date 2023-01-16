# Item initieras med massor med olika variabler som örr spelaren. Variablerna är Name (namn), 
# styrka (Strength), beskrivning (description), inteligens (intelligence) och itembilden (image) och pris(price)

class Item():   
    def __init__ (self, Name, Strength, Description, intelligence, image, price):
        self.price = price
        self.intelligence = intelligence
        self.Name = Name
        self.Strength = Strength
        self.Description = Description
        self.image = image 

# Items som används i spelet sätts
Crossbow = Item("A Crossow", 40, "A bow with alot of arrows!", 10, "Bilder/Items/crossbow.png", 300)
Holy_Bible = Item("Holy Bible", 0, "The original Holy Bible!", 40, "Bilder/Items/Holy Bible.png", 250)
Spiked_Club = Item("Spiked Mace Club", 40, "A heavy mace club filled with rusty spikes!", 0, "Bilder/Items/Spiked_Mace_Club.png", 275)
Gandalf_Staff = Item("Gandalf's staff", 40, "Giant staff previously owned by Gandalf The Gray!", 20, "Bilder/Items/magical_staff.png", 375)
Eternal_Flame = Item("Eternal Flame", 30, "A spectacular torch that burns for all Eternity!", 5, "Bilder/Items/torch.png", 275)
Excalibur = Item("Excalibur", 70, "The legendary sword of King Arthur!", 5, "Bilder/Items/Excalibur.png", 500)
Axe = Item("Axe", 35, "An axe made of pure iron!", 0, "Bilder/Items/Axe.png", 225)
Twosided_Axe = Item("Two-sided Axe", 40, "A powerful axe with two blades!", 0, "Bilder/Items/axe_twosided.png", 250)
Spearaxe = Item("Spear-Axe", 50, "A powerfull axe that can also be used as a spear!", 0, "Bilder/Items/axe_spear.png", 300)
Dagger = Item("Long Dagger", 20, "A long but weak dagger", 0, "Bilder/Items/daggerish.png", 175)
Mjölnir = Item("Mjölnir", 60, "The hammer of the allmighty Thor!", 5, "Bilder/Items/Mjolnir.png", 450)

# tomt item för att illustrera att man exempelvis har en tom plats i inventoryt eller i shoppen. 
Empty = Item("", 0, "", 0, "Bilder/Items/Empty.png", 0) 

# Items som man kan få 
alla_items = [Crossbow, Axe, Twosided_Axe, Spearaxe, Dagger, Mjölnir, Holy_Bible, Empty]

# items som startar i shoppen 
Shop_List = [Spiked_Club, Gandalf_Staff, Eternal_Flame, Excalibur]