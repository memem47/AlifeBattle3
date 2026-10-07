# AlifeBattle3 Game Design

## 1. Game Concept

AlifeBattle3 is a real-time tactical battle simulation in which the player commands multiple platoons made up of individual physical agents.

The player controls platoons rather than individual agents.

The player's primary task is to decide:

- where platoons move
- which routes they take
- where they stop
- which enemy platoons they attack
- when platoons are merged
- when platoons are split

Battlefield outcomes should emerge from these commands and the physical interaction of hundreds of agents.

---

## 2. Core Experience

The most important player experience is:

> Seeing a tactical decision succeed and watching the enemy force rapidly collapse as a result.

Examples include:

- holding an enemy platoon in place
- moving another platoon around its flank
- concentrating several platoons against one enemy platoon
- splitting a platoon to attack from multiple directions
- surrounding an enemy force

The visual spectacle of hundreds of agents fighting simultaneously is also a major part of the game.

---

## 3. Match Structure

Target battle duration:

**Approximately 5 minutes**

Initial force size:

- Red: 3 platoons
- Blue: 3 platoons
- 100 agents per platoon

Total:

**300 vs 300 agents**

---

## 4. Player Control

The primary player-controlled unit is the platoon.

Individual agents cannot be directly selected or commanded.

### 4.1 Move

The player selects a platoon and specifies destinations with the mouse.

Multiple waypoints can be added sequentially.

Example:

```text
Start
  ↓
Waypoint A
  ↓
Waypoint B
  ↓
Destination
```

This allows the player to deliberately create:

- detours
- flanking movement
- rear attacks
- curved movement routes

The platoon follows the waypoints in order.

---

### 4.2 Hold / Defend

When a platoon completes its movement order, it automatically enters a defensive state.

The player can also explicitly stop a moving platoon.

A defending platoon:

- maintains its general position
- attacks enemies within valid attack range
- does not intentionally pursue distant enemies

---

### 4.3 Attack

The player selects an enemy platoon as an attack target.

If the target is outside attack range, the attacking platoon automatically moves toward a valid attack position.

Once attack conditions are satisfied, agents attack the designated enemy.

The platoon does not independently choose a different strategic target.

---

### 4.4 Merge

Multiple friendly platoons can be combined into one platoon.

Example:

```text
Platoon A: 60 agents
Platoon B: 40 agents

        ↓

Platoon C: 100 agents
```

The merged platoon becomes a single command unit.

---

### 4.5 Split

The player can specify a number of agents to separate from an existing platoon.

Example:

```text
Platoon A
100 agents

     ↓ split 30

Platoon A        Platoon B
70 agents        30 agents
```

This allows tactical actions such as:

- creating a reserve
- flanking
- surrounding enemies
- attacking multiple positions

---

## 5. Agent Autonomy

Agents do not make independent tactical decisions.

Agents do not independently:

- choose strategic targets
- flank enemies
- retreat
- change platoon objectives
- decide battlefield strategy

Tactical decisions belong to the player or enemy commander AI.

Agents may automatically perform local actions required to execute orders.

Examples:

- move toward a commanded destination
- avoid invalid physical overlap
- adjust local position
- face an attack target
- attack when conditions are satisfied
- play attack animations
- take damage
- die

---

## 6. Physical Model

Agents are physical entities with non-zero size.

Living agents should not freely occupy the same physical space.

The simulation should therefore be designed around physical occupancy from the beginning rather than adding separation behavior afterward.

Conceptually, an agent contains properties such as:

```text
position
velocity
orientation
physical radius

health

weapon
attack range
attack interval

platoon ID
```

Visual size and physical collision size must remain separate concepts.

This allows future unit types to have different physical characteristics.

Possible future examples include:

- infantry
- heavy infantry
- cavalry
- vehicles

---

## 7. Combat

Combat progresses continuously in real time.

Individual agents perform attacks.

### Ranged Combat

Ranged weapons should provide visible battlefield feedback such as:

- bullet traces
- projectile movement
- muzzle effects
- impact effects

Large numbers of simultaneous attacks should make the battlefield visually active.

### Melee Combat

Close combat may include:

- weapon swings
- thrusts
- attack animation
- hit reactions

Detailed animation quality is less important initially than clearly communicating that many individual agents are fighting.

---

## 8. Victory Conditions

### Elimination

A side loses when all of its agents are dead.

### Time Limit

If the time limit is reached, remaining force strength determines the winner.

Initial implementation may use remaining agent count.

Example:

```text
Red: 127 agents
Blue: 83 agents

Winner: Red
```

---

## 9. Design Principle

The fundamental design principle is:

> Agents execute tactics; they do not invent tactics.

Complex battlefield behavior should emerge primarily from:

```text
player commands
+
platoon positioning
+
hundreds of physical agents
+
combat interactions
```

rather than from sophisticated individual-agent tactical AI.

---

## 10. First Playable Version

The first playable version should demonstrate the core experience as quickly as possible.

Target:

```text
Red
3 platoons × 100 agents

vs

Blue
3 platoons × 100 agents
```

Required features:

1. display 600 agents
2. select a platoon
3. issue movement commands
4. add multiple waypoints
5. physically move agents
6. designate an enemy platoon
7. approach attack range
8. attack
9. apply damage
10. kill agents
11. determine victory

The following features are intentionally postponed:

- platoon merge
- platoon split
- sophisticated enemy commander AI
- terrain
- multiple unit types
- advanced animation
- advanced formations

These features should be added only after the basic 300-vs-300 battle is demonstrated to be enjoyable.