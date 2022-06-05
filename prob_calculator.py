import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, val in kwargs.items():
            for _ in range(val):
                self.contents.append(key)

    def draw(self, number_ball):
        if number_ball > len(self.contents):
            return self.contents
        balls = []
        for _ in range(number_ball):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    n = num_experiments

    expected_no_of_balls = []
    for key in expected_balls:
        expected_no_of_balls.append(expected_balls[key])

    # colors = {}
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        content_drawn = new_hat.draw(num_balls_drawn)
        # isChecked = True

        l = []
        for key in expected_balls:
            l.append(content_drawn.count(key))

        # for j in range(0, len(content_drawn)):
        #     if content_drawn[j] not in colors.keys():
        #         colors[content_drawn[j]] = 0
        #     colors[content_drawn[j]] = colors[content_drawn[j]] + 1

        # isChecked = True

        # for k, v in expected_balls.items():
        #     if k not in colors.keys() or v > colors[k]:
        #         isChecked = False
        #         break
        # if isChecked == True:
        #     m += 1
        if l >= expected_no_of_balls:
            m += 1

    return m / n
# import copy
# import random
# # Consider using the modules imported above.

# class Hat:

#   def __init__(self, **kwargs):
#     self.contents = []
#     for key, value in kwargs.items():
#       for _ in range(value):
#         self.contents.append(key)

#   def draw(self, number):
#     if number > len(self.contents):
#       return self.contents
#     balls = []
#     for _ in range(number):
#       choice = random.randrange(len(self.contents))
#       balls.append(self.contents.pop(choice))
#     return balls

# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

#   expected_no_of_balls = []
#   for key in expected_balls:
#       expected_no_of_balls.append(expected_balls[key])
#   successes = 0

#   for _ in range(num_experiments):
#     new_hat = copy.deepcopy(hat)
#     balls = new_hat.draw(num_balls_drawn)

#     no_of_balls = []
#     for key in expected_balls:
#       no_of_balls.append(balls.count(key))

#     if no_of_balls >= expected_no_of_balls:
#       successes += 1

#   return successes/num_experiments