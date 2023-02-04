from random import choice, randint


class SingleColour():
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length

class TwoColour():
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class SpeckledTabby():
    name = "SpeckledTabby"
    sprites = {1: 'speckledtabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} speckledtabby"
        else:
            return self.colour + self.length + " speckledtabby"

class Stain():
    name = "Stain"
    sprites = {1: 'stain', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} stain"
        else:
            return self.colour + self.length + " stain"

class VoiSokoke():
    name = "VoiSokoke"
    sprites = {1: 'voisokoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} voisokoke"
        else:
            return self.colour + self.length + " voisokoke"

class Tabby():
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"

class Marbled():
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"

class Rosette():
    name = "Rosette"
    sprites = {1: 'rosette', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosette"
        else:
            return self.colour + self.length + " rosette"

class Smoke():
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"

class Ticked():
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"

class Speckled():
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"

class Bengal():
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"

class Mackerel():
    name = "Mackerel"
    sprites = {1: 'mackerel', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} mackerel tabby{self.length}"
        else:
            return f"{self.colour} mackerel tabby{self.length}"

class Classic():
    name = "Classic"
    sprites = {1: 'classic', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} classic tabby{self.length}"
        else:
            return f"{self.colour} classic tabby{self.length}"

class Sokoke():
    name = "Sokoke"
    sprites = {1: 'sokoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} sokoke tabby{self.length}"
        else:
            return f"{self.colour} sokoke tabby{self.length}"

class Agouti():
    name = "Agouti"
    sprites = {1: 'agouti', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} agouti{self.length}"
        else:
            return f"{self.colour} agouti{self.length}"

class Singlestripe():
    name = "Singlestripe"
    sprites = {1: 'singlestripe', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} singlestripe{self.length}"
        else:
            return f"{self.colour} singlestripe{self.length}"

class Tortie():
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}

    def __init__(self, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = choice(tortiecolours)
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"

class Calico():
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}

    def __init__(self, length):
        self.colour = choice(tortiecolours)
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"

#---------------------------------------------- BAT

class Bat_Single():
    name = "Bat_Single"
    sprites = {1: 'bat_single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length

class Bat_TwoColour():
    name = "Bat_TwoColour"
    sprites = {1: 'bat_single', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Bat_Tabby():
    name = "Bat_Tabby"
    sprites = {1: 'bat_tabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bat_tabby{self.length}"
        else:
            return f"{self.colour} bat_tabby{self.length}"

class Bat_Speckled():
    name = "Bat_Speckled"
    sprites = {1: 'bat_speckled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bat_speckled{self.length}"
        else:
            return f"{self.colour} bat_speckled{self.length}"

class Bat_Tortie():
    name = "Bat_Tortie"
    sprites = {1: 'bat_torties', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} Bat_Tortie{self.length}"
        else:
            return f"{self.colour} Bat_Tortie{self.length}"



# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
]
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
    'PEACHYELLOW', 'MOCHA', 'METALLICBRONZE', 'WALNUT', 'FOX', 'ESPRESSO', 'PALEORANGE', 'PALECARMINE', 'CARAMEL', 'SIENNA', 'VANILLA', 'MUSHROOM',
    'COFFEE', 'RICHGOLD', 'MOCCACCINO', 'PALEBROWN', 'DUSTYPINK', 'GRASSY', 'VAMPIRE', 'DOVE', 'GRAVEL', 'SLATEGREY',
    'CADETBLUE', 'OLDLAVENDER', 'COMET', 'MIDGREY', 'IRONGREY', 'DUST', 'VIOLET', 'DARKVIOLET', 'BLUEVIOLET', 'CHARCOAL', 'ASH', 'PALEVIOLET',
]
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER', 'GOLDEN', 'GINGER',
    'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'PEACHYELLOW', 'MOCHA', 'METALLICBRONZE', 'WALNUT', 'FOX', 'ESPRESSO', 'PALEORANGE', 'PALECARMINE', 'CARAMEL', 'SIENNA', 'VANILLA', 'MUSHROOM',
    'COFFEE', 'RICHGOLD', 'MOCCACCINO', 'PALEBROWN', 'DUSTYPINK', 'GRASSY', 'VAMPIRE', 'DOVE', 'GRAVEL', 'SLATEGREY',
    'CADETBLUE', 'OLDLAVENDER', 'COMET', 'MIDGREY', 'IRONGREY', 'DUST', 'VIOLET', 'DARKVIOLET', 'BLUEVIOLET', 'CHARCOAL', 'ASH', 'PALEVIOLET',
]
pelt_colours_modded = ['PEACHYELLOW', 'MOCHA', 'METALLICBRONZE', 'WALNUT', 'FOX', 'ESPRESSO', 'PALEORANGE', 'PALECARMINE', 'CARAMEL', 'SIENNA', 'VANILLA', 'MUSHROOM',
                       'COFFEE', 'RICHGOLD', 'MOCCACCINO', 'PALEBROWN', 'DUSTYPINK', 'GRASSY', 'CLOUD', 'VAMPIRE', 'DOVE', 'GRAVEL', 'SLATEGREY', 'ICE',
                       'CADETBLUE', 'OLDLAVENDER', 'COMET', 'MIDGREY', 'IRONGREY', 'DUST', 'VIOLET', 'DARKVIOLET', 'BLUEVIOLET', 'CHARCOAL', 'ASH', 'PALEVIOLET']
all_colours = ['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
               'PEACHYELLOW', 'MOCHA', 'METALLICBRONZE', 'WALNUT', 'FOX', 'ESPRESSO', 'PALEORANGE', 'PALECARMINE', 'CARAMEL', 'SIENNA', 'VANILLA', 'MUSHROOM',
                       'COFFEE', 'RICHGOLD', 'MOCCACCINO', 'PALEBROWN', 'DUSTYPINK', 'GRASSY', 'CLOUD', 'VAMPIRE', 'DOVE', 'GRAVEL', 'SLATEGREY', 'ICE',
                       'CADETBLUE', 'OLDLAVENDER', 'COMET', 'MIDGREY', 'IRONGREY', 'DUST', 'VIOLET', 'DARKVIOLET', 'BLUEVIOLET', 'CHARCOAL', 'ASH', 'PALEVIOLET']
all_colours_nw = ['PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
               'PEACHYELLOW', 'MOCHA', 'METALLICBRONZE', 'WALNUT', 'FOX', 'ESPRESSO', 'PALEORANGE', 'PALECARMINE', 'CARAMEL', 'SIENNA', 'VANILLA', 'MUSHROOM',
                       'COFFEE', 'RICHGOLD', 'MOCCACCINO', 'PALEBROWN', 'DUSTYPINK', 'GRASSY', 'VAMPIRE', 'DOVE', 'GRAVEL', 'SLATEGREY',
                       'CADETBLUE', 'OLDLAVENDER', 'COMET', 'MIDGREY', 'IRONGREY', 'DUST', 'VIOLET', 'DARKVIOLET', 'BLUEVIOLET', 'CHARCOAL', 'ASH', 'PALEVIOLET']

batpelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
]
batpelt_coloursnw = [
     'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
]
oldtortie = ['BLACK1', 'BLACK2', 'BLACK3', 'BLACK4', 'BLACK5', 'BLACK6', 'SILVER1', 'SILVER2', 'SILVER3', 'SILVER4', 'SILVER5', 'SILVER6', 'BROWN1', 'BROWN2', 'BROWN3', 'BROWN4', 'BROWN5', 'BROWN6']

tortiepatterns = ['tortiesolid', 'tortietabby', 'tortiebengal', 'tortiemarbled', 'tortieticked',
    'tortiesmoke', 'tortierosette', 'tortiespeckled', 'tortiemackerel', 'tortieclassic',
    'tortiesokoke', 'tortieagouti', 'tortievoisokoke', 'tortiespeckledtabby', 'tortiecombo']
patch_colours = ['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'GOLDONE', 'GOLDTWO',
    'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR', 'CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
    'classic', 'sokoke', 'agouti', 'singlestripe', 'voisokoke', 'speckledtabby', 'stain']
tortiecolours = ["SILVER", "GREY", "DARKGREY", "BLACK", "LIGHTBROWN", "BROWN", "DARKBROWN",
                 ]

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
    'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'BLUE2', 'SUNLITICE', 'GREENYELLOW']
yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'COPPER', 'GREENYELLOW']
blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'BLUE2', 'SUNLITICE', 'GREY']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
# bite scars by @wood pank on discord
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
          "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK",]

plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                    "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                    "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "PINK", "PURPLE", "MULTI", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW",
    "WHITEMANE", "PALEGREYMANE", "SILVERMANE", "GREYMANE", "DARKGREYMANE", "BLACKBLACK", "PALEGINGERMANE", "GOLDENMANE", "GINGERMANE", "DARKGINGERMANE",
    "LIGHTBROWNMANE" "BROWNMANE" "DARKBROWNMANE", "VINES1", "VINES2", "VINES3", "VINES4", "VINES5", "VINES6", "GLASSES1", "GLASSES2", "GLASSES3", "GLASSES4",
    "GLASSES5", "VINES7", "VINES8", "CRIMSONCAPE", "BLUECAPE", "YELLOWCAPE", "CYANCAPE", "REDCAPE", "LIMECAPE", "GREENCAPE", "RAINBOWCAPE", "BLACKCAPE",
    "SPIKESCAPE", "PINKCAPE", "PURPLECAPE", "MULTICAPE"
]

tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti", "VoiSokoke"]
spotted = ["Speckled", "Rosette", "SpeckledTabby"]
plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe", "Bat_SingleColour", "Bat_TwoColour"]
exotic = ["Bengal", "Marbled", "Stain"]
torties = ["Tortie", "Calico"]
pelt_categories = [tabbies, spotted, plain, exotic, torties]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK'
]
ginger_colours = ['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']
black_colours = ['GREY', 'DARKGREY', 'GHOST', 'BLACK',
                  'VAMPIRE', 'DOVE', 'GRAVEL', 'SLATEGREY',
                       'CADETBLUE', 'OLDLAVENDER', 'COMET', 'MIDGREY', 'IRONGREY', 'DUST', 'VIOLET', 'DARKVIOLET', 'BLUEVIOLET', 'CHARCOAL', 'ASH', 'PALEVIOLET']
