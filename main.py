import pyray as pr 
import time
import random

from player import Player
from enemy import Enemy

pr.init_window(1080, 720, "History Wars")
pr.init_audio_device()

miumen = Player(900, 720)

roman_img = pr.load_image("assets/images/roman_solder.png")
character_img = pr.load_image("assets/images/character-cloths.png")

pr.image_resize(roman_img, int(roman_img.width // 2), int(roman_img.height // 2))
pr.image_resize(character_img, int(character_img.width // 1.87), int(character_img.height // 1.87))

print(character_img.width, character_img.height)

roman_tx = pr.load_texture_from_image(roman_img)
character_tx = pr.load_texture_from_image(character_img)

pr.unload_image(roman_img)
pr.unload_image(character_img)

sword_sfx = pr.load_sound("assets/sounds/sword.mp3")

Enemies = []

n = 1

for i in range (1, n + 1):
    en = Enemy(i * 25, 720 - 70, miumen)
    en.attack_sound = sword_sfx

    Enemies.append(en)

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
            miumen.move(0.11, 0)

        elif aKey:
            miumen.move(-0.11, 0)

        if spaceKey == 32:
            miumen.jump(300)

        pr.clear_background(pr.WHITE)

        pr.end_texture_mode()
        pr.begin_drawing()   

        miumen.update(dt, Enemies)

        for en in Enemies:
            en.update(Enemies)

            pr.draw_texture(roman_tx, int(en.x), int(en.y - 55), pr.WHITE)            

        pr.draw_text(str(miumen.health), 20, 30, 22, pr.BLACK)
        pr.draw_texture(character_tx, int(miumen.x), int(miumen.y), pr.WHITE)

        pr.end_drawing()

    else:
        pr.begin_drawing()
        pr.draw_text("You Died!", 1080 //2 - (pr.measure_text("You Died!", 120) // 2), 720 //2, 120, pr.BLACK)

        pr.end_drawing()
    
