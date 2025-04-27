import pywinauto.win32_hooks


class COORDS:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class RECT():
    def __init__(self, left: int = None, top: int = None, right: int = None, bottom: int = None, width: int = None, height: int = None, middle: COORDS = None):
        _left: int = None
        _top: int = None

        if height is None and width:
            height: int = width

        elif width is None and height:
            width: int = height

        if middle is not None:
            _left: int = middle.x - width // 2
            _top: int = middle.y - height // 2

        self.left: int = left if left is not None else _left
        self.top: int = top if top is not None else _top

        if not self.left or not self.top:
            raise "Error, set at least a width or height with center"

        if right is not None:
            self.right: int = right

        elif width is not None:
            self.right: int = self.left + width

        else:
            raise "Error, set at least right, width or center"

        if bottom is not None:
            self.bottom: int = bottom

        elif width is not None:
            self.bottom: int = self.top + height

        else:
            raise "Error, set at least bottom, width or center"

        self._width: int = width if width is not None else self.width()
        self._height: int = height if height is not None else self.height()
        self._middle: COORDS = self.mid_point()

    def width(self):
        return abs(self.right-self.left)

    def height(self):
        return abs(self.bottom-self.top)

    def mid_point(self):
        x: int = self.left + int(float(self._width) / 2.)
        y: int = self.top + int(float(self._height) / 2.)
        return COORDS(x, y)


class InputEvent:
    def __init__(self, event):
        self.event = event
        self.current_key = event.current_key
        self.event_type = event.event_type

        if isinstance(event, pywinauto.win32_hooks.KeyboardEvent):
            self.pressed_key = event.pressed_key
            self.mouse_x = None
            self.mouse_y = None

        if isinstance(event, pywinauto.win32_hooks.MouseEvent):
            self.mouse_x = event.mouse_x
            self.mouse_y = event.mouse_y
            self.pressed_key = None
