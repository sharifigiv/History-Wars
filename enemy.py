class Enemy:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y

        self.p = p
        self.speed = 0.1

    def attack (self):
        pass

    def update(self):
        if self.p.x > self.x and self.p.x - self.x > self.p.width + 2:
            self.x += self.speed

        if self.p.x < self.x and self.x - self.p.x > self.p.width + 2:
            self.x -= self.speed

