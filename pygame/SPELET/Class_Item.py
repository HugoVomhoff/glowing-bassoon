class Item():   
    def __init__ (self, Name, Strength, Description, intelligence, image, price):
        self.price = price
        self.intelligence = intelligence
        self.Name = Name
        self.Strength = Strength
        self.Description = Description
        self.image = image 


Empty = Item("", 0, "", 0, "Empty", 0) 

Bow = Item("A Bow", 40, "A bow with alot of arrows!", 10, "placeholder", 300)
Holy_Bible = Item("Holy Bible", 0, "The original Holy Bible!", 40, "placeholder", 200)
Spiked_Club = Item("Spiked Club", 40, "A heavy club filled with rusty spikes!", 0, "placeholder", 275)
Gandalf_Staff = Item("Gandalf's staff", 30, "Giant staff previously owned by Gandalf The Gray!", 20, "placeholder", 375)
Eternal_Flame = Item("Eternal Flame", 30, "A spectacular torch that burns for all Eternity!", 5, "placeholder", 300)
Excalibur = Item("Excalibur", 70, "The legendary sword of King Arthur", 5, "placeholder", 500)


alla_items = [Holy_Bible, Spiked_Club, Gandalf_Staff, Eternal_Flame, Excalibur, Bow]
Shop_List = [Holy_Bible, Spiked_Club, Gandalf_Staff, Eternal_Flame, Excalibur]