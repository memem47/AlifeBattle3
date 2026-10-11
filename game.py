import pygame

import config
from platoon import Platoon


class Game:
    """Owns the battle simulation state."""

    def __init__(self) -> None:
        self.platoons: list[Platoon] = []

        self._create_initial_platoons()

    def _create_initial_platoons(self) -> None:
        """Create the initial Red and Blue armies."""

        platoon_id = 0

        for y in config.PLATOON_START_Y:
            self.platoons.append(
                Platoon(
                    platoon_id=platoon_id,
                    team="red",
                    center=pygame.Vector2(
                        config.RED_START_X,
                        y,
                    ),
                )
            )
            platoon_id += 1

        for y in config.PLATOON_START_Y:
            self.platoons.append(
                Platoon(
                    platoon_id=platoon_id,
                    team="blue",
                    center=pygame.Vector2(
                        config.BLUE_START_X,
                        y,
                    ),
                )
            )
            platoon_id += 1

    def update(self, dt: float) -> None:
        """Advance the simulation by one frame."""

        for platoon in self.platoons:
            platoon.update(dt)

    def select_platoon_at(
        self,
        position: pygame.Vector2,
    ) -> None:
        """Select one Blue platoon at the requested position."""

        for platoon in self.platoons:
            platoon.selected = False

        for platoon in reversed(self.platoons):
            if platoon.team != "blue":
                continue

            if platoon.contains_point(position):
                platoon.selected = True
                return

    def command_selected_platoons(
        self,
        destination: pygame.Vector2,
    ) -> None:
        """Send the selected platoon to a destination."""

        for platoon in self.platoons:
            if platoon.selected:
                platoon.set_destination(destination)