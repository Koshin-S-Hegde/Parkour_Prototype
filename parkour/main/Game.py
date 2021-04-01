import ursina
from parkour.main.game_objects.Floor import Floor
from parkour.main.game_objects import Player

player: Player.Player


def update():
    player.custom_update()


class Game:
    __app: ursina.Ursina

    def __init__(self: "Game"):
        self.__app = ursina.Ursina()
        self.__configure_window()
        self.__create_game_objects()
        self.__run()

    def __run(self: "Game"):
        self.__app.run()

    @staticmethod
    def __configure_window():
        ursina.window.title = "Made by Koshin and not Saurav"
        ursina.window.borderless = False
        ursina.window.fps_counter.position = ursina.window.exit_button.position
        ursina.window.exit_button.visible = False

    @staticmethod
    def __create_game_objects():
        floor_positions: list[tuple[int, int, int]] \
            = [(0, 0, 0), (1, 1, 0), (3, 2, 0), (5, 4, 0), ]
        floor_position: tuple[int, int, int]
        for floor_position in floor_positions:
            Floor(floor_position)
        global player
        player = Player.Player()


if __name__ == "__main__":
    Game()
