import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, val in kwargs:
            for _ in range(val):
                self.contents.append(key)

    def draw(self, number_ball):
        if number_ball > len(self.contents):
            return
        balls = []
        for _ in range(number_ball):
            choice = random.randint(0, len(self.contents) - 1)
            balls.append(self.contents.pop(choice))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    n = num_experiments

    colors = {}
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        content_drawn = new_hat.draw(num_balls_drawn)
        for j in range(0, len(content_drawn)):
            colors[content_drawn[j]] = colors[content_drawn[j]] + 1

        isChecked = True

        for k, v in expected_balls:
            if expected_balls[k] > colors[k]:
                isChecked = False
                break
        if isChecked:
            m += 1

    return m / n
