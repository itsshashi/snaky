
from turtle import Screen
from snake import Snake
from food import Food
from score import Score_board

import time
screen = Screen()
screen.title('SNAKE GAME')
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)
snake=[]

is_on=True

game=Snake()
food =Food()

screen.listen()
screen.onkey(game.up,"Up")
screen.onkey(game.left,"Left")
screen.onkey(game.right,"Right")
screen.onkey(game.down,"Down")
score=Score_board()
while is_on:
    game.head.color('white')

    screen.update()
    time.sleep(0.1)
    game.move()


# collision of ojects
    if game.head.distance(food) < 15:
        food.refresh()
        game.extend()
        score.increase_score()

    #detect boundary
    if game.head.xcor()>298 or game.head.xcor()<-298 or game.head.ycor()>298 or game.head.ycor()<-298:
        score.reset()
        
        game.reset()





    #detection collision with its body
    #uf head collide will tail game over

    for m in game.snake[1:]:

        if game.head.distance(m)<10:
            score.reset()
            game.reset()








screen.exitonclick()