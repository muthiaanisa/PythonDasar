import turtle

# Fungsi untuk menggambar persegi panjang
def gambar_persegi_panjang():
    turtle.penup()
    turtle.goto(-300, 200)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.fillcolor("red")  # Warna isi merah
    turtle.begin_fill()  # Mulai pengisian warna
    for _ in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()  # Akhiri pengisian warna

# Fungsi untuk menggambar segitiga
def gambar_segitiga():
    turtle.penup()
    turtle.goto(-50, 150)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.fillcolor("yellow")  # Warna isi kuning
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(150)
        turtle.left(120)
    turtle.end_fill()

# Fungsi untuk menggambar trapezium
def gambar_trapezium():
    turtle.penup()
    turtle.goto(-280, 0)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.fillcolor("green")  # Warna isi hijau
    turtle.begin_fill()
    turtle.forward(200)  # Basis bawah
    turtle.left(120)
    turtle.forward(100)  # Sisi miring
    turtle.left(60)
    turtle.forward(150)  # Basis atas
    turtle.left(60)
    turtle.forward(100)  # Sisi miring
    turtle.left(120)
    turtle.end_fill()

# Fungsi untuk menggambar jajar genjang
def gambar_jajar_genjang():
    turtle.penup()
    turtle.goto(-50, 50)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.fillcolor("blue")  # Warna isi biru
    turtle.begin_fill()
    turtle.forward(200)  # Basis bawah
    turtle.left(60)
    turtle.forward(100)  # Sisi miring
    turtle.left(120)
    turtle.forward(200)  # Basis atas
    turtle.left(60)
    turtle.forward(100)  # Sisi miring
    turtle.left(120)
    turtle.end_fill()

# Fungsi untuk menggambar segilima
def gambar_segilima():
    turtle.penup()
    turtle.goto(-150, -200)  # Pindahkan posisi awal
    turtle.pendown()
    turtle.fillcolor("purple")  # Warna isi ungu
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(100)
        turtle.left(72)  # Sudut segilima
    turtle.end_fill()

# Menyiapkan layar turtle
turtle.speed(3)  # Mengatur kecepatan menggambar

# Memanggil fungsi untuk menggambar bangun datar
gambar_persegi_panjang()
gambar_segitiga()
gambar_trapezium()
gambar_jajar_genjang()
gambar_segilima()

# Menyembunyikan kursor turtle setelah menggambar
turtle.hideturtle()

# Menunggu sampai klik pada jendela untuk keluar
turtle.done()