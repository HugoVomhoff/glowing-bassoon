# importerar klasser
from Class_GameState import GameState
from Class_Player import Player

# skapar en spelare och scenhanterare (gamestate)
spelare = Player(100, 100, 14, 100, 50000)
game_state = GameState(spelare)