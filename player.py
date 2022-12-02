import time

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

        self.width = 33.0
        self.height = 120.0

        self.flip = 0

        self.health = 1000
        
        self.range = 40

        self.jump_cooldown = 1
        self.last_jump = 0
        self.jumping = False
        self.jumping_rate = 0

        self.image = ""

        self.knockbacking = False
        self.knockback_rate = 0
        self.knockback_direction = 1

    def attack(self, en):
        en.health -= 5

        if en.x > self.x:
            en.x += 100
            en.stop = True

        else:
            en.x -= 100
            en.stop = True

    def move(self, x, y):
        if x < self.x:
            self.flip = -1
        else:
            self.flip = 0

        self.x += x
        self.y += y

    def jump(self, y):
        t = time.time()

        if self.last_jump != 0:
            if t - self.last_jump > self.jump_cooldown:
                self.last_jump = t
                self.jumping = True
                self.jumping_rate = y

                self.last_jump = t

        else:
            self.last_jump = t
            self.jumping = True
            self.jumping_rate = y   

    def knockback(self, knock, direction):
        self.knockbacking = True
        self.knockback_rate = knock
        self.knockback_direction = direction

    def update(self, dt, ens):
        # Gravity

        if self.jumping:
            if self.jumping_rate > 0:
                self.move(0, -0.5)
                self.jumping_rate -= 1

            else:
                self.jumping = False
                self.jumping_rate = 0

        if self.knockbacking:
            if self.knockback_rate > 0:
                self.move( 0.5 * self.knockback_direction, 0)

                self.knockback_rate -= 1

            else:
                self.knockbacking = False
                self.knockback_rate = 0
                self.knockback_direction = 1

        if self.y < 705:
            self.move(0, 0.098)

        if self.y >= 705 - self.height:
            self.y = 705 - self.height

        if self.x >= 1080 - self.width:
            self.x = 1080 - self.width

        if self.x <= 0:
            self.x = 0
        
        if self.y <= 0:
            self.y = 0
