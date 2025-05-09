from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        """乒乓球類別"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_up = 0.1
    
    def move(self):
        """乒乓球移動路徑"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """乒乓球與牆壁的反彈路徑"""
        self.y_move *= -1
    
    def bounce_x(self):
        '''乒乓球與球板的反彈路徑'''
        self.x_move *= -1
        self.speed_up *= 0.7

    def reset_position(self):
        """重新賽局並換邊發球"""
        self.speed_up = 0.1
        self.goto(0, 0)
        self.bounce_x()

        
