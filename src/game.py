import time
from src.gtxt import Gtxt, ANSI


class Game:
    def __init__(self):
        self.display = Gtxt()

    def play(self):
        print(ANSI["ENTER_ALT_SCREEN"] + ANSI["HIDE_CURSOR"], end="", flush=True)

        try:
            while True:
                self.display.view()
                self.display._analysis()
                time.sleep(0.1)  # 0.1 = 10fps
        except KeyboardInterrupt:
            print("\nGame has been stopped")
        finally:
            print(ANSI["SHOW_CURSOR"] + ANSI["EXIT_ALT_SCREEN"], end="", flush=True)
