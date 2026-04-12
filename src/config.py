DATA_FILE_PATH = "data/data.txt"

MODE_PROMPT = "which mode you want to enter: 1 - Gapi | 2 - Gtxt\n>> "
FRAME_TARGET_SECONDS = 0.1  # 100ms

GAPI_WINDOW_TITLE = "Game Of Life"
GAPI_WINDOW_BG = "#333333"
GAPI_BLOCK_SIZE = 20
GAPI_COLORS = {"VOID": "#13a10e", "ALIVE": "#c50f1f", "WAS_ALIVE": "#00af00"}

ANSI = {
    "RESET": "\033[0m",
    "B_RED": "\033[41m",  #! alive
    "B_GREEN": "\033[42m",  #! void
    "B_DARK_GREEN": "\033[48;5;34m",  #!was alive
    "CLEAR_SCREEN": "\033[H\033[J",
    "CURSOR_HOME": "\033[H",
    "HIDE_CURSOR": "\033[?25l",
    "SHOW_CURSOR": "\033[?25h",
    "ENTER_ALT_SCREEN": "\033[?1049h",
    "EXIT_ALT_SCREEN": "\033[?1049l",
}
