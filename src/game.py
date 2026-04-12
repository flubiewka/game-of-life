from time import sleep, perf_counter
from tkinter import TclError
from src.config import FRAME_TARGET_SECONDS, MODE_PROMPT
from src.display import Display
from src.gapi import Gapi
from src.gtxt import Gtxt


class Game:
    def __init__(self):
        self.__display: Display
        # Keep asking until user chooses a supported mode.
        while (mode := input(MODE_PROMPT)) not in ("1", "2"):
            pass
        self.__display = Gapi() if mode == "1" else Gtxt()

        self.__display.on_start()

    def play(self):
        try:
            # Endless simulation loop; timing is handled in __tick.
            while True:
                self.__tick(FRAME_TARGET_SECONDS)
        except (KeyboardInterrupt, TclError):
            print("\nGame has been stopped")
        finally:
            self.__display.on_stop()

    def __tick(self, target_time: float):
        """
        needed this function because there was difference in frame time with different render modes

        vresion 1.0:
        Gtxt frametime: min - 2ms, max - 5ms.
        Gapi frametime: min - 57ms, max - 167ms.

        vresion 2.0: - difference is negligible, no need for this function anymore
        Gtxt frametime: min - 2ms, max - 3ms.
        Gapi frametime: min - 5ms, max - 8ms.

        version 3.0: - canvas instead of frames fixed lags on start and stop
        Gtxt frametime: min - 2ms, max - 3ms.
        Gapi frametime: min - 4ms, max - 10ms.
        =============================================
        """
        frame_started = perf_counter()

        self.__display.view()
        self.__display.step()

        frame_spent = perf_counter() - frame_started

        # Sleep only when frame work finished faster than target.
        frame_time_remained = target_time - frame_spent
        if frame_time_remained > 0:
            sleep(frame_time_remained)
