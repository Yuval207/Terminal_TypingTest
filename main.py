import random
import curses
from curses import wrapper
import time

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!", curses.A_REVERSE )
    stdscr.refresh()
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
    


wrapper(main)