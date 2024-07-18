from turtle import Turtle
POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
DIRECTION=[0,90,180,270]
UP=90
RIGHT=0
LEFT=180
DOWN=270
class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()

        self.head=self.snake[0]



    def create_snake(self):
        for i in POSITION:
            self.add_segment(i)

    def move(self):
        for j in range(len(self.snake)-1,0,-1):
            nx=self.snake[j-1].xcor()
            ny=self.snake[j-1].ycor()
            self.snake[j].goto(nx,ny)

        self.snake[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]
    def add_segment(self,i):
        segment = Turtle('square')
        segment.color("white")
        segment.penup()
        segment.goto(i)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())


