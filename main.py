import pyray as pr 
import time
import random

from player import Player
from enemy import Enemy

pr.init_window(1080, 720, "History Wars")
pr.init_audio_device()

# Images
roman_img = pr.load_image("assets/images/roman_solder.png")
character_img = pr.load_image("assets/images/character-cloths.png")
wooden_sword_img = pr.load_image("assets/images/wooden_sword.png")
sun_img = pr.load_image("assets/images/sun.png")
grass_img = pr.load_image("assets/images/grass.png")
tree_img = pr.load_image("assets/images/tree.png")
tree2_img = pr.load_image("assets/images/tree2.png")
tree3_img = pr.load_image("assets/images/tree3.png")

pr.image_resize(roman_img, int(roman_img.width // 2), int(roman_img.height // 2))
pr.image_resize(character_img, int(character_img.width // 1.87), int(character_img.height // 1.87))
pr.image_resize(wooden_sword_img, int(wooden_sword_img.width // 4.3), int(wooden_sword_img.height // 4.3))
pr.image_resize(sun_img, int(sun_img.width // 1.3), int(sun_img.height // 1.3))
pr.image_resize(grass_img, int(grass_img.width // 5), int(grass_img.height // 5))
pr.image_resize(tree_img, int(tree_img.width // 1.9), int(tree_img.height // 1.9))
pr.image_resize(tree2_img, int(tree2_img.width // 2.5), int(tree2_img.height // 2.5))
pr.image_resize(tree3_img, int(tree3_img.width // 2.1), int(tree3_img.height // 2.1))

roman_tx = pr.load_texture_from_image(roman_img)
character_tx = pr.load_texture_from_image(character_img)
wooden_sword_tx = pr.load_texture_from_image(wooden_sword_img)
sun_tx = pr.load_texture_from_image(sun_img)
grass_tx = pr.load_texture_from_image(grass_img)
tree_tx = pr.load_texture_from_image(tree_img)
tree2_tx = pr.load_texture_from_image(tree2_img)
tree3_tx = pr.load_texture_from_image(tree3_img)

pr.unload_image(roman_img)
pr.unload_image(sun_img)

# Sounds
sword_sfx = pr.load_sound("assets/sounds/sword.mp3")

# Vars
miumen = Player(900, 705)
sword_x, sword_y = miumen.x, miumen.y

Enemies = []

n = 1

for i in range (1, n + 1):
    en = Enemy(i * 25, 705 - 70 , miumen)
    en.attack_sound = sword_sfx

    Enemies.append(en)

old_time = time.time()

rotated = False
# 1 = Left 2 = Right
player_dir = 1

while not pr.window_should_close():
    if miumen.health > 0:
        new_time = time.time()
        dt = new_time - old_time
        old_time = new_time

        dKey = pr.is_key_down(68)
        aKey = pr.is_key_down(65)
        spaceKey = pr.get_key_pressed()

        if pr.get_mouse_x() > miumen.x:
            Right_x = 25

            if not rotated:
                for i in range(3):
                    pr.image_rotate_ccw(wooden_sword_img)

                wooden_sword_tx = pr.load_texture_from_image(wooden_sword_img)

                rotated = True

        else:
            Right_x = -38
            
            if rotated:
                pr.image_rotate_ccw(wooden_sword_img)
                wooden_sword_tx = pr.load_texture_from_image(wooden_sword_img)

                rotated = False

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
            if player_dir != 2:
                pr.image_flip_horizontal(character_img)

                character_tx = pr.load_texture_from_image(character_img)
                player_dir = 2

            miumen.move(0.11, 0)

        elif aKey:
            if player_dir != 1:
                pr.image_flip_horizontal(character_img)

                character_tx = pr.load_texture_from_image(character_img)
                player_dir = 1                
            
            miumen.move(-0.11, 0)

        if spaceKey == 32:
            miumen.jump(300)

        pr.clear_background(pr.WHITE)

        pr.end_texture_mode()
        pr.begin_drawing()   

        miumen.update(dt, Enemies)

        sword_x = miumen.x
        sword_y = miumen.y
        

        pr.draw_texture(tree3_tx, 200, 705 - tree3_img.height, pr.WHITE)
        pr.draw_texture(tree2_tx, 350, 705 - tree2_img.height, pr.WHITE)
        pr.draw_texture(tree_tx, 570, 705 - 277, pr.WHITE)
        pr.draw_texture(tree3_tx, 720, 705 - tree3_img.height, pr.WHITE)
        pr.draw_texture(tree2_tx, 1080, 705 - tree2_img.height, pr.WHITE)
        pr.draw_texture(tree_tx, 50, 705 - 277, pr.WHITE)
        pr.draw_texture(tree_tx, 900, 705 - 277, pr.WHITE)   

        
        for i in range(1080 // grass_img.width + 1):
            pr.draw_texture(grass_tx, i * grass_tx.width, 680, pr.WHITE)     

        for en in Enemies:
            en.update(Enemies)

            pr.draw_texture(roman_tx, int(en.x), int(en.y - 55), pr.WHITE)            

        pr.draw_text(str(miumen.health), 20, 30, 22, pr.BLACK)
        pr.draw_texture(character_tx, int(miumen.x), int(miumen.y), pr.WHITE)
        pr.draw_texture(wooden_sword_tx, int(sword_x) + Right_x, int(sword_y) + 30, pr.WHITE)
        pr.draw_texture(sun_tx, 843, 7, pr.WHITE)        

        pr.end_drawing()
        pr.draw_text(str(pr.get_fps()), 40, 100, 22, pr.BLACK)

    else:
        pr.begin_drawing()
        pr.draw_text("You Died!", 1080 //2 - (pr.measure_text("You Died!", 120) // 2), 720 //2, 120, pr.BLACK)

        pr.end_drawing()

pr.unload_image(wooden_sword_img)
pr.unload_image(character_img)
