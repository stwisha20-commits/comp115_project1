"""
COMP115 PROJECT-1
 I have made the project by making night sky + moon + stars + clouds + grass + house + flowers + butterfly!!

Name: Twisha Sharma
"""

import turtle


screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("midnightblue")
screen.title("COMP115 Project")
screen.tracer(False)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)


def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def circ(x, y, r, color):
    t.color(color)
    t.fillcolor(color)
    move(x, y - r)
    t.setheading(0)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def rect_top_left(x, y, w, h, color):
    
    t.color(color)
    t.fillcolor(color)
    move(x, y)
    t.setheading(0)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

def triangle(p1, p2, p3, color):
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    move(p1[0], p1[1])
    t.goto(p2[0], p2[1])
    t.goto(p3[0], p3[1])
    t.goto(p1[0], p1[1])
    t.end_fill()
    t.setheading(0)


# Sky

def moon(x, y):
    circ(x, y, 42, "#f6f1c1")
    circ(x + 16, y + 8, 42, "midnightblue") 

def star(x, y, s):
    t.color("white")
    move(x, y)
    t.setheading(0)
    for _ in range(4):
        t.forward(s)
        t.backward(s)
        t.left(90)
    for ang in [45, 135]:
        t.setheading(ang)
        t.forward(s)
        t.backward(s)
    t.setheading(0)

def cloud(x, y):
    circ(x, y, 16, "white")
    circ(x + 22, y + 8, 18, "white")
    circ(x + 46, y, 16, "white")

def draw_sky():
    moon(360, 250)

    
    cloud(-420, 285)
    cloud(-90, 315)
    cloud(240, 295)

    
    stars_pos = [(-450, 210), (-300, 330), (-180, 260), (20, 340),
                 (150, 320), (430, 210), (470, 300), (-60, 360)]
    for i, (x, y) in enumerate(stars_pos):
        size = 10 if i % 2 == 0 else 7
        star(x, y, size)


# Ground

def draw_grass():
    
    rect_top_left(-500, -40, 1000, 330, "#0b8a3b")


# House

def roof_heart(cx, cy):
    
    circ(cx - 20, cy, 22, "#ffb0c8")
    circ(cx + 20, cy, 22, "#ffb0c8")
    triangle((cx - 40, cy), (cx + 40, cy), (cx, cy - 55), "#ffb0c8")

def draw_house():
    ground_y = -40

    
    base_w, base_h = 320, 220
    base_left = -base_w / 2
    base_top = ground_y + base_h
    rect_top_left(base_left, base_top, base_w, base_h, "#ff3b5c")

    
    triangle((base_left - 35, base_top),
             (0, base_top + 170),
             (base_left + base_w + 35, base_top),
             "#8e1cff")
    roof_heart(0, base_top + 115)

    
    door_w, door_h = 95, 140
    door_left = -door_w / 2
    door_top = ground_y + door_h
    rect_top_left(door_left, door_top, door_w, door_h, "#ff9ab3")
    circ(door_left + door_w - 16, ground_y + door_h / 2, 7, "white")


# Flowers 

def draw_flower(x, y, petal_color, center_color):
    
    t.color("#1f8a3b")
    t.pensize(6)
    move(x, y)
    t.setheading(90)
    t.forward(40)
    t.pensize(3)

    
    cx, cy = x, y + 40
    petal_r = 9
    ring_r = 16  

    for ang in [0, 60, 120, 180, 240, 300]:
        t.setheading(ang)
        
    offsets = [(ring_r, 0), (ring_r/2, ring_r*0.87), (-ring_r/2, ring_r*0.87),
               (-ring_r, 0), (-ring_r/2, -ring_r*0.87), (ring_r/2, -ring_r*0.87)]

    for dx, dy in offsets:
        circ(cx + dx, cy + dy, petal_r, petal_color)

    
    circ(cx, cy, 7, center_color)

def draw_flowers():
    spots = [(-420, -170), (-280, -210), (-140, -180),
             (0, -230), (140, -180), (280, -210), (420, -170)]
    petals = ["#ff7aa8", "#ffd166", "#b4f8c8", "#cdb4ff"]
    centers = ["#ffd000", "#ffee32", "#ffb703", "#fff2a6"]

    for i, (x, y) in enumerate(spots):
        draw_flower(x, y, petals[i % 4], centers[i % 4])


# Butterfly 

def draw_butterfly(cx, cy):
    
    circ(cx - 18, cy + 8, 14, "#7dd3ff")
    circ(cx + 18, cy + 8, 14, "#7dd3ff")
    circ(cx - 20, cy - 6, 12, "dodgerblue")
    circ(cx + 20, cy - 6, 12, "dodgerblue")

    body_w, body_h = 10, 55
    rect_top_left(cx - body_w/2, cy + 22, body_w, body_h, "#1b1b1b")

    
    t.color("#1b1b1b")
    move(cx, cy + 22)
    t.setheading(120); t.forward(15)
    move(cx, cy + 22)
    t.setheading(60);  t.forward(15)
    t.setheading(0)


def main():
    draw_sky()
    draw_grass()
    draw_house()
    draw_flowers()
    draw_butterfly(0, -230)

    screen.tracer(True)
    screen.update()
    screen.mainloop()

main()