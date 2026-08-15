class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine=Engine()  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Delegation: Car delegates the start method to Engine

c=Car()
c.start_car()