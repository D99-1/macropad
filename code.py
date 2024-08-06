print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP3,board.GP4,board.GP5)
keyboard.row_pins = (board.GP6,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,KC.B,KC.C]
]

if __name__ == '__main__':
    keyboard.go()