from turtle import Turtle,Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake


screen=Screen()
screen .setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
position=[(0,0),(-20,0),(-40,0)]
segment=[]
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



is_game_start=True
while is_game_start:
    screen.update()
    time.sleep(0.17)
    snake.move()



    if snake.head.distance(food)<13:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        is_game_start=False
        scoreboard.game_over()
    #detection collision with  tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) <10:
            is_game_start=False
            scoreboard.game_over()
screen.exitonclick()