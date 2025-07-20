# Raw Source Blueprint

```python
# This is no longer used, but i am including it so you can see how the builders below worked
# This data is now included in the global variables for elements and statuses

STYLE_REF: dict = {
    'element': {
        'water':    { 'color':   4, 'icon': '🌊' },
        'stone':    { 'color': 136, 'icon': '🪨' },
        'fire':     { 'color': 196, 'icon': '🔥' },
        'plant':    { 'color': 112, 'icon': '🌿' },
        'vital':    { 'color': 198, 'icon': '❤️' },
        'force':    { 'color':  36, 'icon': '💨' },
        'thunder':  { 'color': 184, 'icon': '⚡' },
        },
    'status': {
        'burn':     { 'color': 167, 'icon': '🔥' },
        'wound':    { 'color': 168, 'icon': '🩸' },
        'decay':    { 'color':  30, 'icon': '💀' },
        'regen':    { 'color':  70, 'icon': '✨' },
        'slow':     { 'color': 172, 'icon': '🐌'},
        'quick':    { 'color': 229, 'icon': '⚡' },
        'angry':    { 'color': 174, 'icon': '😡' },
        'curse':    { 'color':  56, 'icon': '😈' },
        'stun':     { 'color': 184, 'icon': '😵' },
        'sleep':    { 'color': 107, 'icon': '💤' },
        'tough':    { 'color':  94, 'icon': '🛡️'},
        'strong':   { 'color':   1, 'icon': '💪' },
        }
    }

# This is a much better way to do this, obviously.

ELEMENTS: dict = {
    'water': { 
        'color':   4, 'icon': '🌊',
        'weak_to':   ['thunder', 'plant'],
        'resists':   ['stone'],
        'immune_to': [],
        'absorbs':   ['fire'],
    },
    'stone': { 
        'color': 136, 'icon': '🪨',
        'weak_to':   ['water', 'force'],
        'resists':   ['fire'],
        'immune_to': ['thunder'],
        'absorbs':   [],
    },
    'fire': {
        'color': 196, 'icon': '🔥',
        'weak_to':   ['water', 'stone'],
        'resists':   [],
        'immune_to': [],
        'absorbs':   ['plant'],
    },
    'plant': { 
        'color': 112, 'icon': '🌿',
        'weak_to':   ['fire', 'vital'],
        'resists':   [],
        'immune_to': [],
        'absorbs':   ['water'],
    },
    'vital': { 
        'color': 198, 'icon': '❤️',
        'weak_to':   ['vital', 'force'],
        'resists':   [],
        'immune_to': [],
        'absorbs':   [],
    },
    'force': {
        'color':  36, 'icon': '💨',
        'weak_to':   ['thunder'],
        'resists':   ['vital'],
        'immune_to': ['stone'],
        'absorbs':   [],
    },
    'thunder':  { 
        'color': 184, 'icon': '⚡',
        'weak_to':   ['stone'],
        'resists':   ['water'],
        'immune_to': ['force'],
        'absorbs':   [],
    },
}

STATUSES: dict = {
    'burn': {
        'color': 167, 'icon': '🔥',
        'deals': 'fire',
        'max_amount': 3,
        'at_max': 'burn_out',
    },
    'wound': {
        'color': 168, 'icon': '🩸',
        'deals': 'vital',
        'max_amount': 100,
        'at_max': 'flesh_flood',
    },
    'decay': {
        'color':  30, 'icon': '💀',
        'deals': 'force',
        'max_amount': 5,
        'at_max': 'ignore',
    },
    'regen': {
        'color':  70, 'icon': '✨',
        'deals': 'plant',
        'max_amount': 5,
        'at_max': 'ignore',
    },
    'slow': {
        'color': 172, 'icon': '🐌',
        'deals': 'none',
        'max_amount': 1,
        'at_max': 'ignore',
    },
    'quick': {
        'color': 229, 'icon': '⚡',
        'deals': 'none',
        'max_amount': 1,
        'at_max': 'ignore',
    },
    'angry': {
        'color': 174, 'icon': '😡',
        'deals': 'none',
        'max_amount': 3,
        'at_max': 'ignore',
    },
    'curse': {
        'color':  56, 'icon': '😈',
        'deals': 'none',
        'max_amount': 3,
        'at_max': 'ignore',
    },
    'stun': {
        'color': 184, 'icon': '😵',
        'deals': 'thunder',
        'max_amount': 3,
        'at_max': 'ignore',
    },
    'sleep': {
        'color': 107, 'icon': '💤',
        'deals': 'none',
        'max_amount': 3,
        'at_max': 'ignore',
    },
    'tough': {
        'color':  94, 'icon': '🛡️',
        'deals': 'none',
        'max_amount': 3,
        'at_max': 'ignore',
    },
    'strong': {
        'color':   1, 'icon': '💪',
        'deals': 'none',
        'max_amount': 3,
        'at_max': 'ignore',
    }
}



class character:

    def __init__(self, name:str, element_1:str, element_2:str, temperament:int):
        """
            Constructor Function for the 'Outside of Combat' Character Object.
            This has been built with the intent of being easily copied and modified,
            It might need to be updated in order to reflect creating opponents, though.
            The Build Starter function was made for testing and would be better shifted
            to a model that takes data from a csv or json file, as per the games intented functionality
        """
        self.name:          str =   name
        self.level:         int =   1
        self.max_hp:        int =   10
        self.hp:            int =   self.max_hp
        self.iters:         int =   1
        self.elites_slain:  int =   0
        self.bless_burden:  int =   0



        self.chosen_move:   str =   ""  # Should Probably be the 'move object' rather than just the name?
        self.has_priority:  bool =  False
        
        self.active_moves:  dict =  {}
        self.banked_moves:  dict =  {}
        self.bound_moves:   dict =  {}
        self.blessings:     dict =  {}
        self.attunements:   dict =  {}
        self.statuses:      dict =  {}
        self.move_history:  dict =  {}

        self.starter_moves: dict =  Build_Starter(element_1, element_2, temperament)


#--- Example of Dictionaries filling out at start of Combat:

# Fills out 'attuned_to' dict with default values
for element_name in STYLE_REF['element'].keys():
    style = STYLE_REF['element'].get(element_name, {})
    self.attunements[element_name] = {
        'public':   False,
        'turns':    0,
        'color':    style.get('color', 'white')
        'icon':     style.get('icon', '?')
    }

# Updates the attunements dict to reflect pre-attunement ala special blessings
for blessing in self.blessings:
    for element_name in self.attunements:
        if blessing['pre_attune'] == element_name:
            style = STYLE_REF['element'].get(element_name, {})
            self.attunements[element_name] = {
                'public':   False
                'turns':    1
                'color':    style.get('color', 'white')
                'icon':     style.get('icon', '?')
            }

# Fills out 'status' dict with default values
for status_name in STYLE_REF['status'].keys():
    style = STYLE_REF['status'].get(status_name, {})
    self.statuses[status_name] = {
        'immune_to':False,
        'ignores':  False,
        'turns':    0,
        'color':    style.get('color', 'white'),
        'icon':     style.get('icon', '?')
    }

# Updates the attunements dict to reflect pre-attunement ala special blessings
for blessing in self.blessings:
    for status_name in self.statuses:
        if blessing['pre_status'] == status_name:
            style = STYLE_REF['status'].get(status_name, {})
            self.statuses[status_name] = {
                'immune_to':False
                'ignores':  False
                'turns':    1
                'color':    style.get('color', 'white')
                'icon':     style.get('icon', '?')
            }

    def print_vars(self):
        '''
        Prints Out Color-Coded Variable Updates for Players
        '''
        print("+--------------------------------------------------+")
        print("+---",end="")
        print(colored(f"[ {self.name} ]", 'green'),end="---+\n")
        print(colored(f" HP: ", "light_red"),end=f"{self.hp} / {self.max_hp}    ")
        print(colored(f"ITER:", "yellow"),end=f" {self.iters}\n")

        # Attuned
        print("\n+---",end="")
        print(colored("[ ATTUNED ]", 'yellow'),end="---+\n  ")
        for element_name, data in self.attuned.items():
            print(colored_256(f"{data['icon']} {element_name[:3]}:", data['color']),end=" ") 
            print(f"{data['turns']}",end=" ")
        print("\n",end="  ")

        # Publicity
        for element_name, data in self.attuned.items():
            icon = "<o>"
            if data['public'] != True:
                icon = "---"
            print(colored(f"    {icon}", "grey"),end="")
        
        # Status
        print("\n+---",end="")
        print(colored("[ STATUSES ]", 'light_blue'),end="---+\n")
        status_count = 0
        for status_name, data in self.statuses.items():
            if data['immune_to']== True:
                print('⛨ ',end="")
            else:
                print('  ',end="")
            print(colored_256(f"{data['icon']} {status_name[:3]}:", data['color']),end=" ") 
            print(f"{data['turns']}",end=" ")
            status_count += 1
            if status_count % 6 == 0:
                print("")

        # Priority
        print("\n+---",end="")
        print(colored("[ PRIORITY ]", "light_red"),end="---+\n")
        print(colored(f"    {self.has_priority}", "yellow"))

        # Moves
        print("\n+---",end="")
        print(colored("[ MOVES ]", "cyan"),end="---+\n")
        for move_name, data in self.active_moves.items():
            logo_color = data['color']
            if data['type']== "attack":
                logo = ' ⚔   '
            else:
                logo = ' ⛨   '
            print(colored_256(f"{logo}", logo_color),end=f"{move_name}\n")

        # End
        print("+--------------------------------------------------+\n")

def Build_Starter(element_1:str, element_2:str, temperament:int):
    move_data = {
        "water": { "attack": {"Roll Tide","Cache Flow"},
                   "utility": {"Mistify", "Wash Out"}
        },
        "stone": { "attack": {"Stone Toss", "Shift Plate"},
                    "utility": {"Try Hard", "Mud Bathe"}
        },
        "fire":  {  "attack": { "Flare Up","Burn Notice"},
                    "utility": {"Furnish Flames","Sweat Out"}
        },
        "plant": {  "attack": {"Root Out","Branch Out"},
                    "utility": {"Restore","Bind Guess"}
        },
        "vital": {  "attack": {"Tear Into","Open Wounds"},
                    "utility": {"Acquired Taste","Blood Shot"}
        },
        "force": {  "attack": {"Blow Hard","Ill Wind"},
                    "utility": {"Make Sick","Pestilate"}
        },
        "thunder": {
            "attack": {"General Strike","Bolt Back"},
            "utility": {"Change Up","Thought Storm"}
            }
        }
    moves: list = []
    attacks: list = []
    utilities: list = []
    for element in [element_1, element_2]:
        style = STYLE_REF['element'].get(element, {})
        for move in move_data[element]['attack']:
            attacks.append({
                'name': move,
                'type': 'attack',
                'element': element,
                'color': style.get('color', 'white'),
                'icon': '⚔'
            })
        for move in move_data[element]['utility']:
            utilities.append({
                'name': move,
                'type': 'utility',
                'element': element,
                'color': style.get('color', 'white'),
                'icon': '⛨'
            })

    # Add Attacks
    while temperament > 0:
        if not attacks:
            break
        move = random.choice(attacks)
        moves.append(move)
        attacks.remove(move)
        temperament -= 1

    # Add Utilities
    while len(moves) < 4:
        if not utilities:
            break
        move = random.choice(utilities)
        moves.append(move)
        utilities.remove(move)

    moves_dict = {move['name']: move for move in moves}
    return moves_dict

#--- Example of Dictionaries filling out at start of Combat:

# Fills out 'attuned_to' dict with default values
for element_name in STYLE_REF['element'].keys():
    style = STYLE_REF['element'].get(element_name, {})
    self.attunements[element_name] = {
        'public':   False,
        'turns':    0,
        'color':    style.get('color', 'white')
        'icon':     style.get('icon', '?')
    }

# Updates the attunements dict to reflect pre-attunement ala special blessings
for blessing in self.blessings:
    for element_name in self.attunements:
        if blessing['pre_attune'] == element_name:
            style = STYLE_REF['element'].get(element_name, {})
            self.attunements[element_name] = {
                'public':   False
                'turns':    1
                'color':    style.get('color', 'white')
                'icon':     style.get('icon', '?')
            }

# Fills out 'status' dict with default values
for status_name in STYLE_REF['status'].keys():
    style = STYLE_REF['status'].get(status_name, {})
    self.statuses[status_name] = {
        'immune_to':False,
        'ignores':  False,
        'turns':    0,
        'color':    style.get('color', 'white'),
        'icon':     style.get('icon', '?')
    }

# Updates the attunements dict to reflect pre-attunement ala special blessings
for blessing in self.blessings:
    for status_name in self.statuses:
        if blessing['pre_status'] == status_name:
            style = STYLE_REF['status'].get(status_name, {})
            self.statuses[status_name] = {
                'immune_to':False
                'ignores':  False
                'turns':    1
                'color':    style.get('color', 'white')
                'icon':     style.get('icon', '?')
            }
```
