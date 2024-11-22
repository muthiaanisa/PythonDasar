import turtle

# Fungsi untuk menggambar Fibonacci Tree
def fibonacci_tree(length, level):
    if level == 0 or length < 10:  # Hentikan jika level 0 atau panjang terlalu kecil
        return
    
    # Gambar batang utama
    turtle.forward(length)
    
    # Simpan posisi dan arah
    position = turtle.pos()
    heading = turtle.heading()
    
    # Cabang kiri
    turtle.left(30)
    fibonacci_tree(length * 0.7, level - 1)
    
    # Kembali ke posisi dan arah semula
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()
    
    # Cabang kanan
    turtle.right(30)
    fibonacci_tree(length * 0.7, level - 1)
    
    # Kembali ke posisi awal batang
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()

# Setup awal Turtle
turtle.speed(0)  # Kecepatan maksimal
turtle.left(90)  # Arahkan ke atas
turtle.penup()
turtle.goto(0, -200)  # Posisi awal di bawah
turtle.pendown()
turtle.color("green")

# Menggambar Fibonacci Tree
fibonacci_tree(100, 5)  # Panjang batang 100, level rekursi 5

# Selesaikan gambar
turtle.hideturtle()
turtle.done()