white_colours = ['WHITE', 'PALEGREY', 'SILVER',
                 'CLOUD', 'ICE']
brown_colours = ['LIGHTBROWN', 'BROWN', 'DARKBROWN',
                 'PEACHYELLOW', 'MOCHA', 'METALLICBRONZE', 'WALNUT', 'FOX', 'ESPRESSO', 'PALEORANGE', 'PALECARMINE', 'CARAMEL', 'SIENNA', 'VANILLA', 'MUSHROOM',
                       'COFFEE', 'RICHGOLD', 'MOCCACCINO', 'PALEBROWN', 'DUSTYPINK', 'GRASSY']
colour_categories = [ginger_colours, black_colours, white_colours, brown_colours]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
    'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'BLUE2', 
    'SUNLITICE', 'GREENYELLOW'
]
little_white = ['LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                'BLACKLITTLE', 'BLACKLIGHTTUXEDO', 'BLACKBUZZARDFANG', 'BLACKLITTLECREAMY', 'GINGERLITTLE', 'GINGERLIGHTTUXEDO', 'GINGERBUZZARDFANG', 'GINGERLITTLECREAMY', 'BROWNLITTLE', 'BROWNLIGHTTUXEDO', 'BROWNBUZZARDFANG', 'BROWNLITTLECREAMY',
    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY']
mid_white = ['TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
             'BLACKTUXEDOCREAMY', 'BLACKTUXEDO', 'GINGERTUXEDOCREAMY', 'GINGERTUXEDO', 'BROWNTUXEDOCREAMY', 'BROWNTUXEDO']
high_white = ['ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2',
              'BLACKANY', 'BLACKANY2', 'BLACKANY2CREAMY', 'BLACKBROKEN', 'BLACKANYCREAMY', 'GINGERANY', 'GINGERANY2', 'GINGERANY2CREAMY', 'GINGERBROKEN', 'GINGERANYCREAMY', 'BROWNANY', 'BROWNANY2', 'BROWNANY2CREAMY', 'BROWNBROKEN', 'BROWNANYCREAMY',
    'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'GLASS', 'MASKMANTLE']
mostly_white = ['VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                'BLACKVANCREAMY', 'BLACKLIGHTSONG', 'BONEEAR', 'BLACKVAN', 'GINGERVANCREAMY', 'GINGERLIGHTSONG', 'GINGERONEEAR', 'GINGERVAN', 'BROWNVANCREAMY', 'BROWNLIGHTSONG', 'BROWNONEEAR', 'BROWNVAN']
point_markings = ['COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'KARPATI', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT',
                  'BAGDOLL', 'BLACKCOLOURPOINTCREAMY', 'BLACKCOLOURPOINT', 'GINGERRAGDOLL', 'GINGERCOLOURPOINTCREAMY', 'GINGERCOLOURPOINT', 'BROWNRAGDOLL', 'BROWNCOLOURPOINTCREAMY', 'BROWNCOLOURPOINT']
vit = ['VITILIGO', 'VITILIGO2', 'BLACKVITILIGO', 'GINGERVITILIGO', 'BROWNVITILIGO']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE', 'FULLBLACK', 'FULLBROWN', 'FULLGINGER', 'EXTRA'
]

# 'BLACKANY', 'BLACKTUXEDO', 'BLACKLITTLE', 'BLACKCOLOURPOINT', 'BLACKVAN', 'BLACKANY2', 'BONEEAR', 'BLACKBROKEN', 'BLACKLIGHTTUXEDO', 'BLACKBUZZARDFANG', 'BAGDOLL', 'BLACKLIGHTSONG', 'BLACKVITILIGO', 'BLACKANYCREAMY', 'BLACKTUXEDOCREAMY', 'BLACKLITTLECREAMY', 'BLACKCOLOURPOINTCREAMY', 'BLACKVANCREAMY', 'BLACKANY2CREAMY'
# 'BROWNANY', 'BROWNTUXEDO', 'BROWNLITTLE', 'BROWNCOLOURPOINT', 'BROWNVAN', 'BROWNANY2', 'BROWNONEEAR', 'BROWNBROKEN', 'BROWNLIGHTTUXEDO', 'BROWNBUZZARDFANG', 'BROWNRAGDOLL', 'BROWNLIGHTSONG', 'BROWNVITILIGO', 'BROWNANYCREAMY', 'BROWNTUXEDOCREAMY', 'BROWNLITTLECREAMY', 'BROWNCOLOURPOINTCREAMY', 'BROWNVANCREAMY', 'BROWNANY2CREAMY',
# 'GINGERANY', 'GINGERTUXEDO', 'GINGERLITTLE', 'GINGERCOLOURPOINT', 'GINGERVAN', 'GINGERANY2', 'GINGERONEEAR', 'GINGERBROKEN', 'GINGERLIGHTTUXEDO', 'GINGERBUZZARDFANG', 'GINGERRAGDOLL', 'GINGERLIGHTSONG', 'GINGERVITILIGO', 'GINGERANYCREAMY', 'GINGERTUXEDOCREAMY', 'GINGERLITTLECREAMY', 'GINGERCOLOURPOINTCREAMY', 'GINGERVANCREAMY', 'GINGERANY2CREAMY'


skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']


# CHOOSING PELT
def choose_pelt(colour=None, white=None, pelt=None, length=None, category=None, determined=False):
    colour = colour
    white = white
    pelt = pelt
    length = length
    category = category
    if pelt is None:
        if category != None:
            pelt = choice(category)
    else:
        pelt = pelt
    if length is None:
        length = choice(pelt_length)
    if pelt == 'SingleColour':
        if colour is None and not white:
            return SingleColour(choice(all_colours), length)
        elif colour == None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == 'TwoColour':
        if colour == None:
            return TwoColour(choice(all_colours_nw), length)
        else:
            return TwoColour(colour, length)
    elif pelt == "SpeckledTabby":
        if colour is None and white is None:
            return SpeckledTabby(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return SpeckledTabby(choice(all_colours), white, length)
        else:
            return SpeckledTabby(colour, white, length)
    elif pelt == "Stain":
        if colour is None and white is None:
            return Stain(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return Stain(choice(all_colours), white, length)
        else:
            return Stain(colour, white, length)
    elif pelt == "VoiSokoke":
        if colour is None and white is None:
            return VoiSokoke(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return VoiSokoke(choice(all_colours), white, length)
        else:
            return VoiSokoke(colour, white, length)
    elif pelt == 'Tabby':
        if colour is None and white is None:
            return Tabby(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return Tabby(choice(all_colours), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == 'Marbled':
        if colour is None and white is None:
            return Marbled(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return Marbled(choice(all_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == 'Rosette':
        if colour is None and white is None:
            return Rosette(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return Rosette(choice(all_colours), white, length)
        else:
            return Rosette(colour, white, length)
    elif pelt == 'Smoke':
        if colour is None and white is None:
            return Smoke(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return Smoke(choice(all_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == 'Ticked':
        if colour is None and white is None:
            return Ticked(choice(all_colours), choice([False, True]), length)
        elif colour == None:
            return Ticked(choice(all_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == 'Speckled':
        if colour is None and white is None:
            return Speckled(choice(all_colours), choice([False, True]),
                            length)
        elif colour == None:
            return Speckled(choice(all_colours), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == 'Bengal':
        if colour is None and white is None:
            return Bengal(choice(all_colours), choice([False, True]),
                             length)
        elif colour == None:
            return Bengal(choice(all_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == 'Mackerel':
        if colour is None and white is None:
            return Mackerel(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour == None:
            return Mackerel(choice(pelt_colours), white, length)
        else:
            return Mackerel(colour, white, length)
    elif pelt == 'Classic':
        if colour is None and white is None:
            return Classic(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour == None:
            return Classic(choice(pelt_colours), white, length)
        else:
            return Classic(colour, white, length)
    elif pelt == 'Sokoke':
        if colour is None and white is None:
            return Sokoke(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour == None:
            return Sokoke(choice(pelt_colours), white, length)
        else:
            return Sokoke(colour, white, length)
    elif pelt == 'Agouti':
        if colour is None and white is None:
            return Agouti(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour == None:
            return Agouti(choice(pelt_colours), white, length)
        else:
            return Agouti(colour, white, length)
    elif pelt == 'Singlestripe':
        if colour is None and white is None:
            return Singlestripe(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour == None:
            return Singlestripe(choice(pelt_colours), white, length)
        else:
            return Singlestripe(colour, white, length)
    elif pelt == 'Bat_Single':
        if colour == None and not white:
            return Bat_Single(choice(batpelt_colours), length)
        elif colour == None:
            return Bat_Single("WHITE", length)
        else:
            return Bat_Single(colour, length)
    elif pelt == 'Bat_TwoColour':
        if colour == None:
            return Bat_TwoColour(choice(batpelt_coloursnw), length)
        else:
            return Bat_TwoColour(colour, length)
    elif pelt == "Bat_Tabby":
        if colour is None and white is None:
            return Bat_Tabby(choice(batpelt_colours), choice([False, True]), length)
        elif colour == None:
            return Bat_Tabby(choice(batpelt_colours), white, length)
        else:
            return Bat_Tabby(colour, white, length)
    elif pelt == "Bat_Speckled":
        if colour is None and white is None:
            return Bat_Speckled(choice(batpelt_colours), choice([False, True]), length)
        elif colour == None:
            return Bat_Speckled(choice(batpelt_colours), white, length)
        else:
            return Bat_Speckled(colour, white, length)
    elif pelt == "Bat_Tortie":
        if colour is None and white is None:
            return Bat_Tortie(choice(oldtortie), choice([False, True]), length)
        elif colour == None:
            return Bat_Tortie(choice(oldtortie), white, length)
        else:
            return Bat_Tortie(colour, white, length)
    elif pelt == "SpeckledTabby":
        if colour is None and white is None:
            return SpeckledTabby(choice(pelt_colours), choice([False, True]), length)
        elif colour == None:
            return SpeckledTabby(choice(pelt_colours), white, length)
        else:
            return SpeckledTabby(colour, white, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(choice([False, True]), length)
        else:
            return Tortie(white, length)
    else:
        return Calico(length)

def describe_color(pelt, tortiecolour, tortiepattern, white_patches):
        color_name = ''
        color_name = str(pelt.colour).lower()
        if tortiecolour is not None:
            color_name = str(tortiecolour).lower()
        if color_name == 'palegrey':
            color_name = 'pale grey'
        elif color_name == 'darkgrey':
            color_name = 'dark grey'
        elif color_name == 'paleginger':
            color_name = 'pale ginger'
        elif color_name == 'darkginger':
            color_name = 'dark ginger'
        elif color_name == 'lightbrown':
            color_name = 'light brown'
        elif color_name == 'darkbrown':
            color_name = 'dark brown'
        elif color_name == 'peachyellow':
            color_name = 'peachy yellow'
        elif color_name == 'metallicbronze':
            color_name = 'metallic bronze'
        elif color_name == 'paleorange':
            color_name = 'pale orange'
        elif color_name == 'palecarmine':
            color_name = 'pale carmine'
        elif color_name == 'richgold':
            color_name = 'rich gold'
        elif color_name == 'palebrown':
            color_name = 'pale brown'
        elif color_name == 'dustypink':
            color_name = 'dusty pink'
        elif color_name == 'slategrey':
            color_name = 'slate grey'
        elif color_name == 'cadetblue':
            color_name = 'cadet blue'
        elif color_name == 'oldlavender':
            color_name = 'old lavender'
        elif color_name == 'midgrey':
            color_name = 'mid grey'
        elif color_name == 'irongrey':
            color_name = 'iron grey'
        elif color_name == 'darkviolet':
            color_name = 'dark violet'
        elif color_name == 'blueviolet':
            color_name = 'blue violet'
        elif color_name == 'paleviolet':
            color_name = 'pale violet'
        if pelt.name == "Tabby":
            color_name = color_name + ' tabby'
        elif pelt.name == "SpeckledTabby":
            color_name = color_name + ' speckled tabby'
        elif pelt.name == "Stain":
            color_name = color_name + ' stained'
        elif pelt.name == "VoiSokoke":
            color_name = color_name + ' voisokoke'
        elif pelt.name == "Speckled":
            color_name = color_name + ' speckled'
        elif pelt.name == "Bengal":
            color_name = color_name + ' bengal'
        elif pelt.name == "Marbled":
            color_name = color_name + ' marbled tabby'
        elif pelt.name == "Rosette":
            color_name = color_name + ' rosetted'
        elif pelt.name == "Ticked":
            color_name = color_name + ' ticked tabby'
        elif pelt.name == "Smoke":
            color_name = color_name + ' smoke'
        elif pelt.name == "Mackerel":
            color_name = color_name + ' mackerel tabby'
        elif pelt.name == "Classic":
            color_name = color_name + ' classic tabby'
        elif pelt.name == "Sokoke":
            color_name = color_name + ' sokoke tabby'
        elif pelt.name == "Agouti":
            color_name = color_name + ' agouti'
        elif pelt.name == "Singlestripe":
            color_name = color_name + ', with a dorsal stripe,'
        elif pelt.name == "Bat_Single":
            color_name = color_name + ' Bat SingleColour'
        elif pelt.name == "Bat_TwoColour":
            color_name = color_name + ' Bat TwoColour'

        elif pelt.name == "Tortie":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' torbie'
            else:
                color_name = color_name + ' tortie'
        elif pelt.name == "Calico":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' tabico'
            else:
                color_name = color_name + ' calico'
        # enough to comment but not make calico
        if white_patches is not None:
            if white_patches in little_white + mid_white:
                color_name = color_name + ' and white'
            # and white
            elif white_patches in high_white:
                if pelt.name != "Calico":
                    color_name = color_name + ' and white'
            # white and
            elif white_patches in mostly_white:
                color_name = 'white and ' + color_name
            # colorpoint
            elif white_patches in point_markings:
                color_name = color_name + ' point'
                if color_name == 'dark ginger point' or color_name == 'ginger point':
                    color_name = 'flame point'
            # vitiligo
            elif white_patches in vit:
                color_name = color_name + ' with vitiligo'
        else:
            color_name = color_name

        if color_name == 'tortie':
            color_name = 'tortoiseshell'

        if white_patches == 'FULLWHITE':
            color_name = 'white'
        if white_patches == 'FULLBLACK':
            color_name = 'black'
        if white_patches == 'FULLBROWN':
            color_name = 'brown'
        if white_patches == 'FULLGINGER':
            color_name = 'ginger'

        if color_name == 'white and white':
            color_name = 'white'

        return color_name
