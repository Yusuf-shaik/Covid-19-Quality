import random

class BitSimulation:
    def __init__(self, error_probability):
        self.error_probability = error_probability
    
    def get_true(self):
        random_number = random.random()
        if(random_number < self.error_probability):
            return False
        else:
            return True

    def get_false(self):
        random_number = random.random()
        if(random_number < self.error_probability):
            return True
        else:
            return False
            
            