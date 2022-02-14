from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial',20,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score  = 0
        self.color('white') # chagng different from screen color
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.load_high_score()
        self.update_scoreboard()
        
    def load_high_score(self):
        with open('highscore.txt','r') as f :
            self.high_score = int(f.read())
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score} ",align=ALIGNMENT,font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.clear()
    #     self.write(arg= "GAME OVER" ,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt','r+') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

