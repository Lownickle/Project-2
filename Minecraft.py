from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController




app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)




block_pick = 1

window.exit_button.visible = False


def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1

    if held_keys['2']: block_pick = 2

    if held_keys['3']: block_pick = 3

    if held_keys['4']: block_pick = 4





class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)




class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)

class Item(Entity):

    def __int__(self):
        super().__int__(
            parent = camera.ui,
            model = 'cube',
            texture = grass_texture,
            scale = 0.2,
            #rotation = Vec3(130,-10,0),
            #position = Vec2(0.4, -0.6)
        )


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

def input(key):
    if key == "escape":
        # Escape Key Pressed Quit.
        quit()

player = FirstPersonController()
sky = Sky()
hand = Hand()
item = Item()


app.run()

# I am very dissapointed with myself as there is basically nothing to show besides the code that was gotten from the source. I could not figure out how to do any of these additions in time for the project to be done
# I will continue to work on this after the semester.


#for this project, I want to create an inventory that you can have with different materials that you can put
#into a toolbar that will be on in the player's perspective at all times.
#I also want to have it so that whatever item you have selected in the toolbar will also be in the player's hand.
#I am going to try, hopefully to make it so it takes a different amount of time to break a block instead of instantaneously
#destroying the block.