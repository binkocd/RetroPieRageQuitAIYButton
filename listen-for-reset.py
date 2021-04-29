#!/usr/bin/env python3
import subprocess
from aiy.board import Board, Led

def main():
    with Board() as board:
        while True:
            board.led.state = Led.ON
            board.button.wait_for_press()
            board.led.state = Led.OFF
            #subprocess.call(['rm', '/opt/retropie/configs/all/emulationstation/es_input.cfg'], shell=False)
            #subprocess.call(['rm', '/opt/retropie/configs/all/retroarch-joypads/*'], shell=False)
            subprocess.call(['shutdown', '-r', 'now'], shell=False)


if __name__ == '__main__':
    main()