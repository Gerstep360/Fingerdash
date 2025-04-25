import vgamepad as vg

class XboxController:
    def __init__(self):
        self.pad = vg.VX360Gamepad()
        self._a = False

    def press_a(self):
        if not self._a:
            self.pad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            self.pad.update()
            self._a = True

    def release_a(self):
        if self._a:
            self.pad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            self.pad.update()
            self._a = False
