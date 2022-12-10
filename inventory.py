from ursina import *

class BG(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (0.56, 0.86),
            color = color.light_gray
        )

class Item(Draggable):
    def __int__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            color = color.red,
            scale = (0.1, 0.1)
        )

    def drag(self):
        print(f'x: {self.x}')
        print(f'y: {self.y}')

    def drop(self):
        print(f'x: {self.x}')
        print(f'y: {self.y}')

class Grid(Entity):
    def __int__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = color.light_gray
        )

app = Ursina()
bg = BG()
item = Item()
app.run()