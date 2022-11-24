from pyray import physics_add_force, PhysicsBodyData, create_physics_body_rectangle, get_physics_bodies_count, get_physics_body, get_physics_shape_vertices_count, get_physics_shape_vertex, Vector2

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

        self.width = 30.0
        self.height = 90.0

        self.vel = [0, 0]
        self.acc = [0, 0]

        self.health = 100

    def attack(self):
        pass

    def move(self, x, y):
        self.x += x
        self.y += y

    def update(self, dt, ens):
        # Gravity
        if self.y < 720:
            self.move(0, 0.098)

        if self.y >= 720 - self.height:
            self.y = 720 - self.height

        if self.x >= 1080 - self.width:
            self.x = 1080 - self.width

        if self.x <= 0:
            self.x = 0
        
        if self.y <= 0:
            self.y = 0
