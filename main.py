import pyray as pr 
import time

from player import Player
from enemy import Enemy

pr.init_window(1080, 720, "History Wars")
pr.init_physics()

miumen = Player(100, 500)
Enemies = [Enemy(10, 720 - 70, miumen)]

old_time = time.time()

while not pr.window_should_close():
    new_time = time.time()
    dt = new_time - old_time
    old_time = new_time

    dKey = pr.is_key_down(68)
    aKey = pr.is_key_down(65)
    spaceKey = pr.get_key_pressed()

    if pr.is_mouse_button_down(0):
        attack_x = pr.get_mouse_x()
        print('!')

    if dKey:
        miumen.move(0.3, 0)

    elif aKey:
        miumen.move(-0.3, 0)

    if spaceKey == 32:
        miumen.move(0, -100)

    

    miumen.update(1)

    pr.clear_background(pr.WHITE)

    pr.begin_drawing()   

    Player_Rec = pr.Rectangle(miumen.x, miumen.y, 30, 90)
    pr.draw_rectangle_lines_ex(Player_Rec, 5.0, pr.BLACK)

    for en in Enemies:
        en.update()
        
        Enemy_Rec = pr.Rectangle(en.x, en.y, 30, 70)
        pr.draw_rectangle_lines_ex(Enemy_Rec, 5.0, pr.RED)    

    pr.end_drawing()