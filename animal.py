class Animals:

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def sound(self, sound):
        print(f'Издает звук {sound}')


class Wings(Animals):

    def __init__(self, name, color) -> None:
        super().__init__(name, color)
    
class FourFoots(Animals):

    def __init__(self, name, color) -> None:
        super().__init__(name, color)
