# AlifeBattle3

AlifeBattle3 is a real-time tactical battle simulation in which the player commands platoons composed of many individual agents.

The player does not directly control individual agents. Instead, the player issues high-level commands to platoons while individual agents physically move, engage enemies, attack, take damage, and die in real time.

## Core Concept

- Real-time tactical combat
- 3 platoons per side
- 100 agents per platoon
- Initial target: 300 vs 300 agents
- Approximately 5-minute battles
- Mouse-based platoon command system
- Individual physical agents
- Large-scale visual combat with ranged and melee attack effects

The main gameplay experience is:

> Give simple commands to multiple platoons and watch those decisions create large-scale battlefield consequences.

## Main Commands

Platoons will eventually support:

- Move
- Multiple movement waypoints
- Hold / Defend
- Attack
- Merge platoons
- Split platoons

## Design Philosophy

The player makes tactical decisions.

Individual agents do not make independent tactical decisions such as flanking, retreating, or selecting strategic targets.

Agents are responsible only for executing platoon commands through local behavior such as:

- movement
- physical interaction
- collision handling
- positioning
- attacking
- taking damage
- death

## Development Strategy

AlifeBattle3 prioritizes rapidly reaching playable versions.

Implementation details may be generated with AI tools. Development review focuses primarily on:

1. file responsibilities
2. class responsibilities
3. function responsibilities
4. major algorithms and design decisions

Understanding every implementation line is not required.

See:

- `docs/GAME_DESIGN.md`
- `docs/DEVELOPMENT.md`