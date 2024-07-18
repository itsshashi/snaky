from turtle import Turtle
ALIGNMENT= 'center'
FONT=('Arial', 15, 'bold')
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.color('white')
        with open("data.txt") as file:
            self.highscore=int(file.read())
        self.score=0
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}   High score={self.highscore}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score+=1

        self.update_score()
    # def game_over(self):
    #
    #     self.goto(0,0)
    #     self.write('Game Over',align=ALIGNMENT,font=FONT)
    def reset(self):
        if self.score>self.highscore:#to keep track high score using local files

            self.highscore=self.score
            with open("data.txt",mode="w") as file:
                file.write(self.score)
        self.score=0
        self.update_score()