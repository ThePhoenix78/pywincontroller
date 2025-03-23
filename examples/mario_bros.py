from pywincontroller import WinController, RECT

# import numpy as np

import time


class MarioBros(WinController):
    def __init__(self):
        WinController.__init__(self, "Mesen", "Mesen - Super Mario Bros. (Europe) (Rev A)")

        self.actions: dict = {
            "JUMP": "k",
            "FIRE": "j",

            "START": "i",
            "SELECT": "u",

            "UP": "z",
            "DOWN": "s",
            "LEFT": "q",
            "RIGHT": "d",
        }

        self.actions_list: list = [
            "JUMP",
            "FIRE",

            "UP",
            "DOWN",
            "LEFT",
            "RIGHT",
        ]

    def to_image(self):
        top_crop: int = 120
        return self.main_win.capture_as_image(RECT(left=self.left+10, top=self.top+top_crop, width=self.width-30, height=self.height-top_crop-20))

    def get_timer(self):
        return self.main_win.capture_as_image(RECT(left=self.left+422, top=self.top+101, width=50, height=18))

    def get_score(self):
        return self.main_win.capture_as_image(RECT(left=self.left+52, top=self.top+101, width=102, height=18))

    def get_coins(self):
        return self.main_win.capture_as_image(RECT(left=self.left+212, top=self.top+101, width=38, height=18))


def main():
    iter = 0

    mb = MarioBros()
    mb.focus()

    while iter < 20:
        if iter % 4:
            # to do an action
            mb.do(["JUMP"])

        else:
            # to do nothing
            mb.do("")

        iter += 1

        time.sleep(.18)

    mb.stop()


if __name__ == "__main__":
    main()
