import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")

# Setup pen
pen = turtle.Turtle()
pen.speed(5)

# Fungsi untuk menggambar bentuk logo TikTok
def draw_tiktok_logo():
    # Gambar lingkaran hitam (bagian utama)
    pen.penup()
    pen.goto(-40, 0)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("black")
    pen.circle(80)
    pen.end_fill()

    # Gambar bentuk "not musik" biru
    pen.penup()
    pen.goto(10, 40)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("#69b3e7")  # Biru muda
    pen.setheading(45)
    pen.circle(60, 90)
    pen.setheading(0)
    pen.forward(40)
    pen.setheading(-90)
    pen.circle(40, 90)
    pen.setheading(0)
    pen.forward(20)
    pen.end_fill()

    # Gambar bagian kedua bentuk "not musik" putih
    pen.penup()
    pen.goto(-25, 20)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("white")
    pen.setheading(0)
    pen.circle(80, 90)
    pen.end_fill()

# Gambar logo TikTok
draw_tiktok_logo()

# Selesai
pen.hideturtle()
turtle.done()

