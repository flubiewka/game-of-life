import time
from tkinter import TclError
from src.gtxt import Gtxt, ANSI
from src.gapi import Gapi


class Game:
    def __init__(self):
        while (
            a := input("which mode you want to enter: 1 - Gapi | 2 - Gtxt\n>> ")
        ) not in ("1", "2"):
            pass
        if a == "1":
            self.__display = Gapi()
        else:
            self.__display = Gtxt()
            print(ANSI["ENTER_ALT_SCREEN"] + ANSI["HIDE_CURSOR"], end="", flush=True)

    def play(self):
        try:
            while True:
                self.__display.view()
                self.__display.step()
                time.sleep(0.1)  # 0.1 = 10fps
        except (KeyboardInterrupt, TclError):
            print("\nGame has been stopped")
        finally:
            if isinstance(self.__display, Gtxt):
                print(ANSI["SHOW_CURSOR"] + ANSI["EXIT_ALT_SCREEN"], end="", flush=True)
