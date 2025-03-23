from pywincontrol import WinController, RECT
import time


class MarioWorld(WinController):
    def __init__(self, fps: int):
        WinController.__init__(self, "Snes9x", "Super Mario World (Europe) - Snes9x 1.62.3")

        self.actions: dict = {
            "NO_ACTION": "NO_ACTION",
            "JUMP": "f",
            "SPIN": "x",
            "FIRE": "c",
            "X": "v",

            "L": "a",
            "R": "e",

            "START": "p",
            "SELECT": "m",

            "UP": "z",
            "DOWN": "s",
            "LEFT": "q",
            "RIGHT": "d",
        }

        self.actions_list: list = [
            self.actions.get("NO_ACTION"),
            self.actions.get("JUMP"),
            self.actions.get("SPIN"),
            self.actions.get("FIRE"),

            self.actions.get("UP"),
            self.actions.get("DOWN"),
            self.actions.get("LEFT"),
            self.actions.get("RIGHT"),
        ]

    def to_image_(self):
        top_crop: int = 120
        return self.main_win.capture_as_image(RECT(left=self.left+10, top=self.top+top_crop, width=self.width-30, height=self.height-top_crop-20))

    def get_timer(self):
        return self.main_win.capture_as_image(RECT(left=self.left+307, top=self.top+95, width=50, height=19))

    def get_lifes(self):
        return self.main_win.capture_as_image(RECT(left=self.left+70, top=self.top+95, width=35, height=19))

    def get_score(self):
        return self.main_win.capture_as_image(RECT(left=self.left+370, top=self.top+95, width=115, height=19))

    def get_coins(self):
        return self.main_win.capture_as_image(RECT(left=self.left+432, top=self.top+79, width=50, height=19))


def main():
    iter = 0

    mw = MarioWorld()
    mw.main_win.set_focus()

    while iter < 10:
        data = mw.to_image()
        data.save("test_image.png")

        iter += 1

        time.sleep(.18)

    mw.stop()


if __name__ == "__main__":
    main()
