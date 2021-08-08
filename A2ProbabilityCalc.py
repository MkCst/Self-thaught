# Se utilizaran los siguientes modulos importados
import copy
import random
from collections import Counter


class Hat:
    # Metodo inicio
    def __init__(self, **args):
        """Obtiene una lista con el numero de apariciones de
        cada color"""
        self.balls = args
        self.contents = []
        self.nBalls = 0
        for k,v in args.items():
            for _ in range(0, v):
                self.contents.append(k)
            self.nBalls += v

    # Metodo "quitar"
    def draw(self, nBallsDraw):
        if nBallsDraw > self.nBalls:
            return self.contents
        ballsDraw = []
        ballsDraw = random.sample(self.contents, nBallsDraw)
        for i in ballsDraw:
            self.contents.remove(i)
        return ballsDraw
        

# EXPERIMENTO PRINCIPAL
def experiment(hat, expected_balls, nBallsDraw, nExperiments):
    if nBallsDraw > hat.nBalls:
        nBallsDraw = hat.nBalls

    experiments = [random.sample(hat.contents, nBallsDraw) for _ in range(0, nExperiments)] 
    counter_experiments = [Counter(i) for i in experiments]

    nSuccess = 0
    for i in counter_experiments:
        bool_success = True
        for k,v in expected_balls.items():
            if v>i[k]:
                bool_success = False
                break
            if bool_success:
                nSuccess +=1
    return nSuccess / nExperiments

if __name__ == '__main__':
    hat = Hat(blue=4, red=2, green=6)
    probability = experiment(
        hat=hat,
        expected_balls={"blue":2, "red":1},
        nBallsDraw=4,
        nExperiments=3000
    )
    print("La probabilidad es: ",probability)
