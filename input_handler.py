import pygame

from game import Game


class InputHandler:
    """Translate mouse and window events into game commands."""

    def handle_event(
        self,
        event: pygame.event.Event,
        game: Game,
    ) -> bool:
        """Handle one pygame event.

        Returns False when the application should exit.
        """

        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.Vector2(event.pos)

            if event.button == 1:
                game.select_platoon_at(position)

            elif event.button == 3:
                game.command_selected_platoons(position)

        return True