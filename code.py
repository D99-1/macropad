print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP3,board.GP4,board.GP5)
keyboard.row_pins = (board.GP6,board.GP7,board.GP8,board.GP9)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [KC.A,KC.B,KC.C,
    KC.D,KC.E,KC.F],
    KC.G,KC.H,KC.I,
    KC.J,KC.K,KC.L]
]

if __name__ == '__main__':
    keyboard.go()
