from tkinter import Tk, Frame, Canvas, BOTH
import math
import random

def main():
    width = 800
    height = 600

    root = Tk()
    root.geometry(f"{width}x{height}")

    frame = Frame()
    frame.master.title("Scene")
    frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):

    draw_sky(canvas, 0, 0, 799, 599)

    draw_sun(canvas, 100, 100)

    for _ in range(25):
        cloud_left = random.randint(200, 500)
        cloud_top = random.randint(0, 150)
        cloud_width = 100
        cloud_height = 75
        draw_clouds(canvas, cloud_left, cloud_top, cloud_width, cloud_height)

    draw_ground(canvas, 0, 500, 799, 599)

    draw_fence_posts(canvas, 0, 300, 25, 500)
    draw_fence_posts(canvas, 150, 300, 175, 500) 
    draw_fence_posts(canvas, 300, 300, 325, 500)
    draw_fence_posts(canvas, 450, 300, 475, 500)
    draw_fence_posts(canvas, 600, 300, 625, 500)
    draw_fence_posts(canvas, 750, 300, 775, 500)

    draw_fence_cross(canvas, 0, 325, 799, 350)
    draw_fence_cross(canvas, 0, 425, 799, 450)

    for _ in range(100):
        blade_left = random.randint(scene_left, scene_right)
        blade_top = random.randint(450, 500)
        blade_width = 5
        blade_height = 175
        draw_grass(canvas, blade_left, blade_top, blade_width, blade_height)

def draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_rectangle(scene_left, scene_top, scene_right, scene_bottom, outline="#93ffff", width=0, fill="#93ffff")

def draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_rectangle(scene_left, scene_top, scene_right, scene_bottom, outline="#55311e", width=0, fill="#55311e")
    
def draw_sun(canvas, sun_left, sun_top):
    sun_width = 125
    sun_height = 125
    ray_length = 100
    ray_width = 3
    ray_count = 50

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=ray_width, fill='orange')

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill='yellow', outline='orange')

def draw_grass(canvas, blade_left, blade_top, width, height):
    blade_right = blade_left + width
    blade_bottom = 599
    canvas.create_rectangle(blade_left, blade_top, blade_right, blade_bottom, outline = 'green', fill = 'darkgreen')

def draw_fence_posts(canvas, post_left, post_top, post_right, post_bottom):
    canvas.create_rectangle(post_left, post_top, post_right, post_bottom, outline = 'grey', fill = 'white')

def draw_fence_cross(canvas, cross_left, cross_top, cross_right, cross_bottom):
    canvas.create_rectangle(cross_left, cross_top, cross_right, cross_bottom, outline = 'grey', fill = 'white')

def draw_clouds(canvas, cloud_left, cloud_top, width, height):
    cloud_right = cloud_left + width
    cloud_bottom = cloud_top + height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, outline = 'whitesmoke', fill = 'white')

main()