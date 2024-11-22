
    pen.goto(50, 140)
    pen.goto(70, 90)
    pen.end_fill()

# Fungsi untuk menggambar kumis kucing
def draw_whiskers():
    # Kumis kiri atas
    pen.penup()
    pen.goto(-80, 30)
    pen.setheading(180)
    pen.pendown()
    pen.forward(50)

    # Kumis kiri bawah
    pen.penup()
    pen.goto(-80, 10)
    pen.setheading(180)
    pen.pendown()
    pen.forward(50)

    # Kumis kanan atas
    pen.penup()
    pen.goto(80, 30)
    pen.setheading(0)
    pen.pendown()
    pen.forward(50)

    # Kumis kanan bawah
    pen.penup()
    pen.goto(80, 10)
    pen.setheading(0)
    pen.pendown()
    pen.forward(50)

# Fungsi utama untuk menggambar kucing garong
def draw_cat():
    draw_head()
    draw_eyes()
    draw_nose()
    draw_mouth()
    draw_ears()
    draw_whiskers()

# Gambar kucing
draw_cat()

# Selesai
pen.hideturtle()
turtle.done()
