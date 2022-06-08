class Animal:
    def __init__(self, name, health_level, happiness_level) -> None:
        self.name = name
        self.age = 0
        self.health_level = health_level
        self.happiness_level = happiness_level
    
    def display_info(self):
        print (f"Name : {self.name} | health : {self.health_level} | Happiness : {self.happiness_level}")
        return self

    def feed(self):
        self.health_level +=10
        self.happiness_level += 10
        return self

class Lion(Animal):
    def __init__(self, name, hair_style = "curly") -> None:
        super().__init__(name, health_level = 100, happiness_level =60)
        self.type = "Lion"
        self.hair_style = hair_style

    def feed(self):
        self.health_level += 20
        self.happiness_level += 5
        return self

class Tiger(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, health_level = 80, happiness_level =70)
        self.type = "Tiger"
    
    def feed(self):
        self.health_level += 5
        self.happiness_level += 5
        return self

class Bear(Animal):
    def __init__(self, name) -> None:
        super().__init__(name, health_level = 90, happiness_level =150)
        self.type = "Bear"

    def feed(self):
        self.health_level += 10
        self.happiness_level += 25
        return self