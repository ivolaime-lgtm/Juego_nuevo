import random
objetos = ["espada", "posición de curación", "esplosivo", "un TP", None]
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.recompensa = [None]

    def inspeccion(self):
        recompensa = None
        if self.name == "Dougeon":
            recompensa  = random.choice(objetos)
            self.recompensa.append(recompensa)
        return recompensa


    def go(self, direction):
        return self.paths.get(direction, None), self.description

    def add_paths(self, paths):
        self.paths.update(paths)
