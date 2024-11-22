import turtle

# Setup layar turtle
screen = turtle.Screen()
screen.bgcolor("white")

# Membuat objek turtle
pen = turtle.Turtle()
pen.speed(5)

# Fungsi untuk menggambar persegi panjang dengan warna tertentu
def draw_rectangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Gambar bendera Indonesia
# Gambar bagian merah
draw_rectangle("red", -150, 100, 150, 50)

# Gambar bagian putih
draw_rectangle("white", -150, 50, 150, 50)

# Menyembunyikan turtle setelah gambar selesai
pen.hideturtle()

# Menunggu sampai jendela ditutup
turtle.done()