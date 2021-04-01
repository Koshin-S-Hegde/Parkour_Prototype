from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = (0, 3, 0)

    def custom_update(self):
        if self.y <= -50:
            self.position = (0, 3, 0)
