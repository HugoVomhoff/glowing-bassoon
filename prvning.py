### Menu UI ###
"""
Str = 1000
Hp = 1000
Gul = "Svart"

fråga =     "Vad vill du göra?"
dörr =   "3. Fortsätta på ditt äventyr"
Stats  = "1. Kolla på dina stats"
inventory  = "2. Ta en titt på ditt inventory"
print(len(Stats))
print(len(inventory))
print(len(dörr))




##print(f"{'':<1}{'':_<70} \n|{'':<69} |\n| Styrka: {Str:<60} |\n| Liv:{Hp:<64} |\n| Hudfärg: {Gul:<59} |\n|{'':_<70}|\n")
#Stats


print(f" {'':_<101}") 
print(f"|{'':<101}|")
print(f"|{'':<41}{'':_<19}{'':<41}|")
print(f"|{'':<40}| {fråga} |{'':<40}|")
print(f"|{'':40}|{'':_<19}|{'':<40}|")
print(f"|{'':<101}|")
print(f"|{'':<3} {'':_<24}{'':<2} {'':_<33}{'':<2} {'':_<30} {'':<3}|")
print(f"|{'':<3}| {Stats} | | {inventory} | | {dörr} |{'':<3}|")
print(f"|{'':<3}|{'':_<24}| |{'':_<33}| |{'':_<30}|{'':<3}|")
print(f"|{'':<101}|")
print(f"|{'':_<101}|") 
# UI för alla alternativ början av en runda
menu = ''' 
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                         ___________________                                         |
|                                        | Vad vill du göra? |                                        |
|                                        |___________________|                                        |
|                                                                                                     |
|    ________________________   _________________________________   ______________________________    |
|   | 1. Kolla på dina stats | | 2. Ta en titt på ditt inventory | | 3. Fortsätta på ditt äventyr |   |
|   |________________________| |_________________________________| |______________________________|   |
|                                                                                                     |
|_____________________________________________________________________________________________________|

'''

print(f" {'':_<101} \n|{'':<101}|\n|{'':<41}{'':_<19}{'':<41}|\n|{'':<40}| {fråga} |{'':<40}|\n|{'':40}|{'':_<19}|{'':<40}|\n|{'':<101}|\n|{'':<3} {'':_<24}{'':<2} {'':_<33}{'':<2} {'':_<30} {'':<3}|\n|{'':<3}| {Stats} | | {inventory} | | {dörr} |{'':<3}|\n|{'':<3}|{'':_<24}| |{'':_<33}| |{'':_<30}|{'':<3}|\n|{'':<101}|\n|{'':_<101}|")

ett = "stats"
två = "inventory"
tre = "gå igenom en dörr"
hej = "|   | 1. Kolla på dina stats | | 2. Ta en titt på ditt inventory | | 3. Fortsätta på ditt äventyr |   |"
print(len(hej))
"""


### Vilken dörr Ui ###
"""
ok = "|   | Vänster | | Framåt | | Höger |   |"
print(len(ok))
print(len("Vart vill du gå?"))



print(f" {'':_<38}") 
print(f"|{'':<38}|")
print(f"|{'':<10}{'':_<18}{'':<10}|")
print(f"|{'':<9}| Vart vill du gå? |{'':<9}|")
print(f"|{'':<9}|{'':_<18}|{'':<9}|")
print(f"|{'':<38}|")
print(f"|{'':<3} {'':_<9}{'':<2} {'':_<8}{'':<2} {'':_<7} {'':<3}|")
print(f"|{'':<3}| Vänster | | Framåt | | Höger |{'':<3}|")
print(f"|{'':<3}|{'':_<9}| |{'':_<8}| |{'':_<7}|{'':<3}|")
print(f"|{'':<38}|")
print(f"|{'':_<38}|") 
"""
printc

"""
print(len("_______________________________________________________________________________________"))
print(len("VänsterFramåtHöger"))
"""

menu_dörr = """
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                         __________________                                          |
|                                        | Vart vill du gå? |                                         |
|                                        |__________________|                                         |
|                                                                                                     |
|    _____________________________   _____________________________   _____________________________    |
|   |           Vänster           | |            Framåt           | |            Höger            |   |
|   |_____________________________| |_____________________________| |_____________________________|   |
|                                                                                                     |
|_____________________________________________________________________________________________________|

"""

"""

### Svårhetsgrad UI ###

print(f" {'':_<101}") 
print(f"|{'':<101}|")
print(f"|{'':<41}{'':_<19}{'':<41}|")
print(f"|{'':<40}| Välj svårighetsgraden |{'':<40}|")
print(f"|{'':40}|{'':_<19}|{'':<40}|")
print(f"|{'':<101}|")
print(f"|{'':<3} {'':_<24}{'':<2} {'':_<33}{'':<2} {'':_<30} {'':<3}|")
print(f"|{'':<3}| Lätt | | Normal | | Svår |{'':<3}|")
print(f"|{'':<3}|{'':_<24}| |{'':_<33}| |{'':_<30}|{'':<3}|")
print(f"|{'':<101}|")
print(f"|{'':_<101}|") 


print(len("Välj svårighetsgraden"))
"""

hej = input(f" {'':_<101} \n|{'':<101}|\n|{'':<39}{'':_<23}{'':<39}|\n|{'':<38}| Välj svårighetsgraden |{'':<38}|\n|{'':38}|{'':_<23}|{'':<38}|\n|{'':<101}|\n|{'':<3} {'':_<29}{'':<2} {'':_<29}{'':<2} {'':_<29} {'':<3}|\n|{'':<3}|{'':<12}Lätt{'':<13}| |{'':<11} Normal{'':<11}| |{'':<12}Svår{'':<13}|{'':<3}|\n|{'':<3}|{'':_<29}| |{'':_<29}| |{'':_<29}|{'':<3}|\n|{'':<101}|\n|{'':_<101}|\n")
