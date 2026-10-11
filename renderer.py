import pygame

import config
from game import Game


class Renderer:
    """Draw the current game state."""

    def __init__(
        self,
        screen: pygame.Surface,
    ) -> None:
        self.screen = screen

    def draw(self, game: Game) -> None:
        """Draw one frame."""

        self.screen.fill(config.BACKGROUND_COLOR)

        for platoon in game.platoons:
            self._draw_platoon(platoon)

        pygame.display.flip()

    def _draw_platoon(self, platoon) -> None:
        """Draw one platoon and its command indicators."""

        if platoon.team == "red":
            color = config.RED_COLOR
        else:
            color = config.BLUE_COLOR

        for agent in platoon.agents:
            pygame.draw.circle(
                self.screen,
                color,
                (
                    round(agent.position.x),
                    round(agent.position.y),
                ),
                config.AGENT_RADIUS,
            )

        if platoon.selected:
            pygame.draw.rect(
                self.screen,
                config.SELECTION_COLOR,
                platoon.bounding_rect(),
                width=2,
            )

            pygame.draw.circle(
                self.screen,
                config.DESTINATION_COLOR,
                (
                    round(platoon.destination.x),
                    round(platoon.destination.y),
                ),
                7,
                width=2,
            )