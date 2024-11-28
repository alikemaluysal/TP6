# ButtonModel.py

class ButtonModel:
    # Durumlar için sınıf değişkenleri
    idle = 0       # Düğme boşta
    hover = 1      # Fare düğmenin üzerinde
    pressIn = 2    # Fare tıklandı
    pressOut = 3   # Fare bırakıldı

    def __init__(self):
        # Başlangıç durumu: idle
        self.state = ButtonModel.idle

    # Durum geçişlerini sağlayan metotlar
    def toHover(self):
        if self.state == ButtonModel.idle:
            self.state = ButtonModel.hover
            print("Transition to hover")

    def toPressIn(self):
        if self.state == ButtonModel.hover:
            self.state = ButtonModel.pressIn
            print("Transition to pressIn")

    def toPressOut(self):
        if self.state == ButtonModel.pressIn:
            self.state = ButtonModel.pressOut
            print("Transition to pressOut")

    def toIdle(self):
        if self.state in (ButtonModel.pressOut, ButtonModel.hover):
            self.state = ButtonModel.idle
            print("Transition to idle")

    # Action durumu için metot
    def action(self):
        if self.state == ButtonModel.pressOut:
            print("Action triggered!")
