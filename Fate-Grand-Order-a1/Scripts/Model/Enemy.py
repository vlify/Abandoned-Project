from Scripts.Model.Base.Character import Character


class Enemy(Character):
    def __init__(self, data, level ):
        super(Enemy, self).__init__(data, level)

    @staticmethod
    def rank_data(rank=1, mainParm="stamina"):
        if rank == 1:
            base = {
                "stamina": 5.0,
                "strength": 5.0,
                "agile": 5.0,
                "intelligence": 5.0,
                "spirit": 5.0,
                "memory": 5.0,
                "rule": 5.0
            }
            up = {
                "stamina": 0.1,
                "strength": 0.1,
                "agile": 0.1,
                "intelligence": 0.1,
                "spirit": 0.1,
                "memory": 0.1,
                "rule": 0.1
            }
            element = {
                "fire": 0,
                "water": 0,
                "thunder": 0,
                "wind": 0,
                "earth": 0,
                "light": 0,
                "dark": 0
            }
            base[mainParm] = base[mainParm] + 0.1
            up[mainParm] = up[mainParm] + 0.1
        elif rank == 2:
            base = {
                "stamina": 10.0,
                "strength": 10.0,
                "agile": 10.0,
                "intelligence": 10.0,
                "spirit": 10.0,
                "memory": 10.0,
                "rule": 10.0
            }
            up = {
                "stamina": 0.2,
                "strength": 0.2,
                "agile": 0.2,
                "intelligence": 0.2,
                "spirit": 0.2,
                "memory": 0.2,
                "rule": 0.2
            }
            element = {
                "fire": 0,
                "water": 0,
                "thunder": 0,
                "wind": 0,
                "earth": 0,
                "light": 0,
                "dark": 0
            }
            base[mainParm] = base[mainParm] + 0.2
            up[mainParm] = up[mainParm] + 0.2
        elif rank == 3:
            base = {
                "stamina": 15.0,
                "strength": 15.0,
                "agile": 15.0,
                "intelligence": 15.0,
                "spirit": 15.0,
                "memory": 15.0,
                "rule": 15.0
            }
            up = {
                "stamina": 0.3,
                "strength": 0.3,
                "agile": 0.3,
                "intelligence": 0.3,
                "spirit": 0.3,
                "memory": 0.3,
                "rule": 0.3
            }
            element = {
                "fire": 0,
                "water": 0,
                "thunder": 0,
                "wind": 0,
                "earth": 0,
                "light": 0,
                "dark": 0
            }
            base[mainParm] = base[mainParm] + 0.3
            up[mainParm] = up[mainParm] + 0.3
        elif rank == 4:
            base = {
                "stamina": 20.0,
                "strength": 20.0,
                "agile": 20.0,
                "intelligence": 20.0,
                "spirit": 20.0,
                "memory": 20.0,
                "rule": 20.0
            }
            up = {
                "stamina": 0.4,
                "strength": 0.4,
                "agile": 0.4,
                "intelligence": 0.4,
                "spirit": 0.4,
                "memory": 0.4,
                "rule": 0.4
            }
            element = {
                "fire": 5,
                "water": 5,
                "thunder": 5,
                "wind": 5,
                "earth": 5,
                "light": 5,
                "dark": 5
            }
            base[mainParm] = base[mainParm] + 0.4
            up[mainParm] = up[mainParm] + 0.4
        elif rank == 5:
            base = {
                "stamina": 30.0,
                "strength": 30.0,
                "agile": 30.0,
                "intelligence": 30.0,
                "spirit": 30.0,
                "memory": 30.0,
                "rule": 30.0
            }
            up = {
                "stamina": 0.5,
                "strength": 0.5,
                "agile": 0.5,
                "intelligence": 0.5,
                "spirit": 0.5,
                "memory": 0.5,
                "rule": 0.5
            }
            element = {
                "fire": 10,
                "water": 10,
                "thunder": 10,
                "wind": 10,
                "earth": 10,
                "light": 10,
                "dark": 10
            }
            base[mainParm] = base[mainParm] + 0.5
            up[mainParm] = up[mainParm] + 0.5
        else:
            base = {
                "stamina": 50.0,
                "strength": 50.0,
                "agile": 50.0,
                "intelligence": 50.0,
                "spirit": 50.0,
                "memory": 50.0,
                "rule": 50.0
            }
            up = {
                "stamina": 1.5,
                "strength": 1.5,
                "agile": 1.5,
                "intelligence": 1.5,
                "spirit": 1.5,
                "memory": 1.5,
                "rule": 1.5
            }
            element = {
                "fire": 10,
                "water": 10,
                "thunder": 10,
                "wind": 10,
                "earth": 10,
                "light": 10,
                "dark": 10
            }
            base[mainParm] = base[mainParm] + 0.5
            up[mainParm] = up[mainParm] + 0.5
        return base, up, element
