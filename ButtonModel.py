class ButtonModel:
    idle = 0
    hover = 1
    pressIn = 2
    pressOut = 3

    def __init__(self):
        self.state = self.idle

    def toHover(self):
        if self.state == self.idle:
            self.state = self.hover
            print("State changed to Hover")

    def toPressIn(self):
        if self.state == self.hover:
            self.state = self.pressIn
            print("State changed to PressIn")

    def toPressOut(self):
        if self.state == self.pressIn:
            self.state = self.pressOut
            print("State changed to PressOut")

    def toIdle(self):
        if self.state in {self.hover, self.pressOut}:
            self.state = self.idle
            print("State changed to Idle")

    def action(self):
        if self.state == self.pressOut:
            print("Action executed!")
