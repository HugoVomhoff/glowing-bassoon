import time
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

print(f" {'':_<101} \n|{'':<101}|\n|{'':<41}{'':_<18}{'':<42}|\n|{'':<40}| Vart vill du gå? |{'':<41}|\n|{'':40}|{'':_<18}|{'':<41}|\n|{'':<101}|\n|{'':<3} {'':_<29}{'':<2} {'':_<29}{'':<2} {'':_<29} {'':<3}|\n|{'':<3}|{'':<11}Vänster{'':<11}| |{'':<11} Framåt{'':<11}| |{'':<12}Höger{'':<12}|{'':<3}|\n|{'':<3}|{'':_<29}| |{'':_<29}| |{'':_<29}|{'':<3}|\n|{'':<101}|\n|{'':_<101}|")


print(f" {'':_<38} \n|{'':<38}|\n|{'':<10}{'':_<18}{'':<10}|\n|{'':<9}| Vart vill du gå? |{'':<9}|\n|{'':9}|{'':_<18}|{'':<9}|\n|{'':<38}|\n|{'':<3} {'':_<9}{'':<2} {'':_<8}{'':<2} {'':_<7} {'':<3}|\n|{'':<3}| Vänster | | Framåt | | Höger |{'':<3}|\n|{'':<3}|{'':_<9}| |{'':_<8}| |{'':_<7}|{'':<3}|\n|{'':<38}|\n|{'':_<38}|")
print
print(len("_______________________________________________________________________________________"))
print(len("VänsterFramåtHöger"))

""
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
""

"""

### Svårhetsgrad UI ###
"""
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
print(f" {'':_<101} \n|{'':<101}|\n|{'':<39}{'':_<23}{'':<39}|\n|{'':<38}| Välj svårighetsgraden |{'':<38}|\n|{'':38}|{'':_<23}|{'':<38}|\n|{'':<101}|\n|{'':<3} {'':_<29}{'':<2} {'':_<29}{'':<2} {'':_<29} {'':<3}|\n|{'':<3}|{'':<12}Lätt{'':<13}| |{'':<11} Normal{'':<11}| |{'':<12}Svår{'':<13}|{'':<3}|\n|{'':<3}|{'':_<29}| |{'':_<29}| |{'':_<29}|{'':<3}|\n|{'':<101}|\n|{'':_<101}|\n")
"""
menu_svårighetsgrad = """
 _____________________________________________________________________________________________________ 
|                                                                                                     |
|                                       _______________________                                       |
|                                      | Välj svårighetsgraden |                                      |
|                                      |_______________________|                                      |
|                                                                                                     |
|    _____________________________   _____________________________   _____________________________    |
|   |            Lätt             | |            Normal           | |            Svår             |   |
|   |_____________________________| |_____________________________| |_____________________________|   |
|                                                                                                     |
|_____________________________________________________________________________________________________|
"""

##########################   Menu UI när det laddar  #####################


menu_laddning_1 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                           ____                                                                      |
|                          /    \                                                                     |
|                         (      )                                                                    |
|                          \____/                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''
menu_laddning_2 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                           ____             ____                                                     |
|                          /    \           /    \                                                    |
|                         (      )         (      )                                                   |  
|                          \____/           \____/                                                    |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|

'''
menu_laddning_3 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                           ____             ____             ____                                    |
|                          /    \           /    \           /    \                                   |
|                         (      )         (      )         (      )                                  |  
|                          \____/           \____/           \____/                                   |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''

menu_laddning_5 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                            ____             ____                                    |
|                                           /    \           /    \                                   |
|                                          (      )         (      )                                  |  
|                                           \____/           \____/                                   |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''

menu_laddning_4 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                           ____             ____             ____             ____                   |
|                          /    \           /    \           /    \           /    \                  |
|                         (      )         (      )         (      )         (      )                 |  
|                          \____/           \____/           \____/           \____/                  |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''

menu_laddning_6 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                             ____             ____                   |
|                                                            /    \           /    \                  |
|                                                           (      )         (      )                 |  
|                                                            \____/           \____/                  |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''
menu_laddning_7 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                           ____                                               ____                   |
|                          /    \                                             /    \                  |
|                         (      )                                           (      )                 |  
|                          \____/                                             \____/                  |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''

menu_laddning_10 ='''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                   ______________________________________________________________                    |
|                  |______________________________________________________________|                   |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|

'''
menu_laddning_11 ='''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                   ______________________________________________________________                    |
|                  ||||||||||_____________________________________________________|                   |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|

'''


menu_11 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                   ______________________________________________________________                    |
|                  |||||||||||||||||||____________________________________________|                   |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|

'''
menu_12 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                   ______________________________________________________________                    |
|                  |||||||||||||||||||||||||||||||________________________________|                   |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''

menu_13 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                   ______________________________________________________________                    |
|                  |||||||||||||||||||||||||||||||||||||||||||____________________|                   |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''

menu_14 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                   ______________________________________________________________                    |
|                  ||||||||||||||||||||||||||||||||||||||||||||||||||||||_________|                   |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''


menu_15 = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|                   ______________________________________________________________                    |
|                  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||                   |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''
'''
print(menu_laddning_10)
time.sleep(0.7)
print(menu_laddning_11)
time.sleep(0.7)
print(menu_11)
time.sleep(0.7)
print(menu_12)
time.sleep(0.7)
print(menu_13)
time.sleep(0.7)
print(menu_14)
time.sleep(0.7)
print(menu_15)
'''

##################### STARTING SCREEN ####################
starting_screen = '''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                   ________________________________________________________________                  |
|                  |                                                                |                 |
|                  |                     I WANT TO PLAY A GAME                      |                 |
|                  |________________________________________________________________|                 |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|

'''

########################  STATS #########################
Stats_Screen = '''
 _____________________________________________________________________________________________________ 
|                                                                                                     |
|                                       _______________________                                       |
|                                      | Välj svårighetsgraden |                                      |
|                                      |_______________________|                                      |
|                                                                                                     |
|    _____________________________   _____________________________   _____________________________    |
|   |            Lätt             | |            Normal           | |            Svår             |   |
|   |_____________________________| |_____________________________| |_____________________________|   |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''


########################### INVENTORY ###########################

Inventory_Screen = '''
 _____________________________________________________________________________________________________ 
|                                                                                                     |
|                                       _______________________                                       |
|                                      | Välj svårighetsgraden |                                      |
|                                      |_______________________|                                      |
|                                                                                                     |
|    _____________________________   _____________________________   _____________________________    |
|   |            Lätt             | |            Normal           | |            Svår             |   |
|   |_____________________________| |_____________________________| |_____________________________|   |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''

######################## Spelaren LvLar upp  ############################
lvl = 10000000
Lvl_upp = f'''
 _____________________________________________________________________________________________________
|                                                                                                     |
|                                                                                                     |
|                   ________________________________________________________________                  |
|                  |                                                                |                 |
|                  |      Du dödade monstret och Lvlade upp! Du är nu LVL {lvl+1:<10}|                 |
|                  |________________________________________________________________|                 |
|                                                                                                     |
|                                                                                                     |
|_____________________________________________________________________________________________________|
'''
print(Lvl_upp)
