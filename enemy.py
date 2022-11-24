from pyray import Rectangle, Vector2, check_collision_recs, get_collision_rec
import time

class Enemy:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y

        self.p = p
        self.speed = 0.095
        self.health = 70

        self.width = 30.0
        self.height = 70.0

        self.range = 50
        self.damage = 10

        self.cooldown = False
        self.cooldown_count = 0
        self.cooldown_time = 2

    def attack (self):
        self.p.health -= self.damage

    def collision(self, ens, step):
        Colide = False

        for en in ens:
            if en != self:
                if not step:
                    rec1 = Rectangle(self.x + self.speed, self.y, self.width, self.height)

                if step:
                    rec1 = Rectangle(self.x - self.speed, self.y, self.width, self.height)

                rec2 = Rectangle(en.x, en.y, en.width, en.height)

                if check_collision_recs(rec2, rec1):
                    Colide = True
                    break

        if not Colide:
            return False

        else:
            return True

    def update(self, ens):
        if self.p.x > self.x and self.p.x - self.x > self.p.width + 2 and not self.collision(ens, False):
            self.x += self.speed

        if self.p.x < self.x and self.x - self.p.x > self.p.width + 2 and not self.collision(ens, True):
            self.x -= self.speed

        if self.health <= 0:
            self.x = 10000

        if self.p.x > self.x:
            if self.p.x - self.x <= self.range and not self.cooldown:
                self.attack() 

                self.cooldown = True
                self.cooldown_count = time.time()  

        else:
            if self.x - self.p.x <= self.range and not self.cooldown:
                self.attack() 

                self.cooldown = True
                self.cooldown_count = time.time()

        if self.cooldown:
            new_time = time.time()
            # print(new_time - self.cooldown_count)

            if (new_time - self.cooldown_count) >= self.cooldown_time:
                self.cooldown = False

                new_time = 0
                self.cooldown_count = 0

                
                        

