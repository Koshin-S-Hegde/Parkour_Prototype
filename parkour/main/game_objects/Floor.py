import ursina


class Floor:
    __model: str = "cube"
    __collider: str = "box"
    __texture: str = "white_cube"
    __color: ursina.color.color = ursina.color.gold

    def __init__(self, position: tuple[int, int, int]):
        ursina.Entity(position=position, model=self.__model, color=self.__color, texture=self.__texture,
                      collider=self.__collider)
