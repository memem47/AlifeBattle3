# AlifeBattle3 Architecture

## 1. Architectural Goal

AlifeBattle3 separates tactical decisions from physical execution and rendering.

The main dependency direction is:

```text
Player Input
    |
    v
InputHandler
    |
    v
Game
    |
    v
Platoon
    |
    v
Agent

Game State
    |
    v
Renderer
```

The player commands platoons.

Platoons translate commands into desired behavior for individual agents.

Agents perform individual movement and, later, physical and combat actions.

The renderer observes simulation state but does not modify game rules.

---

# 2. Initial File Responsibilities

## main.py

Application entry point.

Responsible for:

- pygame initialization
- creating major application objects
- running the main loop
- frame timing
- application shutdown

Main loop:

```text
Input
  ↓
Simulation Update
  ↓
Rendering
```

---

## config.py

Contains tunable global configuration values.

Examples:

- screen size
- target FPS
- agent speed
- agent radius
- platoon size
- initial deployment positions

Game logic should not be implemented in this file.

---

## game.py

Owns the overall battle state.

Responsible for:

- platoon collection
- initial army creation
- simulation updates
- player command routing

Future responsibilities may include:

- battle timer
- victory conditions
- army ownership
- battle lifecycle

---

## platoon.py

Represents a player-commandable platoon.

Responsible for:

- platoon membership
- platoon center
- destination
- waypoint queue
- command state
- attack target
- translating platoon commands into individual Agent goals

Platoon is the primary tactical command unit.

---

## agent.py

Represents one physical battlefield entity.

Responsible for individual state such as:

- position
- velocity
- orientation
- physical radius
- health
- attack state

In the first prototype, Agent only performs simple movement.

Later, Agent will interact with Physics and Combat systems.

---

## input_handler.py

Converts raw pygame input events into game commands.

Examples:

```text
Left click
→ select platoon

Right click
→ move selected platoon

Shift + right click
→ append waypoint
```

Input handling should not contain simulation logic.

---

## renderer.py

Displays current simulation state.

Responsible only for visualization.

Examples:

- agents
- platoon selection
- destinations
- projectiles
- effects
- UI

Renderer must not determine simulation outcomes.

---

# 3. Main Runtime Flow

Each frame:

```text
pygame events
      |
      v
InputHandler
      |
      v
Game commands
      |
      v
Game.update(dt)
      |
      v
Platoon.update(dt)
      |
      v
Agent movement
      |
      v
Renderer.draw()
```

`dt` is elapsed real time in seconds.

Movement and combat should use `dt` so simulation speed is not directly tied to frame rate.

---

# 4. Command Hierarchy

Strategic and tactical decisions flow downward.

```text
Player / Commander AI
        |
        v
      Platoon
        |
        v
       Agent
```

The player does not directly command individual Agents.

Agents do not independently invent tactical objectives.

---

# 5. Current Prototype Simplification

The initial prototype does not yet implement physical collision.

Agents maintain fixed formation offsets relative to the platoon center.

Conceptually:

```text
Platoon destination
        |
        v
Platoon center moves
        |
        v
Agent target =
Platoon center + formation offset
```

This is temporary.

It exists to validate:

- command routing
- platoon selection
- large group rendering
- frame-independent movement
- code responsibility boundaries

before physics is introduced.

---

# 6. Planned Evolution

The architecture is expected to evolve approximately as follows:

```text
Player
   |
   v
Platoon Command
   |
   v
Agent desired movement
   |
   v
Physics
   |
   v
Resolved Agent position
   |
   +----> Combat
   |
   v
Renderer
```

Future systems will include:

- waypoint commands
- physical collision
- attack targeting
- ranged combat
- damage and death
- enemy commander AI
- victory conditions

These systems should be introduced only when required by a playable feature.