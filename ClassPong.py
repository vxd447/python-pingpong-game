# Importing Modules

import turtle           # Module for Graphics
import winsound         # Module for Sound

# Class for the Paddle 
class Paddle:

    # Constructor of the Paddle
    def __init__(self, speed, color, wid, len, posx, posy):
        self.paddle = turtle.Turtle()
        self.paddle.speed(speed)
        self.paddle.shape('square')
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=wid, stretch_len=len)
        self.paddle.penup()
        self.paddle.goto(posx, posy)
        self.score = 0

    # Increment the Score for the Paddle
    def increment(self):
        self.score += 1

    # Move the paddle UP
    def move_up(self):
        y = self.paddle.ycor()
        if(y < 350): y += 20
        self.paddle.sety(y)

    # Move the paddle DOWN
    def move_down(self):
        y = self.paddle.ycor()
        if(y > -340): y -= 20
        self.paddle.sety(y)


# Class for the Ball
class Ball:

    # Constructor of the Ball
    def __init__(self, speed, color, posx, posy):
        self.obj = turtle.Turtle()
        self.obj.speed(0)
        self.obj.shape('circle')
        self.obj.color(color)
        self.obj.penup()
        self.obj.goto(posx, posy)
        self.obj.dx = 0.5
        self.obj.dy = 0.5

    # Move Ball to the next position
    def next_move(self):
        self.obj.setx(self.obj.xcor() + self.obj.dx)
        self.obj.sety(self.obj.ycor() + self.obj.dy)

    # Refect the Ball by the left or right Wall
    def reflect_X(self, posx):
        self.obj.setx(posx)
        self.obj.dx *= -1

    # Reflect the Ball by the top or bottom wall
    def reflect_Y(self, posy):
        self.obj.sety(posy)
        self.obj.dy *= -1
    
    # Reset the Ball at Initial Position
    def reset(self):
        self.obj.goto(0, 0)
        self.obj.dx *= -1


# Class for the Game
class Game:

    # Constructor for the Game
    def __init__(self, sizex, sizey):
        self.createScreen(sizex, sizey)     # Create the Window
        self.createPaddles()                # Create the Paddle
        self.createBall()                   # Create the Ball   
        self.createScoreBoard()             # Create the Scoreboard
        self.keyBindings()                  # Key Binding
        self.play()                         # Start the Game

    # Creates the Screen
    def createScreen(self, sizex, sizey):
        self.window = turtle.Screen()
        self.window.title('Ping Pong Game')
        self.window.bgcolor('black')
        self.window.screensize(sizex, sizey)
        self.window.setup(width = 1.0, height = 1.0, startx = None, starty = None)
        self.window.tracer(0)

    # Create the Paddles
    def createPaddles(self):
        self.paddle_a = Paddle(0, 'white', 6, 0.5, -650, 0)
        self.paddle_b = Paddle(0, 'white', 6, 0.5, 650, 0)

    # Create the Ball
    def createBall(self):
        self.ball = Ball(0, 'white', 0, 0)

    # Create the Score Board
    def createScoreBoard(self):
        self.board = turtle.Turtle()
        self.board.speed(0)
        self.board.color('white')
        self.board.penup()
        self.board.hideturtle()
        self.board.goto(0, 350)
        self.board.write(f'Player A: {self.paddle_a.score}  Player B: {self.paddle_b.score}',align='center', font=('Courier', 24, 'normal'))

    # Update the Score Board
    def updateScoreBoard(self):
        self.board.clear()
        self.board.write(f'Player A: {self.paddle_a.score}  Player B: {self.paddle_b.score}',align='center', font=('Courier', 24, 'normal'))

    # Key Bindings
    def keyBindings(self):
        self.window.listen()
        self.window.onkeypress(self.paddle_a.move_up, 'w')
        self.window.onkeypress(self.paddle_a.move_down, 's')
        self.window.onkeypress(self.paddle_b.move_up, 'Up')
        self.window.onkeypress(self.paddle_b.move_down, 'Down')

    # Play the Poing Sound
    def playSound(self):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)        

    # Starts the Game
    def play(self):
        while True:
            # Update the Screen
            self.window.update()

            # Move the Ball to next position
            self.ball.next_move()

            # If ball reaches the TOP
            if (self.ball.obj.ycor() > 350):
                self.ball.reflect_Y(350)
                self.playSound()

            # If ball reaches the BOTTOM
            if (self.ball.obj.ycor() < -350):
                self.ball.reflect_Y(-350)
                self.playSound()
            
            # If ball reaches the RIGHT
            if (self.ball.obj.xcor() > 650):
                self.paddle_a.increment()
                self.updateScoreBoard()
                self.ball.reset()

            # If ball reaches the LEFT
            if(self.ball.obj.xcor() < -650):
                self.paddle_b.increment()
                self.updateScoreBoard()
                self.ball.reset()

            # If ball reaches the RIGHT Paddle
            if(self.ball.obj.xcor() > 640 and self.ball.obj.xcor() < 650) and (self.ball.obj.ycor() < self.paddle_b.paddle.ycor() + 60 and self.ball.obj.ycor() > self.paddle_b.paddle.ycor() - 70):
                self.ball.reflect_X(640)
                self.playSound()

            # If ball reaches the LEFT Paddle
            if(self.ball.obj.xcor() < -640 and self.ball.obj.xcor() > -650) and (self.ball.obj.ycor() < self.paddle_a.paddle.ycor() + 60 and self.ball.obj.ycor() > self.paddle_a.paddle.ycor() - 70):
                self.ball.reflect_X(-640)
                self.playSound()

if(__name__ == "__main__"):
    Game(1280, 720)
