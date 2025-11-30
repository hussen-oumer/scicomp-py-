import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Initialize the hat with balls based on kwargs (color: count)
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy() 
            self.contents.clear()  
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball) 
        return drawn_balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Deep copy the hat to avoid modifying the original
        hat_copy = copy.deepcopy(hat)

        # Draw balls and count their occurrences
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1

        # Check if the drawn balls meet the expected criteria
        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    # Return the probability of success
    return success_count / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)
