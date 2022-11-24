import pyray as pr 
import time
import random

from player import Player
from enemy import Enemy

pr.init_window(1080, 720, "History Wars")
pr.init_physics()

canvas = pr.load_render_texture(1080, 720)


miumen = Player(680, 720)

Enemies = []

n = random.randint(5, 5)

for i in range (1, n + 1):
    Enemies.append(Enemy(i * 70, 720 - 70, miumen))

old_time = time.time()

while not pr.window_should_close():
    if miumen.health > 0:
        new_time = time.time()
        dt = new_time - old_time
        old_time = new_time

        dKey = pr.is_key_down(68)
        aKey = pr.is_key_down(65)
        spaceKey = pr.get_key_pressed()

        if pr.is_mouse_button_pressed(0):
            attack_x = pr.get_mouse_x()

            if attack_x > miumen.x:
                # Right 

                mins = []

                for en in Enemies:
                    if en.x > miumen.x:
                        d = en.x - miumen.x 

                        if d <= miumen.range:
                            mins.append([d, en])               

                if len(mins) >= 1:
                    m = mins[0][0]
                    g = mins[0][1]

                    for i in mins:
                        if i[0] < m:
                            g = i[1]


                    miumen.attack(g)

            else:
                mins = []

                for en in Enemies:
                    if en.x < miumen.x:
                        d = miumen.x - en.x

                        if d <= miumen.range:
                            mins.append([d, en]) 

                if len(mins) >= 1:
                    m = mins[0][0]
                    g = mins[0][1]

                    for i in mins:
                        if i[0] < m:
                            g = i[1]


                    miumen.attack(g)

        if dKey:
            miumen.move(0.15, 0)

        elif aKey:
            miumen.move(-0.15, 0)

        if spaceKey == 32:
            miumen.move(0, -300)

        miumen.update(dt, Enemies)

        pr.clear_background(pr.WHITE)

        pr.begin_texture_mode(canvas)
        pr.set_texture_filter(canvas.texture, 0)
        pr.end_texture_mode()
        pr.begin_drawing()   

        Player_Rec = pr.Rectangle(miumen.x, miumen.y, 30, 90)
        pr.draw_rectangle_lines_ex(Player_Rec, 5.0, pr.BLACK)

        for en in Enemies:
            en.update(Enemies)
            
            Enemy_Rec = pr.Rectangle(en.x, en.y, en.width, en.height)
            pr.draw_rectangle_lines_ex(Enemy_Rec, 5.0, pr.RED) 
            pr.draw_text(str(en.health), int(en.x + (en.width // 2)), int(en.y - 10), 10, pr.BLACK)

        pr.draw_text(str(miumen.health), 20, 30, 22, pr.BLACK)

        pr.end_drawing()

    else:
        pr.begin_drawing()
        pr.draw_text("You Died!", 1080 //2 - (pr.measure_text("You Died!", 120) // 2), 720 //2, 120, pr.BLACK)

        pr.end_drawing()
    
