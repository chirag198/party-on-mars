import operator

directions = ["N", "E", "S", "W"]


class Rover():
    rvrCount = 0  # initialize the count of rovers to 0.
    Mars = ""

    def __init__(self, x, y, direction):
        """
        Initialize a rover and increment the count of rovers by one (1).
        """
        self.direction = direction
        self.x = x
        self.y = y
        self.id = "Rover " + str(Rover.rvrCount)
        print("Rover initiated on {} {} facing {}".format(str(self.x), str(self.y),
                                                            self.direction))

    direction = property(operator.attrgetter('_direction'))

    @direction.setter
    def direction(self, d):
        if d.upper() not in directions: raise Exception("Direction not correct, use 'N, E, S or W'")
        self._direction = d.upper()

    x = property(operator.attrgetter('_x'))

    @x.setter
    def x(self, x):
        if (x < 0 or x > Rover.Mars.getX()): raise Exception(
            "This rover's x-value is out of bounds. It should be value should be < 0 and > " + str(Rover.Mars.getX()))
        self._x = x

    y = property(operator.attrgetter('_y'))

    @y.setter
    def y(self, y):
        if (y < 0 or y > Rover.Mars.getY()): raise Exception(
            "This rover's y-value is out of bounds. It should be value should be < 0 and > " + str(Rover.Mars.getY()))
        self._y = y

    def getDirection(self):
        return self.direction

    def getPosition(self):
        return str(self.x) + " " + str(self.y)

    def turnRight(self):
        self.direction = directions[0] if directions.index(self._direction) == 3 else directions[
            directions.index(self._direction) + 1]

    def turnLeft(self):
        self.direction = directions[3] if directions.index(self._direction) == 0 else directions[
            directions.index(self._direction) - 1]

    def forward(self):
        if self._direction == "N":
            self.y = self._y + 1
        elif self._direction == "S":
            self.y = self._y - 1
        elif self._direction == "E":
            self.x = self._x + 1
        else:
            self.x = self._x - 1

    def backward(self):
        if self._direction == "N":
            self.y = self._y - 1
        elif self._direction == "S":
            self.y = self._y + 1
        elif self._direction == "E":
            self.x = self._x - 1
        else:
            self.x = self._x + 1
