class Mars:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Mars initiated with size: " + str(Mars.getX(self)) + ", " + str(Mars.getY(self)))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

