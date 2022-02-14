import imp
from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]
snake_body= []
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():
    def __init__(self):
        self.full_body = []
        self.create_snake()
        self.head  = self.full_body[0]
    
    def create_snake(self):
        for pos in STARTING_POS:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(pos)
            self.full_body.append(new_segment)

    
    def snake_move(self):
        for seg_num in range(len(self.full_body)-1,0,-1):
            new_x = self.full_body[seg_num-1].xcor()
            new_y = self.full_body[seg_num-1].ycor()
            self.full_body[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_grow_up(self):
        # add new seg ment to snake
        self.add_segment(self.full_body[-1].position())

    def add_segment(self,position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.full_body.append(new_segment)
    
    def reset(self):
        for segment in self.full_body:
            segment.goto(1000,1000)
        self.full_body.clear()
        self.create_snake()
        self.head = self.full_body[0]
        


