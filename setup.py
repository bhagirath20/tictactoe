from cx_Freeze import setup, Executable

setup(
    name="TicTacToe",
    version="1.0",
    description="Tic Tac Toe game",
    executables=[Executable("app.py")],
)