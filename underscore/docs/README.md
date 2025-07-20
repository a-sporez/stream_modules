
# `character` Object Reference Sheet

## Finite State Machine

### Notes on `**kwargs`

Any number of named arguments passed in as a dictionary.

Example:

```python
def enter(self, **kwargs):
    pass
```

is passed by calling it like this:

```python
fsm.change('menu', instanceID="IDxx1", debug_mode=True, stacked_iters=2)
```

internally it would be:

```python
kwargs = {
    'instanceID': 'IDxx1',
    'debug_mode': True,
    'stacked_iters': 2
}
```

So in the `enter()` method one could write:

```python
def enter(self, **kwargs)
    if kwargs.get('debug_mode'):
        print("Debug baby!!")
```

## Core Attributes

| Attribute      | Type  | Description                    |
| -------------- | ----- | ------------------------------ |
| `name`         | `str` | Character's name               |
| `level`        | `int` | Starts at 1                    |
| `max_hp`       | `int` | default 10                     |
| `hp`           | `int` | Current HP, starts at `max_hp` |
| `iters`        | `int` | apply in-out combat variables  |
| `elites_slain` | `int` | Tracks elite enemy kills       |
| `bless_burden` | `int` | blessing burden count          |

---

## Combat State

| Attribute      | Type   | Description                                   |
| -------------- | ------ | --------------------------------------------- |
| `chosen_move`  | `str`  | name of currently chosen move                 |
| `has_priority` | `bool` | whether character has move priority this turn |

---

## Move Management

|Attribute|Type|Description|
|---|---|---|
|`active_moves`|`dict`|Moves available in combat|
|`banked_moves`|`dict`|Moves set aside for later use|
|`bound_moves`|`dict`|Moves restricted/bound for special use|
|`starter_moves`|`dict`|Generated on init from `Build_Starter()`|

---

## Perks and Effects

| Attribute      | Type   | Description                                  |
| -------------- | ------ | -------------------------------------------- |
| `blessings`    | `dict` | special perks (can modify status/attunement) |
| `attunements`  | `dict` | elemental affinity states                    |
| `statuses`     | `dict` | status effects                               |
| `move_history` | `dict` | records of previously used moves             |

Each `attunement` entry is a dict with:

- `public` (`bool`)

- `turns` (`int`)

- `color` (`int`)

- `icon` (`str`)

Each `status` entry is a dict with:

- `immune_to` (`bool`)

- `ignores` (`bool`)

- `turns` (`int`)

- `color` (`int`)

- `icon` (`str`)

---

## Methods

|Method|Description|
|---|---|
|`print_vars()`|Displays character info including HP, attunements, statuses, moves, etc. in formatted output|

---

## Special Functions

### `Build_Starter(element_1, element_2, temperament)`

- Returns a `dict` of moves (up to 4)

- Chooses `temperament` number of attacks

- Fills the rest with utilities from the two elements provided

- Each move is a `dict` with:

- `name`, `type`, `element`, `color`, `icon`

---
