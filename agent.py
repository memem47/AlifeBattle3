from dataclasses import dataclass

import pygame

import config


@dataclass
class Agent:
    """One physical member of a platoon."""

    position: pygame.Vector2
    formation_offset: pygame.Vector2

    def move_toward(
        self,
        target: pygame.Vector2,
        dt: float,
    ) -> None:
        """Move the agent toward the requested world-space position."""

        delta = target - self.position
        distance = delta.length()

        if distance == 0:
            return

        max_step = config.AGENT_SPEED * dt

        if distance <= max_step:
            self.position = target.copy()
            return

        self.position += delta.normalize() * max_step