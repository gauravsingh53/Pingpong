import turtle

# Window setup
wn = turtle.Screen()
wn.title("Fast Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball 🔴 (FAST)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)

# 🔥 High starting speed
ball.dx = 1.2
ball.dy = 1.2

# Score
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("A: 0  B: 0", align="center", font=("Courier", 24, "normal"))

# Controls
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 25)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 25)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 25)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 25)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Game loop
def game_loop():
    global score_a, score_b

    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top/Bottom collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Right wall
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"A: {score_a}  B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Left wall
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"A: {score_a}  B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle collision + 🔥 speed boost
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1.3
        ball.dy *= 1.3

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1.3
        ball.dy *= 1.3

    # 🚫 Speed limit (very high)
    if abs(ball.dx) > 6:
        ball.dx = 6 if ball.dx > 0 else -6

    if abs(ball.dy) > 6:
        ball.dy = 6 if ball.dy > 0 else -6

    # Faster refresh (smooth fast game)
    wn.ontimer(game_loop, 5)

# Start game
game_loop()
wn.mainloop()