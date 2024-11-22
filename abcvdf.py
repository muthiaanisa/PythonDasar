import turtle

# Fungsi untuk menggambar persegi panjang
def gambar_persegi_panjang():
    turtle.penup()
    turtle.goto(-150, 50)  # Pindahkan posisi awal
    turtle.pendown()
    for _ in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

# Fungsi untuk menggambar segitiga
def gambar_segitiga():
    turtle.penup()
    turtle.goto(100, 100)  # Pindahkan posisi awal
    turtle.pendown()
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

# Fungsi untuk menggambar trapezium
def gambar_trapezium():
    turtle.penup()
    turtle.goto(-200, -150)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(100)

# Fungsi untuk menggambar jajar genjang
def gambar_jajar_genjang():
    turtle.penup()
    turtle.goto(-200, 250)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.forward(150)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(150)
    turtle.left(60)
    turtle.forward(100)

# Fungsi untuk menggambar belah ketupat
def gambar_belah_ketupat():
    turtle.penup()
    turtle.goto(150, -100)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)

# Menyiapkan layar turtle
turtle.speed(2)  # Mengatur kecepatan menggambar

# Gambar bangun datar
gambar_persegi_panjang()
gambar_segitiga()
gambar_trapezium()
gambar_jajar_genjang()
gambar_belah_ketupat()

# Menyembunyikan kursor turtle setelah menggambar
turtle.hideturtle()

# Menunggu sampai klik pada jendela untuk keluar
turtle.done()