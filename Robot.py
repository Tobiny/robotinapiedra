import random as rd


class Robot:
    def __init__(self):
        self.victorias = 0
        self.derrotas = 0
        self.tirada = ''

    def tirar(self, tiradas, contador):
        if contador < 3:
            x = list(tiradas.keys())[rd.randint(0, 4)]
            print('el basilisco elige:', x)
            self.tirada = x
        else:
            dist = [element[0] / contador for element in tiradas.values()]
            randRoll = rd.random()  # in [0,1]
            sum = 0
            result = 0
            for mass in dist:
                sum += mass
                if randRoll < sum:
                    x = list(tiradas.keys())[result]
                    eleccion = [key for key in tiradas.keys() if x in tiradas[key][1]]
                    y = rd.choice(eleccion)
                    self.tirada = y
                    print('el basilisco elige:', y)
                    break
                result += 1
        return self.tirada