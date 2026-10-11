import pygame

import config
from game import Game
from input_handler import InputHandler
from renderer import Renderer


def main() -> None:
    """Run the AlifeBattle3 application."""

    pygame.init()

    screen = pygame.display.set_mode(
        (
            config.SCREEN_WIDTH,
            config.SCREEN_HEIGHT,
        )
    )

    pygame.display.set_caption("AlifeBattle3")

    clock = pygame.time.Clock()

    game = Game()
    input_handler = InputHandler()
    renderer = Renderer(screen)

    running = True

    while running:
        dt = clock.tick(config.TARGET_FPS) / 1000.0

        for event in pygame.event.get():
            running = input_handler.handle_event(
                event,
                game,
            )

            if not running:
                break

        game.update(dt)
        renderer.draw(game)

    pygame.quit()


if __name__ == "__main__":
    main()