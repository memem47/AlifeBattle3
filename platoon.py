from collections.abc import Iterable

import pygame

import config
from agent import Agent


class Platoon:
    """A player-commandable group of agents."""

    def __init__(
        self,
        platoon_id: int,
        team: str,
        center: pygame.Vector2,
    ) -> None:
        self.id = platoon_id
        self.team = team

        self.center = center.copy()
        self.destination = center.copy()

        self.agents = self._create_agents()

        self.selected = False

    def _create_agents(self) -> list[Agent]:
        """Create agents in a rectangular formation."""

        agents: list[Agent] = []

        columns = config.FORMATION_COLUMNS
        rows = (
            config.AGENTS_PER_PLATOON
            + columns
            - 1
        ) // columns

        width = (columns - 1) * config.FORMATION_SPACING
        height = (rows - 1) * config.FORMATION_SPACING

        start_x = -width / 2
        start_y = -height / 2

        for index in range(config.AGENTS_PER_PLATOON):
            column = index % columns
            row = index // columns

            offset = pygame.Vector2(
                start_x + column * config.FORMATION_SPACING,
                start_y + row * config.FORMATION_SPACING,
            )

            agents.append(
                Agent(
                    position=self.center + offset,
                    formation_offset=offset,
                )
            )

        return agents

    def set_destination(
        self,
        destination: pygame.Vector2,
    ) -> None:
        """Set a new destination for the platoon."""

        self.destination = destination.copy()

    def update(self, dt: float) -> None:
        """Move every agent toward its desired formation position."""

        delta = self.destination - self.center
        distance = delta.length()

        if distance > 0:
            max_step = config.AGENT_SPEED * dt

            if distance <= max_step:
                self.center = self.destination.copy()
            else:
                self.center += delta.normalize() * max_step

        for agent in self.agents:
            target = self.center + agent.formation_offset
            agent.move_toward(target, dt)

    def contains_point(
        self,
        point: pygame.Vector2,
    ) -> bool:
        """Return True when a screen point lies inside the platoon area."""

        return self.bounding_rect().collidepoint(
            point.x,
            point.y,
        )

    def bounding_rect(self) -> pygame.Rect:
        """Return the rectangle enclosing all living platoon agents."""

        positions: Iterable[pygame.Vector2] = (
            agent.position for agent in self.agents
        )

        positions = list(positions)

        min_x = min(position.x for position in positions)
        max_x = max(position.x for position in positions)
        min_y = min(position.y for position in positions)
        max_y = max(position.y for position in positions)

        margin = config.AGENT_RADIUS + 4

        return pygame.Rect(
            min_x - margin,
            min_y - margin,
            max_x - min_x + margin * 2,
            max_y - min_y + margin * 2,
        )