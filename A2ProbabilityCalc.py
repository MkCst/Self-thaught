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
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_balls_drawn > hat.nBalls:
        num_balls_drawn = hat.nBalls
    
    experiments = [random.sample(hat.contents, num_balls_drawn) for _ in range(0, num_experiments)] 
    counter_experiments = [Counter(i) for i in experiments]

    n_success = 0
    for i in counter_experiments:
        bool_success = True
        for k,v in expected_balls.items():
            if v > i[k]:
                bool_success = False
                break
        if bool_success:
            n_success +=1
    return n_success / num_experiments


if __name__ == '__main__':
    hat = Hat(blue=4, red=2, green=6)   
    probability = experiment(
        hat=hat,
        expected_balls={"blue":2, "red":1},
        num_balls_drawn=4,
        num_experiments=3000
    )
    print("La probabilidad es: ",probability)
