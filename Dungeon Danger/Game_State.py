# importerar klasser
from Class_GameState import GameState
from Class_Player import Player

# skapar en spelare och scenhanterare (gamestate)
spelare = Player(100, 1, 1, 100, 50)
game_state = GameState(spelare)