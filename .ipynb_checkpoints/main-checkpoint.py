class PointGround:
    def __init__(self , x, y):
        self.x = x
        self.y = y      #constructor
    def move(self):
        print('move here')

    def draw(self):
        print("draw here")
        print('lets go home')


class Point(PointGround):    # inheritance
    pass                           #you can define a new method here


class Ground(PointGround):
    pass


point1 = Point(10,20)
point1.draw()




